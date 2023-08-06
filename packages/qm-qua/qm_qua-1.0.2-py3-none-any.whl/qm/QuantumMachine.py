import json
import logging
from typing import Optional, Union, List, Tuple, Dict

import numpy
from deprecation import deprecated
from qm.QmPendingJob import QmPendingJob

from qm.QmQueue import QmQueue
from qm.QmJob import QmJob
from qm.octave.qm_octave import QmOctave
from qm.utils import fix_object_data_type as _fix_object_data_type
from qm.pb.frontend_pb2 import QmDataRequest, PokeRequest, CompileRequest
from qm.pb.inc_qm_api_pb2 import HighQmApiRequest, HighQmApiResponse, RISING, FALLING
from qm.pb.qm_manager_pb2 import CloseQuantumMachineRequest, GetRunningJobRequest
from qm.program import _Program
from qm.simulate.interface import SimulationConfig
from grpc._channel import _InactiveRpcError
from qm.utils import _level_map, _set_compiler_options
from qm.exceptions import CompilationException, JobCancelledError, InvalidConfigError
from qm._QmJobErrors import (
    InvalidDigitalInputPolarityError,
)


logger = logging.getLogger(__name__)


class QuantumMachine(object):
    def __init__(self, machine_id, pb_config, config, manager):
        super(QuantumMachine, self).__init__()
        self._id = machine_id
        self.id = machine_id
        self._pb_config = pb_config
        self._config = config
        self._manager = manager
        self._frontend = manager._frontend
        self._queue = QmQueue(self, manager)
        self._octave = QmOctave(self, self._manager.octave_manager)

    @property
    def queue(self) -> QmQueue:
        """
        Returns the queue for the Quantum Machine
        """
        return self._queue

    @property
    def manager(self) -> "qm.QuantumMachinesManager.QuantumMachinesManager":
        """
        Returns the Quantum Machines Manager
        """
        return self._manager

    @property
    def octave(self) -> QmOctave:
        return self._octave

    def close(self):
        """
        Closes the quantum machine.

        :return: ``True`` if the close request succeeded, raises an exception otherwise.
        """
        request = CloseQuantumMachineRequest()
        request.machineID = self._id

        result = self._frontend.CloseQuantumMachine(request)
        if not result.success:
            error_str = ""
            for err in result.errors:
                error_str = error_str + err.message + "\n"
            exception = Exception(error_str)
            exception.errors = [(it.code, it.message) for it in result.errors]
            raise exception

        return result.success

    def simulate(self, program, simulate, **kwargs):
        """
        Simulate the outputs of a deterministic QUA program.

        Equivalent to ``execute()`` with ``simulate=SimulationConfig`` (see example).

        .. note::
            A simulated job does not support calling QuantumMachine API functions.

        The following example shows a simple execution of the simulator, where the
        associated config object is omitted for brevity.

        Example::

            >>> from qm.QuantumMachinesManager import QuantumMachinesManager
            >>> from qm.qua import *
            >>> from qm.simulate import SimulationConfig
            >>>
            >>> qmManager = QuantumMachinesManager()
            >>> qm1 = qmManager.open_qm(config)
            >>>
            >>> with program() as prog:
            >>>     play('pulse1', 'element1')
            >>>
            >>> job = qm1.simulate(prog, SimulationConfig(duration=100))

        :param program: A QUA ``program()`` object to execute
        :param simulate: A ``SimulationConfig`` configuration object
        :param kwargs: additional parameteres to pass to execute
        :return: a ``QmJob`` object (see QM Job API).
        """
        kwargs["simulate"] = simulate
        try:
            job = self.execute(program, **kwargs)
        except _InactiveRpcError as e:
            raise RuntimeError("Error encountered while compiling") from e
        return job

    def execute(
        self,
        program,
        duration_limit=1000,
        data_limit=20000,
        force_execution=False,
        dry_run=False,
        **kwargs,
    ) -> QmJob:
        """
        Executes a program and returns an job object to keep track of execution and get
        results.

        .. note::

            Calling execute will halt any currently running program and clear the current
            queue. If you want to add a job to the queue, use qm.queue.add()

        :param program: A QUA ``program()`` object to execute

        :param duration_limit: This parameter is ignored as it is obsolete
        :type duration_limit: int
        :param data_limit: This parameter is ignored as it is obsolete
        :type data_limit: int
        :param force_execution: This parameter is ignored as it is obsolete
        :type force_execution: bool
        :param dry_run: This parameter is ignored as it is obsolete
        :type dry_run: bool

        :return: A ``QmJob`` object (see QM Job API).

        """
        if type(program) is not _Program:
            raise Exception("program argument must be of type qm.program.Program")

        simulation = kwargs.get("simulate", None)
        if type(simulation) is SimulationConfig:
            kwargs.pop("simulate")
            return self._manager.simulate(
                self.get_config(), program, simulation, **kwargs
            )

        self._queue.clear()
        current_running_job = self.get_running_job()
        if current_running_job is not None:
            current_running_job.halt()
        pending_job = self._queue.add(program, **kwargs)
        logger.info("Executing program")
        return pending_job.wait_for_execution(timeout=5)

    def compile(self, program: _Program, **kwargs) -> str:
        """
        Compiles a QUA program to be executed later. The returned `program_id`
        can then be directly added to the queue. For a detailed explanation
        see `Precompile Jobs <https://qm-docs.qualang.io/guides/features.html#precompile-jobs>`__.

        :param program: A QUA program
        :return: a program_id str

        Example::

        >>> program_id = qm.compile(program)
        >>> pending_job = qm.queue.add_compiled(program_id)
        >>> job = pending_job.wait_for_execution()
        """
        request = CompileRequest()
        request.quantumMachineId = self.id
        ast = program.build(self._pb_config)
        request.highLevelProgram.CopyFrom(ast)

        _set_compiler_options(request, **kwargs)

        logger.info("Compiling program")

        response = self._manager._frontend.Compile(request)
        messages = [(_level_map[msg.level], msg.message) for msg in response.messages]
        program_id = response.programId

        for lvl, msg in messages:
            logger.log(lvl, msg)

        if not response.ok:
            logger.error("Compilation of program " + program_id + " failed")
            raise CompilationException(program_id)

        return program_id

    def list_controllers(self):
        """
        Gets a list with the defined controllers in this qm

        :return: The names of the controllers configured in this qm
        """
        return tuple(self.get_config()["controllers"].keys())

    def set_mixer_correction(self, mixer, intermediate_frequency, lo_frequency, values):
        """
        Sets the correction matrix for correcting gain and phase imbalances
        of an IQ mixer for the supplied intermediate frequency and LO frequency.

        :param mixer: the name of the mixer, as defined in the configuration
        :type mixer: str
        :param intermediate_frequency: the intermediate frequency for which to apply the correction matrix
        :type intermediate_frequency: int
        :param lo_frequency: the LO frequency for which to apply the correction matrix
        :type lo_frequency: int
        :param values:

            tuple is of the form (v00, v01, v10, v11) where
            the matrix is
            | v00 v01 |
            | v10 v11 |

        :type values: tuple

        .. note::

            Currently, the OPX does not support multiple mixer calibration entries.
            This function will accept IF & LO frequencies written in the config file,
            and will update the correction matrix for all of the elements with the given
            mixer/frequencies combination when the program started.

            It’s not recommended to use this method while a job is running.
            To change the calibration values for a running job,
            use job.set_element_correction
        """
        if (type(values) is not tuple and type(values) is not list) or len(values) != 4:
            raise Exception("correction values must be a tuple of 4 items")

        values = [_fix_object_data_type(x) for x in values]

        request = self._init_qm_request()

        request.setCorrection.mixer.mixer = mixer
        request.setCorrection.mixer.intermediateFrequency = abs(intermediate_frequency)
        request.setCorrection.mixer.frequencyNegative = intermediate_frequency < 0
        request.setCorrection.mixer.loFrequency = lo_frequency

        request.setCorrection.correction.v00 = values[0]
        request.setCorrection.correction.v01 = values[1]
        request.setCorrection.correction.v10 = values[2]
        request.setCorrection.correction.v11 = values[3]
        response = self._frontend.PerformQmRequest(request)
        self._handle_qm_api_response(response)

    @deprecated("1.0.0", "1.1.0", details="use set_mixer_correction(..) instead")
    def set_correction(self, qe, values):
        """
        **DEPRECATED** This method is deprecated. Using this method will update the correction for ALL elements that use the same mixer config
        as the supplied element. Use set_mixer_correction(..) instead.

        Sets the correction matrix for correcting gain and phase imbalances
        of an IQ mixer associated with a element.

        :param qe: the name of the element to update the correction for
        :type qe: str
        :param values:

            tuple is of the form (v00, v01, v10, v11) where
            the matrix is
            | v00 v01 |
            | v10 v11 |

        :type values: tuple
        :type values: tuple
        """
        if type(qe) is not str:
            raise Exception("qe must be a string")
        if (type(values) is not tuple and type(values) is not list) or len(values) != 4:
            raise Exception("correction values must be a tuple of 4 items")

        values = [_fix_object_data_type(x) for x in values]

        request = self._init_qm_request()
        request.setCorrection.qe = qe
        # request.setCorrection.correction
        request.setCorrection.correction.v00 = values[0]
        request.setCorrection.correction.v01 = values[1]
        request.setCorrection.correction.v10 = values[2]
        request.setCorrection.correction.v11 = values[3]
        response = self._frontend.PerformQmRequest(request)
        self._handle_qm_api_response(response)

    @deprecated("1.0.0", "1.1.0", details="use set_intermediate_frequency(..) instead")
    def set_frequency(self, qe, freq):
        """
        **DEPRECATED** This method is deprecated. Use set_intermediate_frequency(..) instead

         Sets the frequency of an element, at the output of the mixer, taking LO frequency into account.

        :param qe: the name of the element to update the correction for
        :param freq: the frequency to set to the given element
        :type qe: str
        :type freq: float
        """
        if type(qe) is not str:
            raise Exception("qe must be a string")
        if not isinstance(freq, (numpy.floating, float)):
            raise Exception("freq must be a float")

        config = self.get_config()
        if qe not in config["elements"]:
            raise Exception("qe does not exist")

        element = config["elements"][qe]

        if "singleInput" in element:
            self.set_intermediate_frequency(qe, freq)
        else:
            intermediate_frequency = freq - element["mixInputs"]["lo_frequency"]
            self.set_intermediate_frequency(qe, intermediate_frequency)

    def set_intermediate_frequency(self, element, freq):
        """
        Sets the intermediate frequency of the element

        :param element: the name of the element whose intermediate frequency will be updated
        :type element: str
        :param freq: the intermediate frequency to set to the given element
        :type freq: float
        """

        logger.debug(
            "Setting element '%s' intermediate frequency to '%s'", element, freq
        )
        if type(element) is not str:
            raise TypeError("element must be a string")
        if not isinstance(freq, (numpy.floating, float)):
            raise TypeError("freq must be a float")

        freq = _fix_object_data_type(freq)

        request = self._init_qm_request()
        request.setFrequency.qe = element
        request.setFrequency.value = freq
        response = self._frontend.PerformQmRequest(request)
        self._handle_qm_api_response(response)

    @deprecated(
        "1.0.0", "1.1.0", details="use get_output_dc_offset_by_element(..) instead"
    )
    def get_dc_offset_by_qe(self, qe, input):
        """
        **DEPRECATED** This method is deprecated. Use get_output_dc_offset_by_element(..) instead

        Get the current DC offset of the OPX analog output channel associated with a element.

        :param qe: the name of the element to get the correction for
        :param input: the input name as appears in the element's config
        :return: the offset, in normalized output units
        """
        self.get_output_dc_offset_by_element(qe, input)

    def get_output_dc_offset_by_element(self, element, input):
        """
        Get the current DC offset of the OPX analog output channel associated with a element.

        :param element: the name of the element to get the correction for
        :param input:
            the port name as appears in the element config. Options:

            `'single'`
                for an element with a single input

            `'I'` or `'Q'`
                for an element with mixer inputs
        :return: the offset, in normalized output units
        """
        config = self.get_config()

        if element in config["elements"]:
            element_obj = config["elements"][element]
        else:
            raise InvalidConfigError(f"Element {element} not found")

        if "singleInput" in element_obj:
            port = element_obj["singleInput"]["port"]
        elif "mixInputs" in element_obj:
            port = element_obj["mixInputs"][input]
        else:
            raise InvalidConfigError(f"Port {input}, not found")

        if len(port) == 2:
            controller, analog_output = port
        else:
            raise InvalidConfigError(
                "Port format does not recognized. (Use port[0] for the controller and port[1] for the analog output)"
            )

        if controller in config["controllers"]:
            controller = config["controllers"][port[0]]
        else:
            raise InvalidConfigError("Controller does not exist")

        if analog_output in controller["analog_outputs"]:
            return controller["analog_outputs"][port[1]]["offset"]
        else:
            raise InvalidConfigError(f"Controller {controller} does not exist")

    @deprecated(
        "1.0.0", "1.1.0", details="use set_output_dc_offset_by_element(..) instead"
    )
    def set_dc_offset_by_qe(self, qe, input, offset):
        """
        ***DEPRECATED***  "This method is deprecated. Use set_output_dc_offset_by_element(..) instead." *****
        set the current DC offset of the OPX analog output channel associated with a element.

        :param qe: the name of the element to update the correction for
        :type qe: str
        :param input:
            the input name as appears in the element config. Options:

            `'single'`
                for an element with single input

            `'I'` or `'Q'`
                for an element with mixer inputs

        :type input: str
        :param offset: the dc value to set to, in normalized output units. Ranges from -0.5 to 0.5 - 2^-16 in steps of 2^-16.
        :type offset: float

        .. note::

            if the sum of the DC offset and the largest waveform data-point exceed the normalized unit range specified
            above, DAC output overflow will occur and the output will be corrupted.
        """
        return self.set_output_dc_offset_by_element(qe, input, offset)

    def set_output_dc_offset_by_element(self, element, input, offset):
        """
        Set the current DC offset of the OPX analog output channel associated with a element.

        :param element: the name of the element to update the correction for
        :type element: str
        :param input:
            the input name as appears in the element config. Options:

            `'single'`
                for an element with a single input

            `'I'` or `'Q'` or a tuple ('I', 'Q')
                for an element with mixer inputs

        :type input: Union[str, Tuple[str,str], List[str]]
        :param offset: The dc value to set to, in normalized output units. Ranges from -0.5 to 0.5 - 2^-16 in steps of 2^-16.
        :type offset: Union[float, Tuple[float,float], List[float]]

        Examples::

            >>> qm.set_output_dc_offset_by_element('flux', 'single', 0.1)
            >>> qm.set_output_dc_offset_by_element('qubit', 'I', -0.01)
            >>> qm.set_output_dc_offset_by_element('qubit', ('I', 'Q'), (-0.01, 0.05))

        .. note::

            If the sum of the DC offset and the largest waveform data-point exceed the normalized unit range specified
            above, DAC output overflow will occur and the output will be corrupted.
        """
        logger.debug(
            "Setting DC offset of input '%s' on element '%s' to '%s'",
            input,
            element,
            offset,
        )
        if type(element) is not str:
            raise TypeError("element must be a string")

        if isinstance(input, (tuple, list)):
            if not isinstance(offset, (tuple, list)) or not len(input) == len(offset):
                raise TypeError("input and offset are not of the same length")
            for i, o in zip(input, offset):
                self.set_output_dc_offset_by_element(element, i, o)
            return

        if type(input) is not str:
            raise TypeError("input must be a string or a tuple of strings")
        if offset == 0:
            offset = float(offset)
        if not isinstance(offset, (numpy.floating, float)):
            raise TypeError("offset must be a float or a tuple of floats")

        offset = _fix_object_data_type(offset)

        request = self._init_qm_request()
        request.setOutputDcOffset.qe.qe = element
        request.setOutputDcOffset.qe.port = input
        request.setOutputDcOffset.I = offset
        request.setOutputDcOffset.Q = offset
        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def set_output_filter_by_element(
        self,
        element: str,
        input: str,
        feedforward: Union[List, numpy.ndarray, None],
        feedback: Union[List, numpy.ndarray, None],
    ):
        """
        Sets the intermediate frequency of the element

        :param element: the name of the element whose ports filters will be updated
        :param input:
            the input name as appears in the element config. Options:

            `'single'`
                for an element with single input

            `'I'` or `'Q'`
                for an element with mixer inputs

        :param feedforward: the values for the feedforward filter
        :param feedback: the values for the feedback filter
        """
        logger.debug(
            f"Setting output filter of port '{input}' on element '{element}' "
            + f"to (feedforward: {feedforward}, feedback: {feedback})"
        )
        if type(element) is not str:
            raise TypeError("element must be a string")
        if type(input) is not str:
            raise TypeError("port must be a string")
        if feedforward is not None and not isinstance(
            feedforward, (numpy.ndarray, List)
        ):
            raise TypeError("feedforward must be a list or None")

        if feedback is not None and not isinstance(feedback, (numpy.ndarray, List)):
            raise TypeError("feedback must be a list or None")

        request = self._init_qm_request()
        request.setOutputFilterTaps.qe.qe = element
        request.setOutputFilterTaps.qe.port = input
        request.setOutputFilterTaps.filter.SetInParent()
        request.setOutputFilterTaps.filter.feedforward.extend(feedforward)
        request.setOutputFilterTaps.filter.feedback.extend(feedback)
        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def set_input_dc_offset_by_element(self, element, output, offset):
        """
        set the current DC offset of the OPX analog input channel associated with a element.

        :param element: the name of the element to update the correction for
        :type element: str
        :param output:
            the output key name as appears in the element config under 'outputs'.
        :type output: str
        :param offset: the dc value to set to, in normalized input units. Ranges from -0.5 to 0.5 - 2^-16 in steps of 2^-16.
        :type offset: float

        .. note::
            If the sum of the DC offset and the largest waveform data-point exceed the normalized unit range specified
            above, DAC output overflow will occur and the output will be corrupted.
        """
        logger.debug(
            "Setting DC offset of output '%s' on element '%s' to '%s'",
            output,
            element,
            offset,
        )
        if type(element) is not str:
            raise TypeError("element must be a string")
        if type(output) is not str:
            raise TypeError("output must be a string")
        if not isinstance(offset, (numpy.floating, float)):
            raise TypeError("offset must be a float")

        offset = _fix_object_data_type(offset)

        request = self._init_qm_request()
        request.setInputDcOffset.qe.qe = element
        request.setInputDcOffset.qe.port = output
        request.setInputDcOffset.offset = offset
        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def get_input_dc_offset_by_element(self, element, output):
        """
        Get the current DC offset of the OPX analog input channel associated with a element.

        :param element: the name of the element to get the correction for
        :param output:
            the output key name as appears in the element config under 'outputs'.
        :return: the offset, in normalized output units
        """
        config = self.get_config()

        if element in config["elements"]:
            element_obj = config["elements"][element]
        else:
            raise Exception("Element not found")

        if "outputs" in element_obj:
            outputs = element_obj["outputs"]
        else:
            raise Exception("Element has not outputs")

        if output in outputs:
            port = outputs[output]
        else:
            raise Exception("Output does not exist")

        if port[0] in config["controllers"]:
            controller = config["controllers"][port[0]]
        else:
            raise Exception("Controller does not exist")

        if "analog_inputs" not in controller:
            raise Exception("Controller has not analog inputs defined")

        if port[1] in controller["analog_inputs"]:
            return controller["analog_inputs"][port[1]]["offset"]
        else:
            raise Exception("Port not found")

    def get_digital_delay(self, element, digital_input):
        """
        Gets the delay of the digital input of the element

        :param element: the name of the element to get the delay for
        :param digital_input: the digital input name as appears in the element's config
        :return: the delay
        """
        element_object = None
        config = self.get_config()
        for (key, value) in config["elements"].items():
            if key == element:
                element_object = value
                break

        if element_object is None:
            raise Exception("element not found")

        for (key, value) in element_object["digitalInputs"].items():
            if key == digital_input:
                return value["delay"]

        raise Exception("digital input not found")

    def set_digital_delay(self, element, digital_input, delay):
        """
        Sets the delay of the digital input of the element

        :param element: the name of the element to update delay for
        :type element: str
        :param digital_input: the digital input name as appears in the element's config
        :type digital_input: str
        :param delay: the delay value to set to, in nsec. Range: 0 to 255 - 2 * buffer, in steps of 1
        :type delay: int
        """
        logger.debug(
            "Setting delay of digital port '%s' on element '%s' to '%s'",
            digital_input,
            element,
            delay,
        )
        if type(element) is not str:
            raise Exception("element must be a string")
        if type(digital_input) is not str:
            raise Exception("port must be a string")
        if type(delay) is not int:
            raise Exception("delay must be an int")

        request = self._init_qm_request()
        request.setDigitalRoute.delay.qe = element
        request.setDigitalRoute.delay.port = digital_input
        request.setDigitalRoute.value = delay

        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def get_digital_buffer(self, element, digital_input):
        """
        Gets the buffer for digital input of the element

        :param element: the name of the element to get the buffer for
        :type element: str
        :param digital_input: the digital input name as appears in the element's config
        :type digital_input: str
        :return: the buffer
        """
        element_object = None
        config = self.get_config()
        for (key, value) in config["elements"].items():
            if key == element:
                element_object = value
                break

        if element_object is None:
            raise Exception("element not found")

        for (key, value) in element_object["digitalInputs"].items():
            if key == digital_input:
                return value["buffer"]

        raise Exception("digital input not found")

    def set_digital_buffer(self, element, digital_input, buffer):
        """
        Sets the buffer for digital input of the element

        :param element: the name of the element to update buffer for
        :type element: str
        :param digital_input: the digital input name as appears in the element's config
        :type digital_input: str
        :param buffer: the buffer value to set to, in nsec. Range: 0 to (255 - delay) / 2, in steps of 1
        :type buffer: int
        """
        logger.debug(
            "Setting buffer of digital port '%s' on element '%s' to '%s'",
            digital_input,
            element,
            buffer,
        )
        if type(element) is not str:
            raise Exception("element must be a string")
        if type(digital_input) is not str:
            raise Exception("port must be a string")
        if type(buffer) is not int:
            raise Exception("buffer must be an int")

        request = self._init_qm_request()
        request.setDigitalRoute.buffer.qe = element
        request.setDigitalRoute.buffer.port = digital_input
        request.setDigitalRoute.value = buffer

        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def get_time_of_flight(self, element):
        """
        Gets the *time of flight*, associated with a measurement element.

        This is the amount of time between the beginning of a measurement pulse applied to element
        and the time that the data is available to the controller for demodulation or streaming.

        :param element: the name of the element to get time of flight for
        :type element: str
        :return: the time of flight, in nsec
        """
        element_object = None
        config = self.get_config()
        for (key, value) in config["elements"].items():
            if key == element:
                if "time_of_flight" in value:
                    return value["time_of_flight"]
                else:
                    return 0

        if element_object is None:
            raise Exception("element not found")

    def get_smearing(self, element):
        """
        Gets the *smearing* associated with a measurement element.

        This is a broadening of the raw results acquisition window, to account for dispersive broadening
        in the measurement elements (readout resonators etc.) The acquisition window will be broadened
        by this amount on both sides.

        :param element: the name of the element to get smearing for
        :type element: str
        :return: the smearing, in nesc.
        """
        element_object = None
        config = self.get_config()
        for (key, value) in config["elements"].items():
            if key == element:
                if "smearing" in value:
                    return value["smearing"]
                else:
                    return 0

        if element_object is None:
            raise Exception("element not found")

    def set_io1_value(self, value_1: Union[float, bool, int]):
        """
        Sets the value of ``IO1``.

        This can be used later inside a QUA program as a QUA variable ``IO1`` without declaration.
        The type of QUA variable is inferred from the python type passed to ``value_1``, according to the following rule:

        int -> int
        float -> fixed
        bool -> bool

        :param value_1: the value to be placed in ``IO1``
        :type value_1: Union[float,bool,int]
        """
        self.set_io_values(value_1, None)

    def set_io2_value(self, value_2: Union[float, bool, int]):
        """
        Sets the value of ``IO1``.

        This can be used later inside a QUA program as a QUA variable ``IO2`` without declaration.
        The type of QUA variable is inferred from the python type passed to ``value_2``, according to the following rule:

        int -> int
        float -> fixed
        bool -> bool

        :param value_2: the value to be placed in ``IO1``
        :type value_2: Union[float, bool, int]
        """
        self.set_io_values(None, value_2)

    def set_io_values(
        self,
        value_1: Optional[Union[float, bool, int]],
        value_2: Optional[Union[float, bool, int]],
    ):
        """
        Sets the values of ``IO1`` and ``IO2``

        This can be used later inside a QUA program as a QUA variable ``IO1``, ``IO2`` without declaration.
        The type of QUA variable is inferred from the python type passed to ``value_1``, ``value_2``,
        according to the following rule:

        int -> int
        float -> fixed
        bool -> bool

        :param value_1: the value to be placed in ``IO1``
        :param value_2: the value to be placed in ``IO2``
        :type value_1: Optional[Union[float, bool, int]]
        :type value_2: Optional[Union[float, bool, int]]
        """

        if value_1 is None and value_2 is None:
            return

        if value_1 is not None:
            logger.debug("Setting value '%s' to IO1", value_1)
        if value_2 is not None:
            logger.debug("Setting value '%s' to IO2", value_2)

        request = self._init_qm_request()
        request.setIOValues.all = True

        value_1 = _fix_object_data_type(value_1)
        value_2 = _fix_object_data_type(value_2)

        if type(value_1) is int:
            request.setIOValues.ioValueSetData.add(io_number=1, intValue=value_1)
        elif type(value_1) is float:
            request.setIOValues.ioValueSetData.add(io_number=1, doubleValue=value_1)
        elif type(value_1) is bool:
            request.setIOValues.ioValueSetData.add(io_number=1, booleanValue=value_1)
        elif value_1 is None:
            pass
        else:
            raise Exception(
                "Invalid value_1 type (The possible types are: int, bool or float)"
            )

        if type(value_2) is int:
            request.setIOValues.ioValueSetData.add(io_number=2, intValue=value_2)
        elif type(value_2) is float:
            request.setIOValues.ioValueSetData.add(io_number=2, doubleValue=value_2)
        elif type(value_2) is bool:
            request.setIOValues.ioValueSetData.add(io_number=2, booleanValue=value_2)
        elif value_2 is None:
            pass
        else:
            raise Exception(
                "Invalid value_2 type (The possible types are: int, bool or float)"
            )

        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def _init_qm_request(self):
        request = HighQmApiRequest()
        request.quantumMachineId = self._id
        return request

    @staticmethod
    def _handle_qm_api_response(response: HighQmApiResponse):
        if not response.ok:
            msg = "\n\t" + "\n\t".join([it.message for it in response.errors])
            logger.error("Failed: %s", msg)
            raise RuntimeError("\n".join([it.message for it in response.errors]))

    def get_io1_value(self):
        """
        Gets the data stored in ``IO1``

        No inference is made on type.

        :return:
            A dictionary with data stored in ``IO1``.
            (Data is in all three format: ``int``, ``float`` and ``bool``)
        """
        return self.get_io_values()[0]

    def get_io2_value(self):
        """
        Gets the data stored in ``IO2``

        No inference is made on type.

        :return:
            A dictionary with data from the second IO register.
            (Data is in all three format: ``int``, ``float`` and ``bool``)
        """
        return self.get_io_values()[1]

    def get_io_values(self):
        """
        Gets the data stored in both ``IO1`` and ``IO2``

        No inference is made on type.

        :return:
            A list that contains dictionaries with data from the IO registers.
            (Data is in all three format: ``int``, ``float`` and ``bool``)
        """
        request = QmDataRequest()
        request.io_value_Request.add(io_number=1, quantumMachineId=self._id)
        request.io_value_Request.add(io_number=2, quantumMachineId=self._id)
        response = self._frontend.RequestData(request)

        if not response.success:
            error_str = ""
            for err in response.errors:
                error_str = error_str + err.message + "\n"
            exception = Exception(error_str)
            exception.errors = [(it.code, it.message) for it in response.errors]
            raise exception

        resp1 = response.io_value_response[0]
        resp2 = response.io_value_response[1]

        return [
            {
                "io_number": 1,
                "int_value": resp1.values.int_value,
                "fixed_value": resp1.values.double_value,
                "boolean_value": resp1.values.boolean_value,
            },
            {
                "io_number": 2,
                "int_value": resp2.values.int_value,
                "fixed_value": resp2.values.double_value,
                "boolean_value": resp2.values.boolean_value,
            },
        ]

    def peek(self, address):
        raise NotImplementedError()
        # if you must use this, code below will work for a specific controller
        # request = PeekRequest()
        # request.controllerId = list(self._config["controllers"].keys())[0]
        # request.address = address

        # return self._frontend.Peek(request)

    def poke(self, address, value):

        request = PokeRequest()
        request.address = address
        request.value = value

        return self._frontend.Poke(request)

    def get_config(self):
        """
        Gets the current config of the qm

        :return: A dictionary with the qm's config
        """
        configs = self._manager._get_qm_config(self._id)
        self._pb_config = configs["pb_config"]
        self._config = configs["config"]
        return self._config

    def save_config_to_file(self, filename):
        """
        Saves the qm current config to a file

        :param: filename: The name of the file where the config will be saved
        """
        json_str = json.dumps(self.get_config())
        with open(filename, "w") as writer:
            writer.write(json_str)

    def get_running_job(self) -> Optional[QmJob]:
        """
        Gets the currently running job. Returns None if there isn't one.
        """
        request = GetRunningJobRequest()
        request.machineID = self._id

        response = self._frontend.GetRunningJob(request)
        if response.jobId == "":
            return None
        else:
            try:
                return QmPendingJob(
                    response.jobId, self, self._manager
                ).wait_for_execution(timeout=10)
            except JobCancelledError:
                # In case that the job has finished between the GetRunningJon and the
                # wait for execution
                return None

    def set_digital_input_threshold(
        self, port: Tuple[str, int], threshold: float
    ) -> float:
        request = self._init_qm_request()
        request.setDigitalInputThreshold.digitalPort.controllerName = port[0]
        request.setDigitalInputThreshold.digitalPort.portNumber = port[1]
        request.setDigitalInputThreshold.threshold = threshold
        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def _get_digital_input_port(self, port: Tuple[str, int]):
        config: Dict = self.get_config()
        component = "Controller"
        target_controller_name, target_port = port
        controller = config["controllers"].get(target_controller_name, None)
        if controller is not None:
            controller_digital_inputs = controller.get("digital_inputs", None)
            if controller_digital_inputs is not None:
                if target_port in controller_digital_inputs:
                    return controller_digital_inputs[target_port]
                else:
                    component = "Digital input port"
            else:
                component = "Digital input for conroller"

        raise InvalidConfigError(f"{component} not found")

    def get_digital_input_threshold(self, port: Tuple[str, int]) -> float:
        return self._get_digital_input_port(port)["threshold"]

    def set_digital_input_deadtime(self, port: Tuple[str, int], deadtime: int) -> int:
        request = self._init_qm_request()
        request.setDigitalInputDeadtime.digitalPort.controllerName = port[0]
        request.setDigitalInputDeadtime.digitalPort.portNumber = port[1]
        request.setDigitalInputDeadtime.deadtime = deadtime
        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def get_digital_input_deadtime(self, port: Tuple[str, int]) -> int:
        return self._get_digital_input_port(port)["deadtime"]

    def set_digital_input_polarity(self, port: Tuple[str, int], polarity: str) -> str:
        request = self._init_qm_request()
        request.setDigitalInputPolarity.digitalPort.controllerName = port[0]
        request.setDigitalInputPolarity.digitalPort.portNumber = port[1]
        request.setDigitalInputPolarity.polarity = RISING
        if polarity == "RISING":
            request.setDigitalInputPolarity.polarity = RISING
        elif polarity == "FALLING":
            request.setDigitalInputPolarity.polarity = FALLING
        else:
            raise InvalidDigitalInputPolarityError(
                f"Invalid value for polarity {polarity}. Valid values are: 'RISING' "
                f"or 'FALLING'"
            )

        response = self._frontend.PerformQmRequest(request)
        return self._handle_qm_api_response(response)

    def get_digital_input_polarity(self, port: Tuple[str, int]) -> str:
        return self._get_digital_input_port(port)["polarity"]
