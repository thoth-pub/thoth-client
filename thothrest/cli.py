"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""


def _client():
    from client import ThothRESTClient
    return ThothRESTClient()


def formats(json=False):
    """
    Full list of metadata formats that can be output by Thoth
    @param json: whether to return JSON or an object (default)
    """
    print(_client().formats(json))


def format(identifier, json=False):
    """
    Find the details of a format that can be output by Thoth
    @param identifier: the format ID to describe
    @param json: whether to return JSON or an object (default)
    """
    print(_client().format(identifier, json))


def specifications(json=False):
    """
    Full list of metadata specifications that can be output by Thoth
    @param json: whether to return JSON or an object (default)
    """
    print(_client().specifications(json))


def specification(identifier, json=False):
    """
    Find the details of a metadata specification that can be output by Thoth
    @param identifier: the format ID to describe
    @param json: whether to return JSON or an object (default)
    """
    print(_client().specification(identifier, json))


def platforms(json=False):
    """
    Full list of metadata specifications that can be output by Thoth
    @param json: whether to return JSON or an object (default)
    """
    print(_client().platforms(json))


def platform(identifier, json=False):
    """
    Find the details of a platform supported by Thoth's outputs
    @param identifier: the format ID to describe
    @param json: whether to return JSON or an object (default)
    """
    print(_client().platform(identifier, json))


def work(identifier, work):
    """
    Find the details of a platform supported by Thoth's outputs
    @param identifier: the spefication ID
    @param work: the work ID
    @param json: whether to return JSON or an object (default)
    """
    print(_client().work(identifier, work))


if __name__ == '__main__':
    import fire
    fire.Fire()
