from qm.pb.inc_qua_pb2 import QuaProgram

from qm._loc import _get_loc


class StatementsCollection(object):
    def __init__(self, body):
        super(StatementsCollection, self).__init__()
        self._body = body

    def play(
        self,
        pulse,
        element,
        duration=None,
        condition=None,
        target="",
        chirp=None,
        truncate=None,
        timestamp_label=None,
    ):
        """
        Play a pulse to a element as per the OPX config
        :param pulse: A tuple (pulse, amp). pulse is string of pulse name, amp is a 4 matrix
        :param element:
        :param duration:
        :param condition:
        :param target:
        :return:
        """

        amp = None
        if type(pulse) is tuple:
            pulse, amp = pulse

        loc = _get_loc()
        statement = self._body.statements.add()
        statement.play.SetInParent()
        statement.play.loc = loc
        if isinstance(pulse, QuaProgram.RampPulse):
            statement.play.rampPulse.SetInParent()
            statement.play.rampPulse.CopyFrom(pulse)
        else:
            statement.play.namedPulse.SetInParent()
            statement.play.namedPulse.name = pulse
            statement.play.pulse.name = pulse
        statement.play.qe.name = element
        statement.play.targetInput = target
        if duration is not None:
            statement.play.duration.CopyFrom(duration)
        if condition is not None:
            statement.play.condition.CopyFrom(condition)
        if chirp is not None:
            statement.play.chirp.CopyFrom(chirp)
            statement.play.chirp.loc = loc
        if amp is not None:
            statement.play.amp.SetInParent()
            statement.play.amp.loc = loc
            statement.play.amp.v0.CopyFrom(amp[0])
            for i in range(1, 4, 1):
                if amp[i] is not None:
                    getattr(statement.play.amp, "v" + str(i)).CopyFrom(amp[i])
        if truncate is not None:
            statement.play.truncate.CopyFrom(truncate)
        if timestamp_label is not None:
            statement.play.timestampLabel = timestamp_label

    def pause(self, *elements):
        """
        Pause the execution of the given elements
        :param elements:
        :return:
        """
        statement = self._body.statements.add()
        statement.pause.SetInParent()
        statement.pause.loc = _get_loc()
        for element in elements:
            element_ref = statement.pause.qe.add()
            element_ref.name = element

    def update_frequency(self, element, new_frequency, units, keep_phase):
        """
        Updates the frequency of a given element
        :param element: The element to set the frequency to
        :param new_frequency: The new frequency value to set
        :return:
        """
        statement = self._body.statements.add()
        statement.updateFrequency.SetInParent()
        statement.updateFrequency.loc = _get_loc()
        statement.updateFrequency.qe.name = element
        if units == "Hz":
            statement.updateFrequency.units = QuaProgram.UpdateFrequencyStatement.Hz
        elif units == "mHz":
            statement.updateFrequency.units = QuaProgram.UpdateFrequencyStatement.mHz
        elif units == "uHz":
            statement.updateFrequency.units = QuaProgram.UpdateFrequencyStatement.uHz
        elif units == "nHz":
            statement.updateFrequency.units = QuaProgram.UpdateFrequencyStatement.nHz
        elif units == "pHz":
            statement.updateFrequency.units = QuaProgram.UpdateFrequencyStatement.pHz
        else:
            raise RuntimeError(f'unknown units "{units}"')
        statement.updateFrequency.keepPhase = keep_phase
        statement.updateFrequency.value.CopyFrom(new_frequency)

    def update_correction(self, element, c00, c01, c10, c11):
        """
        Updates the correction of a given element
        :param element: The element to set the correction to
        :param c00: The top left matrix element
        :param c01: The top right matrix element
        :param c10: The bottom left matrix element
        :param c11: The bottom right matrix element
        """
        statement = self._body.statements.add()
        statement.updateCorrection.SetInParent()
        statement.updateCorrection.qe.name = element
        statement.updateCorrection.loc = _get_loc()
        statement.updateCorrection.correction.SetInParent()
        statement.updateCorrection.correction.c0.CopyFrom(c00)
        statement.updateCorrection.correction.c1.CopyFrom(c01)
        statement.updateCorrection.correction.c2.CopyFrom(c10)
        statement.updateCorrection.correction.c3.CopyFrom(c11)

    def set_dc_offset(self, element, element_input, offset):
        """
        Update the DC offset of an element's input
        :param element: The element to update its DC offset
        :param element_input: desired input of the element, can be 'single' for a 'singleInput' element
            or 'I' or 'Q' for a 'mixInputs' element
        :param offset: Desired dc offset for single
        """
        statement = self._body.statements.add()
        statement.setDcOffset.SetInParent()
        statement.setDcOffset.loc = _get_loc()
        statement.setDcOffset.qe.name = element
        statement.setDcOffset.qeInputReference = element_input
        statement.setDcOffset.offset.CopyFrom(offset)

    def advance_input_stream(self, input_stream):
        """
        advance an input stream pointer to be sent to the QUA program
        :param input_stream: The input stream to advance
        """
        statement = self._body.statements.add()
        statement.advanceInputStream.SetInParent()
        statement.advanceInputStream.loc = _get_loc()
        if isinstance(input_stream, QuaProgram.ArrayVarRefExpression):
            statement.advanceInputStream.streamArray.CopyFrom(input_stream)
        elif (
            isinstance(input_stream, QuaProgram.AnyScalarExpression)
            and input_stream.WhichOneof("expression_oneof") == "variable"
        ):
            statement.advanceInputStream.streamVariable.CopyFrom(input_stream.variable)
        else:
            raise RuntimeError("unsupported type for advance input stream")

    def align(self, *elements):
        """
        Align the given elements
        :param elements:
        :return:
        """
        statement = self._body.statements.add()
        statement.align.SetInParent()
        statement.align.loc = _get_loc()
        for element in elements:
            element_ref = statement.align.qe.add()
            element_ref.name = element

    def reset_phase(self, element):
        """
        TODO: document
        :param element:
        :return:
        """
        statement = self._body.statements.add()
        statement.resetPhase.SetInParent()
        statement.resetPhase.qe.SetInParent()
        statement.resetPhase.qe.name = element
        statement.resetPhase.loc = _get_loc()

    def wait(self, duration, *elements):
        """
        Waits for the given duration on all provided elements
        :param duration:
        :param elements:
        :return:
        """
        statement = self._body.statements.add()
        statement.wait.SetInParent()
        statement.wait.loc = _get_loc()
        statement.wait.time.CopyFrom(duration)
        for element in elements:
            element_ref = statement.wait.qe.add()
            element_ref.name = element

    def wait_for_trigger(
        self, pulse_to_play, trigger_element, time_tag_target, *elements
    ):
        statement = self._body.statements.add()
        statement.waitForTrigger.SetInParent()
        statement.waitForTrigger.loc = _get_loc()
        if pulse_to_play is not None:
            statement.waitForTrigger.pulseToPlay.name = pulse_to_play
        if trigger_element is not None:
            statement.waitForTrigger.elementOutput.SetInParent()
            if type(trigger_element) == tuple:
                statement.waitForTrigger.elementOutput.element = trigger_element[0]
                statement.waitForTrigger.elementOutput.output = trigger_element[1]
            else:
                statement.waitForTrigger.elementOutput.element = trigger_element
        else:
            statement.waitForTrigger.globalTrigger.SetInParent()
        if time_tag_target is not None:
            statement.waitForTrigger.timeTagTarget.CopyFrom(time_tag_target)
        for element in elements:
            element_ref = statement.waitForTrigger.qe.add()
            element_ref.name = element

    def save(self, source, result):
        statement = self._body.statements.add()
        statement.save.SetInParent()
        statement.save.loc = _get_loc()
        statement.save.source.CopyFrom(source)
        statement.save.tag = result._get_var_name()

    def z_rotation(self, angle, *elements):
        for element in elements:
            statement = self._body.statements.add()
            statement.zRotation.SetInParent()
            statement.zRotation.loc = _get_loc()
            statement.zRotation.value.CopyFrom(angle)
            statement.zRotation.qe.name = element

    def reset_frame(self, *elements):
        for element in elements:
            statement = self._body.statements.add()
            statement.resetFrame.SetInParent()
            statement.resetFrame.loc = _get_loc()
            statement.resetFrame.qe.name = element

    def ramp_to_zero(self, element, duration):
        statement = self._body.statements.add()
        statement.rampToZero.SetInParent()
        statement.rampToZero.qe.SetInParent()
        statement.rampToZero.qe.name = element
        if duration is not None:
            statement.rampToZero.duration.SetInParent()
            statement.rampToZero.duration.value = duration

    def measure(self, pulse, element, stream=None, *processes, timestamp_label=None):
        """
        Measure an element using the given pulse, process the result with the integration weights and
        store the results to the provided variables
        :param pulse:
        :param element:
        :param stream:
        :type stream: _ResultSource
        :param processes: an iterable of analog processes
        :param timestamp_label
        :return:
        """
        amp = None
        if type(pulse) is tuple:
            pulse, amp = pulse

        loc = _get_loc()
        statement = self._body.statements.add()
        statement.measure.SetInParent()
        statement.measure.loc = loc
        statement.measure.pulse.name = pulse
        statement.measure.qe.name = element
        if stream is not None:
            statement.measure.streamAs = stream._get_var_name()

        for analog_process in processes:
            added_process = statement.measure.measureProcesses.add()
            added_process.CopyFrom(analog_process)

        if amp is not None:
            statement.measure.amp.SetInParent()
            statement.measure.amp.loc = loc
            statement.measure.amp.v0.CopyFrom(amp[0])
            for i in range(1, 4, 1):
                if amp[i] is not None:
                    getattr(statement.measure.amp, "v" + str(i)).CopyFrom(amp[i])

        if timestamp_label is not None:
            statement.measure.timestampLabel = timestamp_label

    def if_block(self, condition, unsafe=False):
        statement = self._body.statements.add()
        ifstatement = getattr(statement, "if")
        ifstatement.SetInParent()
        ifstatement.loc = _get_loc()
        ifstatement.condition.CopyFrom(condition)
        ifstatement.unsafe = unsafe
        ifstatement.body.SetInParent()
        return StatementsCollection(ifstatement.body)

    def for_each(self, iterators):
        statement = self._body.statements.add()
        forEach = statement.forEach
        forEach.SetInParent()
        forEach.loc = _get_loc()
        for it in iterators:
            pb_it = forEach.iterator.add()
            pb_it.variable.CopyFrom(it[0])
            pb_it.array.CopyFrom(it[1])
        forEach.body.SetInParent()
        return StatementsCollection(forEach.body)

    def get_last_statement(self):
        statements = self._body.statements
        l = len(statements)
        if l == 0:
            return None
        return statements[l - 1]

    def for_block(self):
        statement = self._body.statements.add()
        forstatement = getattr(statement, "for")
        forstatement.SetInParent()
        forstatement.loc = _get_loc()
        return forstatement

    def strict_timing_block(self):
        statement = self._body.statements.add()
        strict_timing_statement = statement.strictTiming
        strict_timing_statement.SetInParent()
        strict_timing_statement.loc = _get_loc()
        return strict_timing_statement

    def assign(self, target, expression):
        """
        Assign a value calculated by :expression into :target
        :param target: The name of the variable to assign to
        :param expression: The expression to calculate
        :return:
        """
        statement = self._body.statements.add()
        statement.assign.SetInParent()
        statement.assign.loc = _get_loc()
        statement.assign.target.CopyFrom(target)
        statement.assign.expression.CopyFrom(expression)
