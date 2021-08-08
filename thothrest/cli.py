"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""


def _client():
    from .client import ThothRESTClient
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


def work(identifier, work_identifier):
    """
    Find the details of a platform supported by Thoth's outputs
    @param identifier: the specification ID
    @param work_identifier: the work ID
    """
    print(_client().work(identifier, work_identifier))


def works(identifier, publisher):
    """
    Obtain a metadata record that adheres to a particular specification for all of a given publisher's works
    @param identifier: the specification ID
    @param publisher: the publisher ID
    """
    print(_client().works(identifier, publisher))


if __name__ == '__main__':
    import fire

    fire.Fire()
