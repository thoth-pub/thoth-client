"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""


class ThothRESTError(Exception):
    """Exception to report Thoth errors"""

    def __init__(self, request, response):
        message = "REST Error.\nRequest:\n{}\n\nResponse:\n{}".format(
            request, response)
        super().__init__(message)
