"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import fire
from client import ThothRESTClient


class ThothCLI(object):
    """A simple CLI for Thoth REST."""

    def formats(self, return_json=False):
        """
        Full list of metadata formats that can be output by Thoth
        @param return_json: whether to return JSON or an object (default)
        """
        client = ThothRESTClient()
        print(client.formats(return_json))


if __name__ == '__main__':
    fire.Fire(ThothCLI)
