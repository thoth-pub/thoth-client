#!/bin/bash

# this script will generate the stored fixtures for the test suite
# it should only be run when the program is generating the correct output
# running this when the code produces bad output will yield the test suite
# inoperative/inaccurate.

# when updating this script, find and replace:
# 0.4.2 -> new version
# 0_4_2 -> new version with underscores

cd ../../../

bash -c "python3 -m thothlibrary.cli contributions --version=0.5.0 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/contributions.json"
bash -c "python3 -m thothlibrary.cli works --version=0.5.0 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/works.json"
bash -c "python3 -m thothlibrary.cli publications --version=0.5.0 --limit=2 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publications.json"
bash -c "python3 -m thothlibrary.cli publishers --version=0.5.0 --limit=4 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publishers.json"
bash -c "python3 -m thothlibrary.cli publisher --version=0.5.0 --publisher_id=85fd969a-a16c-480b-b641-cb9adf979c3b --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publisher.json"
bash -c "python3 -m thothlibrary.cli work --version=0.5.0 --work_id=e0f748b2-984f-45cc-8b9e-13989c31dda4 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/work.json"
bash -c "python3 -m thothlibrary.cli work --version=0.5.0 --doi=https://doi.org/10.21983/P3.0314.1.00 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/workByDoi.json"
bash -c "python3 -m thothlibrary.cli publication --version=0.5.0 --publication_id=27b7bdab-e9e5-4220-811e-1f370861f5e1 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/publication.json"
bash -c "python3 -m thothlibrary.cli imprints --version=0.5.0 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/imprints.json"
bash -c "python3 -m thothlibrary.cli imprint --version=0.5.0 --imprint_id=78b0a283-9be3-4fed-a811-a7d4b9df7b25 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/imprint.json"
bash -c "python3 -m thothlibrary.cli contributors --version=0.5.0 --limit=4 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/contributors.json"
bash -c "python3 -m thothlibrary.cli contributor --version=0.5.0 --contributor_id=e8def8cf-0dfe-4da9-b7fa-f77e7aec7524 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/contributor.json"
bash -c "python3 -m thothlibrary.cli contribution --version=0.5.0 --contribution_id=29e4f46b-851a-4d7b-bb41-e6f305fc2b11 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/contribution.json"
bash -c "python3 -m thothlibrary.cli serieses --version=0.5.0 --limit=3 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/serieses.json"
bash -c "python3 -m thothlibrary.cli series --version=0.5.0 --series_id=d4b47a76-abff-4047-a3c7-d44d85ccf009 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/series.json"
bash -c "python3 -m thothlibrary.cli issues --version=0.5.0 --limit=10 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/issues.json"
bash -c "python3 -m thothlibrary.cli issue --version=0.5.0 --issue_id=6bd31b4c-35a9-4177-8074-dab4896a4a3d --raw > thothlibrary/thoth-0_4_2/tests/fixtures/issue.json"
bash -c "python3 -m thothlibrary.cli languages --version=0.5.0 --limit=10 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/languages.json"
bash -c "python3 -m thothlibrary.cli language --version=0.5.0 --language_id=c19e68dd-c5a3-48f1-bd56-089ee732604c --raw > thothlibrary/thoth-0_4_2/tests/fixtures/language.json"
bash -c "python3 -m thothlibrary.cli prices --version=0.5.0 --limit=10 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/prices.json"
bash -c "python3 -m thothlibrary.cli price --version=0.5.0 --price_id=818567dd-7d3a-4963-8704-3381b5432877 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/price.json"
bash -c "python3 -m thothlibrary.cli subjects --version=0.5.0 --limit=10 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/subjects.json"
bash -c "python3 -m thothlibrary.cli subject --version=0.5.0 --subject_id=1291208f-fc43-47a4-a8e6-e132477ad57b --raw > thothlibrary/thoth-0_4_2/tests/fixtures/subject.json"
bash -c "python3 -m thothlibrary.cli funders --version=0.5.0 --limit=10 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/funders.json"
bash -c "python3 -m thothlibrary.cli funder --version=0.5.0 --funder_id=194614ac-d189-4a74-8bf4-74c0c9de4a81 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/funder.json"
bash -c "python3 -m thothlibrary.cli fundings --version=0.5.0 --limit=10 --raw > thothlibrary/thoth-0_4_2/tests/fixtures/fundings.json"
bash -c "python3 -m thothlibrary.cli funding --version=0.5.0 --funding_id=5323d3e7-3ae9-4778-8464-9400fbbb959e --raw > thothlibrary/thoth-0_4_2/tests/fixtures/funding.json"

bash -c "echo '{\"data\": {\"contributions\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/contributions_bad.json"
bash -c "echo '{\"data\": {\"works\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/works_bad.json"
bash -c "echo '{\"data\": {\"publications\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publications_bad.json"
bash -c "echo '{\"data\": {\"publishers\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publishers_bad.json"
bash -c "echo '{\"data\": {\"publisher\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publisher_bad.json"
bash -c "echo '{\"data\": {\"work\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/work_bad.json"
bash -c "echo '{\"data\": {\"workByDoi\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/workByDoi_bad.json"
bash -c "echo '{\"data\": {\"publication\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/publication_bad.json"
bash -c "echo '{\"data\": {\"imprints\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/imprints_bad.json"
bash -c "echo '{\"data\": {\"imprint\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/imprint_bad.json"
bash -c "echo '{\"data\": {\"contributors\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/contributors_bad.json"
bash -c "echo '{\"data\": {\"contributor\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/contributor_bad.json"
bash -c "echo '{\"data\": {\"contribution\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/contribution_bad.json"
bash -c "echo '{\"data\": {\"serieses\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/serieses_bad.json"
bash -c "echo '{\"data\": {\"series\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/series_bad.json"
bash -c "echo '{\"data\": {\"issues\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/issues_bad.json"
bash -c "echo '{\"data\": {\"issue\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/issue_bad.json"
bash -c "echo '{\"data\": {\"languages\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/languages_bad.json"
bash -c "echo '{\"data\": {\"language\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/language_bad.json"
bash -c "echo '{\"data\": {\"prices\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/prices_bad.json"
bash -c "echo '{\"data\": {\"price\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/price_bad.json"
bash -c "echo '{\"data\": {\"subjects\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/subjects_bad.json"
bash -c "echo '{\"data\": {\"subject\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/subject_bad.json"
bash -c "echo '{\"data\": {\"funders\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/funders_bad.json"
bash -c "echo '{\"data\": {\"funder\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/funder_bad.json"
bash -c "echo '{\"data\": {\"fundings\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/fundings_bad.json"
bash -c "echo '{\"data\": {\"funding\": [\"1\"] } }'  > thothlibrary/thoth-0_4_2/tests/fixtures/funding_bad.json"
