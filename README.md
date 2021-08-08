Python client for Thoth's GraphQL and REST APIs

[![Build Status](https://travis-ci.org/openbookpublishers/thoth-client.svg?branch=master)](https://travis-ci.org/openbookpublishers/thoth-client) [![Release](https://img.shields.io/github/release/openbookpublishers/thoth-client.svg?colorB=58839b)](https://github.com/openbookpublishers/thoth-client/releases) [![License](https://img.shields.io/github/license/openbookpublishers/thoth-client.svg?colorB=ff0000)](https://github.com/openbookpublishers/thoth-client/blob/master/LICENSE)

## Usage

### Install
Install is either via pip or cloning the repository.

From pip: 
```sh
python3 -m pip install thothlibrary==0.5.0
```

Or from the repo:
```sh
git clone git@github.com:dqprogramming/thoth-client.git
cd thoth-client
pip3 install -r ./requirements.txt
```

### GraphQL Usage
```python
from thothlibrary import ThothClient

thoth = ThothClient(version="0.4.2")
print(thoth.works())
```

### CLI GraphQL Usage
```sh
python3 -m thothlibrary.cli works --limit=10 --order='{field: PUBLICATION_DATE, direction: DESC}' --work_status=ACTIVE --work_type=MONOGRAPH --offset=1 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
python3 -m thothlibrary.cli publisher --publisher_id=85fd969a-a16c-480b-b641-cb9adf979c3b
python3 -m thothlibrary.cli publishers --limit=10 --order='{field: PUBLISHER_ID, direction: ASC}' --offset=0 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli publications --limit=10 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
python3 -m thothlibrary.cli work --doi="https://doi.org/10.11647/OBP.0222"
python3 -m thothlibrary.cli work --work_id="e0f748b2-984f-45cc-8b9e-13989c31dda4"
python3 -m thothlibrary.cli publisher_count --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli work_count --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
python3 -m thothlibrary.cli publication_count --publication_type="HARDBACK"
```


### REST Usage
```python
from thothlibrary import ThothRESTClient

client = ThothRESTClient()
print(client.formats())
```

### CLI REST Usage
```sh
python3 -m thothrest.cli
python3 -m thothrest.cli formats
python3 -m thothrest.cli formats --return-json
python3 -m thothrest.cli work onix_3.0::project_muse e0f748b2-984f-45cc-8b9e-13989c31dda4
```

## Test Suite
Tests for GraphQL queries are versioned in the thoth-[ver] folder of thothlibrary.

Tests confirm that current code produces good, known object outputs from stored GraphQL input.

## Versioning
The Thoth API is not yet considered stable and functionality changes between versions. The recommended way to add a new version compatibility is:

1. Read the latest Thoth changelog to understand the changes.
2. Copy the latest thoth-[ver] folder to the correctly named new version.
3. Find and replace the strings specified in genfixtures.sh and genjson.sh. Update the version string in tests and endpoints.
4. Run genjson.sh _only_ from inside the tests directory of the new version. This will fetch the latest server JSON responses and store it inside the fixtures directory for these tests. If there are any errors, then the command line CLI has encountered a breaking change that must first be fixed.
5. Run the test suite for the latest version and examine breakages. It is possible that breakages are not actually full breakdown, but merely a change in the serialized object. Nonetheless, fix these by subclassing the previous versions of the API and overriding broken methods. In the cases of total breakage, a non-subclassed rewrite may be more appropriate. (May also apply at major version breaks.)
6. When the test suite passes, or a new object format has been decided and tests rewritten, run genfixtures.sh to freeze the current test suite.

