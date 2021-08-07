#!/bin/bash

# this script will generate the stored fixtures for the test suite
# it should only be run when the program is generating the correct output
# running this when the code produces bad output will yield the test suite
# inoperative/inaccurate.

# when updating this script, find and replace:
# 0.4.2 -> new version
# 0_4_2 -> new version with underscores

cd ../../../

bash -c "python3 -m thothlibrary.cli contributions --version=0.4.2 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/contributions.json"
bash -c "python3 -m thothlibrary.cli works --version=0.4.2 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/works.json"
bash -c "python3 -m thothlibrary.cli publications --version=0.4.2 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publications.json"
bash -c "python3 -m thothlibrary.cli publishers --version=0.4.2 --limit=4 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publishers.json"
bash -c "python3 -m thothlibrary.cli publisher --version=0.4.2 --publisher_id=85fd969a-a16c-480b-b641-cb9adf979c3b --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publisher.json"
bash -c "python3 -m thothlibrary.cli work --version=0.4.2 --work_id=e0f748b2-984f-45cc-8b9e-13989c31dda4 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/work.json"
bash -c "python3 -m thothlibrary.cli work --version=0.4.2 --doi=https://doi.org/10.21983/P3.0314.1.00 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/workByDoi.json"

bash -c "echo '{\"data\": {\"contributions\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/contributions_bad.json"
bash -c "echo '{\"data\": {\"works\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/works_bad.json"
bash -c "echo '{\"data\": {\"publications\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publications_bad.json"
bash -c "echo '{\"data\": {\"publishers\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publishers_bad.json"
bash -c "echo '{\"data\": {\"publisher\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publisher_bad.json"
bash -c "echo '{\"data\": {\"work\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/work_bad.json"
bash -c "echo '{\"data\": {\"workByDoi\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/workByDoi_bad.json"
