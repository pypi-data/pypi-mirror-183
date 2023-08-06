# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Basic exception classes.
"""


class ParzzleyError(Exception):

    def __call__(self, *args):
        return self.__class__(*(self.args + args))


class InvalidCommandLineError(ParzzleyError):
    pass


class ConfigurationError(ParzzleyError):
    pass


class ReadInvalidConfigurationError(ConfigurationError):
    pass


class ParzzleyEngineExecutionError(ParzzleyError):
    pass


class PreparationEnabledBeforeEnablingExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Preparation not disabled before enabling")


class PreparationDisabledAfterEnablingExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Preparation disabled after enabling")


class PreparationEnabledAfterDisablingExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Preparation not disabled after disabling")


class ErrorEnablingPreparationExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Unable to enable preparation")


class ErrorDisablingPreparationExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Unable to disable preparation")


class ErrorGettingPreparationStateExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Unable to get preparation state")


class ErrorInitializingExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Unable to initialize the synchronization task")


class ErrorExecutingExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Unable to execute the synchronization task")


class EnablingImpossibleExecutionError(ParzzleyEngineExecutionError):

    def __init__(self):
        super().__init__("Impossible to enable the preparation")
