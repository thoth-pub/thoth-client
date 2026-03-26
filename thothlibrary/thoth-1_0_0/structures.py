"""
Copyright (c) 2026 Thoth Open Metadata
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import collections
from datetime import datetime

from munch import Munch


def _munch_repr(obj):
    Munch.__repr__ = munch_local
    return obj.__repr__()


def _ordered_names(contributions):
    author_dict = {}

    for contribution in contributions or []:
        name = getattr(contribution, "fullName", None)
        if not name:
            continue
        if contribution.contributionType == "AUTHOR":
            author_dict[contribution.contributionOrdinal] = name
        elif contribution.contributionType == "EDITOR":
            author_dict[contribution.contributionOrdinal] = name + " (ed.)"

    ordered = collections.OrderedDict(sorted(author_dict.items()))
    return ", ".join(ordered.values())


def _canonical_item(items):
    if not items:
        return None
    for item in items:
        if getattr(item, "canonical", False):
            return item
    return items[0]


def _canonical_title(work):
    title = _canonical_item(getattr(work, "titles", []))
    if title:
        return getattr(title, "fullTitle", getattr(title, "title", None))
    return getattr(work, "fullTitle", None)


def _canonical_biography(contribution):
    biography = _canonical_item(getattr(contribution, "biographies", []))
    if biography:
        return getattr(biography, "content", None)
    return getattr(contribution, "biography", None)


def _publisher_name(work):
    try:
        return work.imprint.publisher.publisherName
    except AttributeError:
        return None


def _work_place(work):
    return getattr(work, "place", None) or "n.p."


def _date_parser(date):
    if date:
        return datetime.strptime(date, "%Y-%m-%d").year
    return "n.d."


def _price_parser(prices):
    if isinstance(prices, list) and prices:
        return "({0}{1})".format(prices[0].unitPrice, prices[0].currencyCode)
    if hasattr(prices, "currencyCode"):
        return "{0}{1}".format(prices.unitPrice, prices.currencyCode)
    return ""


def _generic_formatter(format_object, type_name, output):
    if "__typename" in format_object and format_object.__typename == type_name:
        return output
    return f"{_munch_repr(format_object)}"


def _contribution_formatter(contribution):
    work_title = _canonical_title(getattr(contribution, "work", None)) or "Untitled"
    format_str = (
        f"{contribution.fullName} "
        f"({contribution.contributionType} of {work_title}) "
        f"[{contribution.contributionId}]"
    )
    return _generic_formatter(contribution, "Contribution", format_str)


def _contributor_formatter(contributor):
    format_str = (
        f"{contributor.fullName} "
        f"contributed to {len(getattr(contributor, 'contributions', []))} works "
        f"[{contributor.contributorId}]"
    )
    return _generic_formatter(contributor, "Contributor", format_str)


def _institution_formatter(institution):
    format_str = (
        f"{institution.institutionName} "
        f"affiliated with {len(getattr(institution, 'fundings', []))} books "
        f"[{institution.institutionId}]"
    )
    return _generic_formatter(institution, "Institution", format_str)


def _funding_formatter(funding):
    work_title = _canonical_title(getattr(funding, "work", None)) or "Untitled"
    institution_name = getattr(getattr(funding, "institution", None),
                               "institutionName", "Unknown institution")
    format_str = f"{institution_name} funded {work_title} [{funding.fundingId}]"
    return _generic_formatter(funding, "Funding", format_str)


def _imprint_formatter(imprint):
    publisher_name = getattr(getattr(imprint, "publisher", None),
                             "publisherName", "Unknown publisher")
    publisher_id = getattr(getattr(imprint, "publisher", None),
                           "publisherId", "unknown")
    format_str = (
        f"{imprint.imprintName} "
        f"({publisher_name}/{publisher_id}) "
        f"[{imprint.imprintId}]"
    )
    return _generic_formatter(imprint, "Imprint", format_str)


def _issue_formatter(issue):
    work_title = _canonical_title(getattr(issue, "work", None)) or "Untitled"
    series_name = getattr(getattr(issue, "series", None), "seriesName",
                          "Unknown series")
    format_str = f"{work_title} in {series_name} [{issue.issueId}]"
    return _generic_formatter(issue, "Issue", format_str)


def _language_formatter(language):
    work_title = _canonical_title(getattr(language, "work", None)) or "Untitled"
    format_str = (
        f"{work_title} is in {language.languageCode} "
        f"({language.languageRelation}) [{language.languageId}]"
    )
    return _generic_formatter(language, "Language", format_str)


def _price_formatter(price):
    work = getattr(getattr(price, "publication", None), "work", None)
    title = _canonical_title(work) or "Untitled"
    publisher = _publisher_name(work) or "Unknown publisher"
    format_str = (
        f"{title} ({_work_place(work)}: {publisher}, "
        f"{_date_parser(getattr(work, 'publicationDate', None))}) "
        f"costs {_price_parser(price)} [{price.priceId}]"
    )
    return _generic_formatter(price, "Price", format_str)


def _publication_formatter(publication):
    work = getattr(publication, "work", None)
    title = _canonical_title(work) or "Untitled"
    authors = _ordered_names(getattr(work, "contributions", []))
    publisher = _publisher_name(work) or "Unknown publisher"
    format_str = (
        f"{authors + ', ' if authors else ''}{title} "
        f"({_work_place(work)}: {publisher}, "
        f"{_date_parser(getattr(work, 'publicationDate', None))}) "
        f"[{publication.publicationType}] "
        f"{_price_parser(getattr(publication, 'prices', []))} "
        f"[{publication.publicationId}]"
    )
    return _generic_formatter(publication, "Publication", format_str)


def _publisher_formatter(publisher):
    format_str = f"{publisher.publisherName} ({publisher.publisherId})"
    return _generic_formatter(publisher, "Publisher", format_str)


def _series_formatter(series):
    publisher = getattr(getattr(getattr(series, "imprint", None), "publisher",
                                None), "publisherName", "Unknown publisher")
    format_str = f"{series.seriesName} ({publisher}) [{series.seriesId}]"
    return _generic_formatter(series, "Series", format_str)


def _subject_formatter(subject):
    work_title = _canonical_title(getattr(subject, "work", None)) or "Untitled"
    format_str = (
        f"{work_title} is in the {subject.subjectCode} "
        f"subject area ({subject.subjectType}) [{subject.subjectId}]"
    )
    return _generic_formatter(subject, "Subject", format_str)


def _work_formatter(work):
    authors = _ordered_names(getattr(work, "contributions", []))
    title = _canonical_title(work) or "Untitled"
    publisher = _publisher_name(work) or "Unknown publisher"
    format_str = (
        f"{authors + ', ' if authors else ''}{title} "
        f"({_work_place(work)}: {publisher}, "
        f"{_date_parser(getattr(work, 'publicationDate', None))}) "
        f"[{work.workId}]"
    )
    return _generic_formatter(work, "Work", format_str)


def _affiliation_formatter(affiliation):
    institution = getattr(getattr(affiliation, "institution", None),
                          "institutionName", "Unknown institution")
    contributor = getattr(getattr(affiliation, "contribution", None),
                          "fullName", "Unknown contributor")
    format_str = (
        f"{contributor} affiliated with {institution} "
        f"[{affiliation.affiliationId}]"
    )
    return _generic_formatter(affiliation, "Affiliation", format_str)


def _title_formatter(title):
    format_str = f"{title.fullTitle} ({title.localeCode}) [{title.titleId}]"
    return _generic_formatter(title, "Title", format_str)


def _abstract_formatter(abstract):
    work_title = _canonical_title(getattr(abstract, "work", None)) or "Untitled"
    format_str = (
        f"{work_title} {abstract.abstractType} abstract "
        f"({abstract.localeCode}) [{abstract.abstractId}]"
    )
    return _generic_formatter(abstract, "Abstract", format_str)


def _biography_formatter(biography):
    contributor = getattr(getattr(biography, "contribution", None),
                          "fullName", "Unknown contributor")
    format_str = (
        f"{contributor} biography ({biography.localeCode}) "
        f"[{biography.biographyId}]"
    )
    return _generic_formatter(biography, "Biography", format_str)


def _work_resource_formatter(resource):
    title = getattr(resource, "title", "Untitled")
    format_str = f"{title} ({resource.resourceType}) [{resource.workResourceId}]"
    return _generic_formatter(resource, "WorkResource", format_str)


def _award_formatter(award):
    title = getattr(award, "title", "Untitled")
    format_str = f"{title} [{award.awardId}]"
    return _generic_formatter(award, "Award", format_str)


def _endorsement_formatter(endorsement):
    author = getattr(endorsement, "authorName", "Unknown endorser")
    format_str = f"{author} endorsement [{endorsement.endorsementId}]"
    return _generic_formatter(endorsement, "Endorsement", format_str)


def _book_review_formatter(book_review):
    title = getattr(book_review, "title", None) or "Untitled review"
    format_str = f"{title} [{book_review.bookReviewId}]"
    return _generic_formatter(book_review, "BookReview", format_str)


def _work_featured_video_formatter(video):
    title = getattr(video, "title", None) or "Featured video"
    format_str = f"{title} [{video.workFeaturedVideoId}]"
    return _generic_formatter(video, "WorkFeaturedVideo", format_str)


def _contact_formatter(contact):
    format_str = (
        f"{contact.contactType} contact {contact.email} [{contact.contactId}]"
    )
    return _generic_formatter(contact, "Contact", format_str)


def _file_formatter(file_object):
    format_str = f"{file_object.fileType} file [{file_object.fileId}]"
    return _generic_formatter(file_object, "File", format_str)


default_fields = {
    "contribution": _contribution_formatter,
    "contributions": _contribution_formatter,
    "contributor": _contributor_formatter,
    "contributors": _contributor_formatter,
    "funding": _funding_formatter,
    "fundings": _funding_formatter,
    "imprint": _imprint_formatter,
    "imprints": _imprint_formatter,
    "institution": _institution_formatter,
    "institutions": _institution_formatter,
    "issue": _issue_formatter,
    "issues": _issue_formatter,
    "language": _language_formatter,
    "languages": _language_formatter,
    "price": _price_formatter,
    "prices": _price_formatter,
    "publication": _publication_formatter,
    "publications": _publication_formatter,
    "publisher": _publisher_formatter,
    "publishers": _publisher_formatter,
    "series": _series_formatter,
    "serieses": _series_formatter,
    "subject": _subject_formatter,
    "subjects": _subject_formatter,
    "work": _work_formatter,
    "workByDoi": _work_formatter,
    "bookByDoi": _work_formatter,
    "chapterByDoi": _work_formatter,
    "works": _work_formatter,
    "books": _work_formatter,
    "chapters": _work_formatter,
    "affiliation": _affiliation_formatter,
    "affiliations": _affiliation_formatter,
    "title": _title_formatter,
    "titles": _title_formatter,
    "abstract": _abstract_formatter,
    "abstracts": _abstract_formatter,
    "biography": _biography_formatter,
    "biographies": _biography_formatter,
    "additionalResource": _work_resource_formatter,
    "additionalResources": _work_resource_formatter,
    "award": _award_formatter,
    "awards": _award_formatter,
    "endorsement": _endorsement_formatter,
    "endorsements": _endorsement_formatter,
    "bookReview": _book_review_formatter,
    "bookReviews": _book_review_formatter,
    "workFeaturedVideo": _work_featured_video_formatter,
    "workFeaturedVideos": _work_featured_video_formatter,
    "contact": _contact_formatter,
    "contacts": _contact_formatter,
    "file": _file_formatter,
}

munch_local = Munch.__repr__


class StructureBuilder:
    """A class to build a Thoth object structure."""

    def __init__(self, structure, data):
        self.structure = structure
        self.data = data

    def create_structure(self):
        structures = []
        if isinstance(self.data, list):
            for item in self.data:
                structures.append(self._munch(item))
            return structures

        return self._munch(self.data)

    def _munch(self, item):
        x = Munch.fromDict(item)
        if self.structure in default_fields:
            struct = default_fields[self.structure]
            Munch.__repr__ = Munch.__str__
            Munch.__str__ = struct
        return x
