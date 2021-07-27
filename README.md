Python client for Thoth's GraphQL and REST APIs

[![Build Status](https://travis-ci.org/openbookpublishers/thoth-client.svg?branch=master)](https://travis-ci.org/openbookpublishers/thoth-client) [![Release](https://img.shields.io/github/release/openbookpublishers/thoth-client.svg?colorB=58839b)](https://github.com/openbookpublishers/thoth-client/releases) [![License](https://img.shields.io/github/license/openbookpublishers/thoth-client.svg?colorB=ff0000)](https://github.com/openbookpublishers/thoth-client/blob/master/LICENSE)

## Usage

### Install
```sh
python3 -m pip install thothlibrary==0.5.0
```

### GraphQL Usage
```python
from thothlibrary import ThothClient

thoth = ThothClient()
all_works = thoth.works()
print(all_works)
```

### REST Usage
```python
from thothlibrary import ThothRESTClient

client = ThothRESTClient()
print(client.formats())
```

### CLI REST Usage
```sh
python3 ./thothrest/cli.py
python3 ./thothrest/cli.py formats
python3 ./thothrest/cli.py formats --return-json
```
