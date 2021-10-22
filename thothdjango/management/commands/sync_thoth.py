"""
(c) ΔQ Programming LLP, 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
from django.core.management.base import BaseCommand
from thothlibrary import ThothClient
from thoth.models import BIC, BISAC, Contribution, Contributor
from thoth.models import Publisher, Subject, Thema, Work


class Command(BaseCommand):
    """
    A management command that syncs Thoth entries to the local database
    """

    help = "Syncs Thoth metadata to the platform"

    def handle(self, *args, **options):
        """
        A management command that syncs Thoth entries to the local database
        :param args: command line arguments
        :param options: command line options
        """
        default_thoth_endpoint = "https://api.thoth.pub"

        # TODO: these should be specified dynamically as you wish in your code
        # the dummy code below fetches punctum books and Open Book Publishers

        to_fetch = [{'publisher': '9c41b13c-cecc-4f6a-a151-be4682915ef5',
                     'endpoint': default_thoth_endpoint},
                    {'publisher': '85fd969a-a16c-480b-b641-cb9adf979c3b',
                     'endpoint': default_thoth_endpoint}]

        for thoth_sync in to_fetch:
            # a neater way to do this would be to aggregate together all
            # requests that share an endpoint. However, that's more complex
            # so we just do standard iter here

            client = ThothClient(thoth_endpoint=thoth_sync['endpoint'])

            # lookup the publisher name for friendly display
            # this adds an extra API call
            publisher = client.publisher(publisher_id=thoth_sync['publisher'])

            # pull the full list of works for each publisher
            # as a note: technically, a work is different to a publication
            # a publication is a specific format, at a specific price point
            print("Fetching works for "
                  "publisher {0} [{1}]".format(thoth_sync['publisher'],
                                               publisher.publisherName))

            publisher_model = Publisher.objects.get_or_create(
                thoth_id=publisher.publisherId,
                thoth_instance=thoth_sync['endpoint']
            )[0]

            publisher_model.publisher_name = publisher.publisherName
            publisher_model.save()

            # we can handle a max of 9999 works at any one time
            # Thoth does support pagination, but currently has no way of
            # precisely querying the expected number of records
            works = client.works(limit=9999, publishers='["{0}"]'.format(
                publisher.publisherId))

            self._sync_works(publisher_model, thoth_sync, works)

            self._verify_exists_in_thoth(thoth_sync, works)

    @staticmethod
    def _verify_exists_in_thoth(thoth_sync, works):
        """
        Verifies that entries in our database are in remote Thoth servers
        :param thoth_sync: the Thoth instance
        :param works: a list of works from a Thoth instance to check
        """

        works_in_db = Work.objects.filter(
            publisher__thoth_id=thoth_sync['publisher'])

        for work in works_in_db:
            if any([x for x in works if str(x.workId) == str(work.thoth_id)]):
                print("[Verified] {0} exists in Thoth".format(work))
            else:
                print("[Unverified] Could not find {0} in Thoth. "
                      "Deleting.".format(work))
                work.delete()

    def _sync_works(self, publisher_model, thoth_sync, works):
        """
        Synchronizes works from the remote Thoth instance
        :param publisher_model: the publisher to use
        :param thoth_sync: the Thoth instance
        :param works: a list of works from a Thoth instance to sync
        """
        for work in works:
            # build a work model
            work_model, created = Work.objects.get_or_create(
                thoth_id=work.workId)
            work_model.thoth_id = work.workId
            work_model.doi = work.doi
            work_model.work_type = work.workType
            work_model.full_title = work.fullTitle
            work_model.cover_url = work.coverUrl
            work_model.cover_caption = work.coverCaption
            work_model.publisher = publisher_model
            work_model.landing_page = work.landingPage

            if work.license:
                work_model.license = work.license

            if work.longAbstract:
                work_model.long_abstract = work.longAbstract

            if work.shortAbstract:
                work_model.short_abstract = work.shortAbstract

            if work.publicationDate:
                work_model.published_date = work.publicationDate

            work_model.save()

            self._sync_contributions(thoth_sync, work, work_model)

            self._sync_subjects(thoth_sync, work, work_model)

    @staticmethod
    def _sync_subjects(thoth_sync, work, work_model):
        """
        Synchronizes Thoth subject codes to the local database
        :param thoth_sync: the Thoth sync object
        :param work: the work to sync to
        :param work_model: the database work model
        """
        # save the subjects
        for subject in work.subjects:
            subject_model = Subject.objects.get_or_create(
                thoth_id=subject.subjectId,
                thoth_instance=thoth_sync['endpoint'],
                work=work_model
            )[0]

            subject_model.subject_type = subject.subjectType
            subject_model.subject_code = subject.subjectCode
            subject_model.subject_ordinal = subject.subjectOrdinal
            subject_model.thoth_id = subject.subjectId

            # see if there's a BIC entry
            if subject.subjectType == "THEMA":
                try:
                    thema_model = Thema.objects.get(
                        code=subject.subjectCode
                    )

                    subject_model.thema_code = thema_model
                except Thema.DoesNotExist:
                    pass
            elif subject.subjectType == "BIC":
                try:
                    bic_model = BIC.objects.get(
                        code=subject.subjectCode
                    )

                    subject_model.BIC_code = bic_model
                except BIC.DoesNotExist:
                    pass
            elif subject.subjectType == "BISAC":
                try:
                    bisac_model = BISAC.objects.get(
                        code=subject.subjectCode
                    )

                    subject_model.BISAC_code = bisac_model
                except BISAC.DoesNotExist:
                    pass

            subject_model.save()

    @staticmethod
    def _sync_contributions(thoth_sync, work, work_model):
        """
        Synchronize contributors from Thoth to the local DB
        :param thoth_sync: the Thoth instance
        :param work: the work instance
        :param work_model: the work model instance
        """
        # build the contributions and contributors
        for contribution in work.contributions:
            # find or build the contributor and then update it
            contributor = contribution.contributor

            contributor_model = Contributor.objects.get_or_create(
                thoth_id=contributor.contributorId,
                thoth_instance=thoth_sync['endpoint'])[0]

            contributor_model.first_name = contributor.firstName
            contributor_model.last_name = contributor.lastName
            contributor_model.full_name = contributor.fullName
            contributor_model.orcid = contributor.orcid
            contributor_model.thoth_id = contributor.contributorId

            contributor_model.save()

            # now save the contribution

            contribution_model = Contribution.objects.get_or_create(
                thoth_id=contribution.contributionId,
                thoth_instance=thoth_sync['endpoint'])[0]

            contribution_model.institution = contribution.institution
            contribution_model.contribution_ordinal \
                = contribution.contributionOrdinal
            contribution_model.contribution_type = \
                contribution.contributionType
            contributor_model.thoth_id = contribution.contributionId

            contribution_model.work = work_model

            contribution_model.contributor = contributor_model

            contribution_model.save()
