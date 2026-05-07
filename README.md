Python client for Thoth's APIs. This release supports the Thoth `1.0.0` GraphQL schema and uses personal access tokens for authenticated GraphQL requests.

[![Release](https://img.shields.io/github/release/openbookpublishers/thoth-client.svg?colorB=58839b)](https://github.com/openbookpublishers/thoth-client/releases) [![PyPi version](https://badgen.net/pypi/v/thothlibrary/)](https://pypi.org/project/thothlibrary)

## Usage

### Install
Install is either via pip or cloning the repository.

From pip:
```sh
python3 -m pip install thothlibrary==1.1.2
```

Or from the repo:
```sh
git clone git@github.com:thoth-pub/thoth-client.git
cd thoth-client
pip3 install -r ./requirements.txt
```

### GraphQL Usage
```python
from thothlibrary import ThothClient

thoth = ThothClient()
thoth.set_token("your-pat")
print(thoth.works())
```

### CLI GraphQL Usage
Set `THOTH_PAT` for authenticated commands such as mutations.

```sh
python3 -m thothlibrary.cli contribution --contribution_id=29e4f46b-851a-4d7b-bb41-e6f305fc2b11
python3 -m thothlibrary.cli contributions --limit=10
python3 -m thothlibrary.cli contribution_count
python3 -m thothlibrary.cli contributor --contributor_id=e8def8cf-0dfe-4da9-b7fa-f77e7aec7524
python3 -m thothlibrary.cli contributors --limit=10
python3 -m thothlibrary.cli contributor_count --search="Vincent"
python3 -m thothlibrary.cli institution --institution_id=194614ac-d189-4a74-8bf4-74c0c9de4a81
python3 -m thothlibrary.cli institutions --limit=10
python3 -m thothlibrary.cli funding_count
python3 -m thothlibrary.cli funding --funding_id=5323d3e7-3ae9-4778-8464-9400fbbb959e
python3 -m thothlibrary.cli fundings --limit=10
python3 -m thothlibrary.cli imprint --imprint_id=78b0a283-9be3-4fed-a811-a7d4b9df7b25
python3 -m thothlibrary.cli imprints --limit=25 --offset=0 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli imprint_count --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli issue --issue_id=6bd31b4c-35a9-4177-8074-dab4896a4a3d
python3 -m thothlibrary.cli issues --limit=10
python3 -m thothlibrary.cli issue_count
python3 -m thothlibrary.cli language --language_id=c19e68dd-c5a3-48f1-bd56-089ee732604c
python3 -m thothlibrary.cli languages --limit=10 --language_codes=CHI
python3 -m thothlibrary.cli language_count --language_codes=CHI
python3 -m thothlibrary.cli price --price_id=818567dd-7d3a-4963-8704-3381b5432877
python3 -m thothlibrary.cli prices --limit=10 --currency_codes=GBP
python3 -m thothlibrary.cli price_count --currency_codes=GBP
python3 -m thothlibrary.cli publication --publication_id=27b7bdab-e9e5-4220-811e-1f370861f5e1
python3 -m thothlibrary.cli publications --limit=10 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
python3 -m thothlibrary.cli publication_count --publication_types="HARDBACK"
python3 -m thothlibrary.cli publisher --publisher_id=85fd969a-a16c-480b-b641-cb9adf979c3b
python3 -m thothlibrary.cli publishers --limit=10 --order='{field: PUBLISHER_ID, direction: ASC}' --offset=0 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli publisher_count --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b" "9c41b13c-cecc-4f6a-a151-be4682915ef5"]'
python3 -m thothlibrary.cli series --series_id=d4b47a76-abff-4047-a3c7-d44d85ccf009
python3 -m thothlibrary.cli serieses --limit=3 --search="Classics"
python3 -m thothlibrary.cli series_count --series_types=BOOK_SERIES
python3 -m thothlibrary.cli subject --subject_id=1291208f-fc43-47a4-a8e6-e132477ad57b
python3 -m thothlibrary.cli subjects --limit=10 --subject_types=BIC
python3 -m thothlibrary.cli subject_count --subject_types=THEMA
python3 -m thothlibrary.cli supported_versions
python3 -m thothlibrary.cli update_cover --doi="https://doi.org/10.11647/OBP.0278" --url="https://cdn.openbookpublishers.com/covers/10.11647/obp.0278.jpg"
python3 -m thothlibrary.cli work --doi="https://doi.org/10.11647/OBP.0222"
python3 -m thothlibrary.cli work --work_id="e0f748b2-984f-45cc-8b9e-13989c31dda4"
python3 -m thothlibrary.cli works --limit=10 --order='{field: PUBLICATION_DATE, direction: DESC}' --work_status=ACTIVE --work_types=MONOGRAPH --offset=1 --publishers='["85fd969a-a16c-480b-b641-cb9adf979c3b"]'
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
python3 -m thothlibrary.rest_cli formats
python3 -m thothlibrary.rest_cli formats --return_json
python3 -m thothlibrary.rest_cli work onix_3.0::project_muse e0f748b2-984f-45cc-8b9e-13989c31dda4
```

## Test Suite
The GraphQL test suite is focused on the retained `1.0.0` client surface under `thothlibrary/thoth-1_0_0/tests`.
The export API client is covered by focused tests under `thothlibrary/tests`.
