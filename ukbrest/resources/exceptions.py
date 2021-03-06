from ukbrest.config import logger


class UkbRestException(Exception):
    def __init__(self, message, subtype, output=None):
        super(UkbRestException, self).__init__(message)

        self.message = message
        self.status_code = 400
        self.subtype = subtype

        if output is not None:
            self.output = output

        logger.error(self.message.strip())


class UkbRestValidationError(UkbRestException):
    def __init__(self, message):
        super(UkbRestValidationError, self).__init__(message, 'VALIDATION_ERROR')


class UkbRestProgramExecutionError(UkbRestException):
    def __init__(self, message, output=None):
        super(UkbRestProgramExecutionError, self).__init__(message, 'EXECUTION_ERROR', output)


class UkbRestSQLExecutionError(UkbRestException):
    def __init__(self, message):
        super(UkbRestSQLExecutionError, self).__init__(message, 'SQL_EXECUTION_ERROR')
