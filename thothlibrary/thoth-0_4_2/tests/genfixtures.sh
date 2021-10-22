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
bash -c "python3 -m thothlibrary.cli imprint --version=0.4.2 --imprint_id=78b0a283-9be3-4fed-a811-a7d4b9df7b25 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/imprint.pickle"
bash -c "python3 -m thothlibrary.cli contributors --version=0.4.2 --limit=4 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/contributors.pickle"
bash -c "python3 -m thothlibrary.cli contributor --version=0.4.2 --contributor_id=e8def8cf-0dfe-4da9-b7fa-f77e7aec7524 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/contributor.pickle"
bash -c "python3 -m thothlibrary.cli contribution --version=0.4.2 --contribution_id=29e4f46b-851a-4d7b-bb41-e6f305fc2b11 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/contribution.pickle"
bash -c "python3 -m thothlibrary.cli serieses --version=0.4.2 --limit=3 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/serieses.pickle"
bash -c "python3 -m thothlibrary.cli series --version=0.4.2 --series_id=d4b47a76-abff-4047-a3c7-d44d85ccf009 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/series.pickle"
bash -c "python3 -m thothlibrary.cli issues --version=0.4.2 --limit=10 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/issues.pickle"
bash -c "python3 -m thothlibrary.cli issue --version=0.4.2 --issue_id=6bd31b4c-35a9-4177-8074-dab4896a4a3d --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/issue.pickle"
bash -c "python3 -m thothlibrary.cli languages --version=0.4.2 --limit=10 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/languages.pickle"
bash -c "python3 -m thothlibrary.cli language --version=0.4.2 --language_id=c19e68dd-c5a3-48f1-bd56-089ee732604c --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/language.pickle"
bash -c "python3 -m thothlibrary.cli prices --version=0.4.2 --limit=10 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/prices.pickle"
bash -c "python3 -m thothlibrary.cli price --version=0.4.2 --price_id=818567dd-7d3a-4963-8704-3381b5432877 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/price.pickle"
bash -c "python3 -m thothlibrary.cli subjects --version=0.4.2 --limit=10 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/subjects.pickle"
bash -c "python3 -m thothlibrary.cli subject --version=0.4.2 --subject_id=1291208f-fc43-47a4-a8e6-e132477ad57b --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/subject.pickle"
bash -c "python3 -m thothlibrary.cli funders --version=0.4.2 --limit=10 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/funders.pickle"
bash -c "python3 -m thothlibrary.cli funder --version=0.4.2 --funder_id=194614ac-d189-4a74-8bf4-74c0c9de4a81 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/funder.pickle"
bash -c "python3 -m thothlibrary.cli fundings --version=0.4.2 --limit=10 --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/fundings.pickle"
bash -c "python3 -m thothlibrary.cli funding --version=0.4.2 --funding_id=5323d3e7-3ae9-4778-8464-9400fbbb959e --serialize > thothlibrary/thoth-0_4_2/tests/fixtures/funding.pickle"