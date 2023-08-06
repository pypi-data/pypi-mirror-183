class ErrorToLog(Exception):

    def __init__(self, message: str, *stacktrace: str):
        self.__stacktrace = list(stacktrace)
        self.__message = message
        super().__init__(message)

    def __str__(self) -> str:
        return 'ERROR:' + ':'.join(self.__stacktrace[::-1]) + ':' + self.__message
    
    def __repr__(self) -> str:
        return self.__str__()

    def append(self, trace_level: str):
        self.__stacktrace.append(trace_level)
        return self
