#!/bin/bash

# this script will generate the stored fixtures for the test suite
# it should only be run when the program is generating the correct output
# running this when the code produces bad output will yield the test suite
# inoperative/inaccurate.

cd ../../../

bash -c "python3 -m thothlibrary.cli contributions --version=0.4.2 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/contributions.json"
bash -c "python3 -m thothlibrary.cli works --version=0.4.2 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/works.json"
bash -c "python3 -m thothlibrary.cli publications --version=0.4.2 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publications.json"
bash -c "python3 -m thothlibrary.cli publishers --version=0.4.2 --limit=4 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publishers.json"

bash -c "echo '{\"data\": {\"contributions\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/contributions_bad.json"
bash -c "echo '{\"data\": {\"works\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/works_bad.json"
bash -c "echo '{\"data\": {\"publications\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publications_bad.json"
bash -c "echo '{\"data\": {\"publishers\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publishers_bad.json"

bash -c "python3 -m thothlibrary.cli contributions --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/contributions.pickle"
bash -c "python3 -m thothlibrary.cli works --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/works.pickle"
bash -c "python3 -m thothlibrary.cli publications --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/publications.pickle"
bash -c "python3 -m thothlibrary.cli publishers --version=0.4.2 --limit=4 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/publishers.pickle"