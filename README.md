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

thoth = ThothClient(version="0.4.2")
print(thoth.works())
```

### CLI GraphQL Usage
```sh
python3 ./cli.py works --limit=10 --order='{field: PUBLICATION_DATE, direction: DESC}' --work_status=ACTIVE --work_type=MONOGRAPH --offset=1 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
python3 ./cli.py publishers --limit=10 --order='{field: PUBLISHER_ID, direction: ASC}' --offset=0 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 ./cli.py publisher_count --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
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
python3 ./cli.py work onix_3.0::project_muse e0f748b2-984f-45cc-8b9e-13989c31dda4
```
