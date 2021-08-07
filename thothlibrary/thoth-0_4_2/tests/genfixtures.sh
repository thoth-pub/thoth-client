#!/bin/bash

cd ../../../

bash -c "python3 -m thothlibrary.cli works --version=0.4.2 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/works.json"

bash -c "echo '{\"data\": {\"works\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/works_bad.json"

bash -c "python3 -m thothlibrary.cli contributions --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/contributions.pickle"
bash -c "python3 -m thothlibrary.cli works --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/works.pickle"
bash -c "python3 -m thothlibrary.cli publications --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/publications.pickle"
bash -c "python3 -m thothlibrary.cli publishers --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/publishers.pickle"