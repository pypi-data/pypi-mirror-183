import logging

from qm.QuantumMachine import QuantumMachine  # noqa
from qm.program import _Program  # noqa
from qm.program import _ResultAnalysis  # noqa
from qm.program._qua_config_schema import validate_config  # noqa
from qm.user_config import UserConfig  # noqa
from qm.generate_qua_script import generate_qua_script  # noqa
from qm.simulate import *  # noqa
from qm._pretty_errors import activate_verbose_errors, disable_colored_errors  # noqa
from qm.version import __version__  # noqa
from qm.logging_utils import config_loggers


config = UserConfig.create_from_file()
config_loggers(config)


logger = logging.getLogger(__name__)
logger.info(f"Starting session: {config.SESSION_ID}")
