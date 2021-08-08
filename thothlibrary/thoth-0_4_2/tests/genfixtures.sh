#!/bin/bash

# this script will generate the stored fixtures for the test suite
# it should only be run when the program is generating the correct output
# running this when the code produces bad output will yield the test suite
# inoperative/inaccurate.

# when updating this script, find and replace:
# 0.4.2 -> new version
# 0_4_2 -> new version with underscores

./genjson.sh

cd ../../../

bash -c "python3 -m thothlibrary.cli contributions --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/contributions.pickle"
bash -c "python3 -m thothlibrary.cli works --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/works.pickle"
bash -c "python3 -m thothlibrary.cli publications --version=0.4.2 --limit=2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/publications.pickle"
bash -c "python3 -m thothlibrary.cli publishers --version=0.4.2 --limit=4 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/publishers.pickle"
bash -c "python3 -m thothlibrary.cli publisher --version=0.4.2 --publisher_id=85fd969a-a16c-480b-b641-cb9adf979c3b --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/publisher.pickle"
bash -c "python3 -m thothlibrary.cli work --version=0.4.2 --work_id=e0f748b2-984f-45cc-8b9e-13989c31dda4 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/work.pickle"
bash -c "python3 -m thothlibrary.cli work --version=0.4.2 --doi=https://doi.org/10.21983/P3.0314.1.00 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/workByDoi.pickle"
bash -c "python3 -m thothlibrary.cli publication --version=0.4.2 --publication_id=34712b75-dcdd-408b-8d0c-cf29a35be2e5 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/publication.pickle"
bash -c "python3 -m thothlibrary.cli imprints --version=0.4.2 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/imprints.pickle"