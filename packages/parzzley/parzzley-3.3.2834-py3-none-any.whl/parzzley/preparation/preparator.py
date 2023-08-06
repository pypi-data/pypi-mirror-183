# SPDX-FileCopyrightText: © 2014 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Helper for enabling and disabling preparations.
"""

import traceback
import typing as t

import parzzley.exceptions
import parzzley.logger
import parzzley.runtime.returnvalue

if t.TYPE_CHECKING:
    import parzzley.preparation.abstractpreparation
    import parzzley.runtime.runtime


class Preparator:

    @staticmethod
    def _logandthrowexception(runtime: 'parzzley.runtime.runtime.RuntimeData', exclass: t.Type[Exception],
                              olde: t.Optional[Exception] = None) -> None:
        newe = exclass()
        dolog = (olde is None) or (not getattr(olde, "_is_logged", False))
        newe._is_logged = True
        if dolog:
            oldetext = f": {olde}" if olde else ""
            runtime.log(verb="Error", comment=str(newe) + oldetext, severity=parzzley.logger.Severity.ERROR, symbol="E")
        if olde:
            runtime.log(subject="Callstack", comment=traceback.format_exc(), severity=parzzley.logger.Severity.DEBUG,
                        symbol="E")
            raise newe from olde
        else:
            raise newe

    def __init__(self, runtime: 'parzzley.runtime.runtime.RuntimeData',
                 preparation: 'parzzley.preparation.abstractpreparation.Preparation'):
        self.runtime = runtime
        self.preparation = preparation

    def __enter__(self):
        rollback_on_exception = False
        try:
            succ = False
            self.runtime.log(verb=f"Begin preparing {self.preparation}", severity=parzzley.logger.Severity.DEBUGVERBOSE)
            try:
                if self.preparation.ensuredisabledbefore():
                    try:
                        if self.preparation.getstate(self.runtime):
                            Preparator._logandthrowexception(
                                self.runtime, parzzley.exceptions.PreparationEnabledBeforeEnablingExecutionError)
                    except Exception as e:
                        Preparator._logandthrowexception(
                            self.runtime, parzzley.exceptions.ErrorGettingPreparationStateExecutionError, e)
                rollback_on_exception = True
                presucc = False
                try:
                    self.preparation.enable(self.runtime)
                    presucc = True
                except Exception as e:
                    self.runtime.log(verb="Error", comment=f"while enabling preparation: {e}",
                                     severity=parzzley.logger.Severity.DEBUGVERBOSE, symbol="E")
                if presucc:
                    if self.preparation.ensureenabled():
                        try:
                            if not self.preparation.getstate(self.runtime):
                                Preparator._logandthrowexception(
                                    self.runtime, parzzley.exceptions.PreparationDisabledAfterEnablingExecutionError)
                        except Exception as e:
                            Preparator._logandthrowexception(
                                self.runtime, parzzley.exceptions.ErrorGettingPreparationStateExecutionError, e)
                    succ = True
                if not succ:
                    if self.preparation.ensuredisabledafter():
                        # noinspection PyBroadException
                        try:
                            self.preparation.disable(self.runtime)
                        except Exception:
                            pass
                    raise parzzley.exceptions.EnablingImpossibleExecutionError()
            except Exception as e:
                self.runtime.set_retval(parzzley.runtime.returnvalue.ReturnValue.ERROR_PREPARATION)
                if not isinstance(e, parzzley.exceptions.EnablingImpossibleExecutionError):
                    Preparator._logandthrowexception(
                        self.runtime, parzzley.exceptions.ErrorEnablingPreparationExecutionError, e)
            self.enabled = succ
        except Exception:
            if rollback_on_exception:
                self.__exit__(None, None, None)
            raise
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        succ = False
        self.runtime.log(verb=f"Begin disabling {self.preparation}", severity=parzzley.logger.Severity.DEBUGVERBOSE)
        try:
            try:
                self.preparation.disable(self.runtime)
                if self.preparation.ensuredisabledafter():
                    try:
                        if self.preparation.getstate(self.runtime):
                            Preparator._logandthrowexception(
                                self.runtime, parzzley.exceptions.PreparationEnabledAfterDisablingExecutionError)
                    except Exception as e:
                        Preparator._logandthrowexception(
                            self.runtime, parzzley.exceptions.ErrorGettingPreparationStateExecutionError, e)
                succ = True
            except Exception as e:
                Preparator._logandthrowexception(
                    self.runtime, parzzley.exceptions.ErrorDisablingPreparationExecutionError, e)
        except Exception:
            pass
        if not succ:
            self.runtime.set_retval(parzzley.runtime.returnvalue.ReturnValue.ERROR_UNPREPARATION)
            self.runtime.log(verb="Disabling preparation failed", severity=parzzley.logger.Severity.ERROR)
