Python client for Thoth's GraphQL and REST APIs. Currently supports Thoth version 0.6.0.

[![Release](https://img.shields.io/github/release/openbookpublishers/thoth-client.svg?colorB=58839b)](https://github.com/openbookpublishers/thoth-client/releases) [![PyPi version](https://badgen.net/pypi/v/thothlibrary/)](https://pypi.org/project/thothlibrary)

## Usage

### Install
Install is either via pip or cloning the repository.

From pip:
```sh
python3 -m pip install thothlibrary==0.11.0
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

thoth = ThothClient()
print(thoth.works())
```

### CLI GraphQL Usage
```sh
python3 -m thothlibrary.cli contribution --contribution_id=29e4f46b-851a-4d7b-bb41-e6f305fc2b11
python3 -m thothlibrary.cli contributions --limit=10
python3 -m thothlibrary.cli contribution_count
python3 -m thothlibrary.cli contributor --contributor_id=e8def8cf-0dfe-4da9-b7fa-f77e7aec7524
python3 -m thothlibrary.cli contributors --limit=10
python3 -m thothlibrary.cli contributor_count --search="Vincent"
python3 -m thothlibrary.cli institution --institution_id=194614ac-d189-4a74-8bf4-74c0c9de4a81
python3 -m thothlibrary.cli institutions --limit=10
python3 -m thothlibrary.cli funder_count
python3 -m thothlibrary.cli funding --funding_id=5323d3e7-3ae9-4778-8464-9400fbbb959e
python3 -m thothlibrary.cli fundings --limit=10
python3 -m thothlibrary.cli imprint --imprint_id=78b0a283-9be3-4fed-a811-a7d4b9df7b25
python3 -m thothlibrary.cli imprints --limit=25 --offset=0 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli imprint_count --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli issue --issue_id=6bd31b4c-35a9-4177-8074-dab4896a4a3d
python3 -m thothlibrary.cli issues --limit=10
python3 -m thothlibrary.cli issue_count
python3 -m thothlibrary.cli language --language_id=c19e68dd-c5a3-48f1-bd56-089ee732604c
python3 -m thothlibrary.cli languages --limit=10 --language_code=CHI
python3 -m thothlibrary.cli language_count --language_code=CHI
python3 -m thothlibrary.cli price --price_id=818567dd-7d3a-4963-8704-3381b5432877
python3 -m thothlibrary.cli prices --limit=10 --currency_code=GBP
python3 -m thothlibrary.cli price_count --currency_code=GBP
python3 -m thothlibrary.cli publication --publication_id=27b7bdab-e9e5-4220-811e-1f370861f5e1
python3 -m thothlibrary.cli publications --limit=10 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
python3 -m thothlibrary.cli publication_count --publication_type="HARDBACK"
python3 -m thothlibrary.cli publisher --publisher_id=85fd969a-a16c-480b-b641-cb9adf979c3b
python3 -m thothlibrary.cli publishers --limit=10 --order='{field: PUBLISHER_ID, direction: ASC}' --offset=0 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli publisher_count --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli series --series_id=d4b47a76-abff-4047-a3c7-d44d85ccf009
python3 -m thothlibrary.cli serieses --limit=3 --search="Classics"
python3 -m thothlibrary.cli series_count --series_type=BOOK_SERIES
python3 -m thothlibrary.cli subject --subject_id=1291208f-fc43-47a4-a8e6-e132477ad57b
python3 -m thothlibrary.cli subjects --limit=10 --subject_type=BIC
python3 -m thothlibrary.cli subject_count --subject_type=THEMA
python3 -m thothlibrary.cli supported_versions
python3 -m thothlibrary.cli update_cover --doi="https://doi.org/10.11647/OBP.0278" --url="https://cdn.openbookpublishers.com/covers/10.11647/obp.0278.jpg"
python3 -m thothlibrary.cli work --doi="https://doi.org/10.11647/OBP.0222"
python3 -m thothlibrary.cli work --work_id="e0f748b2-984f-45cc-8b9e-13989c31dda4"
python3 -m thothlibrary.cli works --limit=10 --order='{field: PUBLICATION_DATE, direction: DESC}' --work_status=ACTIVE --work_type=MONOGRAPH --offset=1 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
python3 -m thothlibrary.cli work_count --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
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

## Thoth Django
The thothdjango folder includes models, an import routine, subject-code support, and admin procedures to use Thoth in a django app. The import provides unidirectional synchronization from remote Thoth imports to a local database for use in a Django app.

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
7. Include the new version directory in the list of packages in `setup.py`
8. Update `THOTH_VERSION` in `thothlibrary/client.py`

