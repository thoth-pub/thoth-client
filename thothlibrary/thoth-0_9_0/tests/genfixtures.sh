#!/bin/bash

# this script will generate the stored fixtures for the test suite
# it should only be run when the program is generating the correct output
# running this when the code produces bad output will yield the test suite
# inoperative/inaccurate.

# when updating this script, find and replace:
# 0.9.0 -> new version
# 0_9_0 -> new version with underscores

./genjson.sh

cd ../../../

bash -c "python3 -m thothlibrary.cli contributions --version=0.9.0 --limit=2 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/contributions.pickle"
bash -c "python3 -m thothlibrary.cli works --version=0.9.0 --limit=2 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/works.pickle"
bash -c "python3 -m thothlibrary.cli books --version=0.9.0 --limit=2 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/books.pickle"
bash -c "python3 -m thothlibrary.cli publications --version=0.9.0 --limit=2 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/publications.pickle"
bash -c "python3 -m thothlibrary.cli publishers --version=0.9.0 --limit=4 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/publishers.pickle"
bash -c "python3 -m thothlibrary.cli publisher --version=0.9.0 --publisher_id=85fd969a-a16c-480b-b641-cb9adf979c3b --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/publisher.pickle"
bash -c "python3 -m thothlibrary.cli work --version=0.9.0 --work_id=e0f748b2-984f-45cc-8b9e-13989c31dda4 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/work.pickle"
bash -c "python3 -m thothlibrary.cli work --version=0.9.0 --doi=https://doi.org/10.21983/P3.0314.1.00 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/workByDoi.pickle"
bash -c "python3 -m thothlibrary.cli publication --version=0.9.0 --publication_id=27b7bdab-e9e5-4220-811e-1f370861f5e1 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/publication.pickle"
bash -c "python3 -m thothlibrary.cli imprints --version=0.9.0 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/imprints.pickle"
bash -c "python3 -m thothlibrary.cli imprint --version=0.9.0 --imprint_id=78b0a283-9be3-4fed-a811-a7d4b9df7b25 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/imprint.pickle"
bash -c "python3 -m thothlibrary.cli contributors --version=0.9.0 --limit=4 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/contributors.pickle"
bash -c "python3 -m thothlibrary.cli contributor --version=0.9.0 --contributor_id=e8def8cf-0dfe-4da9-b7fa-f77e7aec7524 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/contributor.pickle"
bash -c "python3 -m thothlibrary.cli contribution --version=0.9.0 --contribution_id=29e4f46b-851a-4d7b-bb41-e6f305fc2b11 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/contribution.pickle"
bash -c "python3 -m thothlibrary.cli serieses --version=0.9.0 --limit=3 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/serieses.pickle"
bash -c "python3 -m thothlibrary.cli series --version=0.9.0 --series_id=d4b47a76-abff-4047-a3c7-d44d85ccf009 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/series.pickle"
bash -c "python3 -m thothlibrary.cli issues --version=0.9.0 --limit=10 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/issues.pickle"
bash -c "python3 -m thothlibrary.cli issue --version=0.9.0 --issue_id=8f949497-8f84-4776-8c17-7663a1e1b871 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/issue.pickle"
bash -c "python3 -m thothlibrary.cli languages --version=0.9.0 --limit=10 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/languages.pickle"
bash -c "python3 -m thothlibrary.cli language --version=0.9.0 --language_id=c19e68dd-c5a3-48f1-bd56-089ee732604c --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/language.pickle"
bash -c "python3 -m thothlibrary.cli prices --version=0.9.0 --limit=10 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/prices.pickle"
bash -c "python3 -m thothlibrary.cli price --version=0.9.0 --price_id=818567dd-7d3a-4963-8704-3381b5432877 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/price.pickle"
bash -c "python3 -m thothlibrary.cli subjects --version=0.9.0 --limit=10 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/subjects.pickle"
bash -c "python3 -m thothlibrary.cli subject --version=0.9.0 --subject_id=1291208f-fc43-47a4-a8e6-e132477ad57b --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/subject.pickle"
bash -c "python3 -m thothlibrary.cli institutions --version=0.9.0 --limit=10 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/institutions.pickle"
bash -c "python3 -m thothlibrary.cli institution --version=0.9.0 --institution_id=194614ac-d189-4a74-8bf4-74c0c9de4a81 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/institution.pickle"
bash -c "python3 -m thothlibrary.cli fundings --version=0.9.0 --limit=10 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/fundings.pickle"
bash -c "python3 -m thothlibrary.cli funding --version=0.9.0 --funding_id=5323d3e7-3ae9-4778-8464-9400fbbb959e --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/funding.pickle"
bash -c "python3 -m thothlibrary.cli references --version=0.9.0 --limit=10 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/references.pickle"
bash -c "python3 -m thothlibrary.cli reference --version=0.9.0 --reference_id=bafb182d-2667-436d-93df-7a9842733a03 --serialize > thothlibrary/thoth-0_9_0/tests/fixtures/reference.pickle"
