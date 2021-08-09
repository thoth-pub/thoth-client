"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import collections

from munch import Munch
from datetime import datetime


def _munch_repr(obj):
    """
    This is a hacky munch context switcher. It passes the original __repr__
    pointer back
    @param obj: the object to represent
    @return: the original munch representation
    """
    Munch.__repr__ = munch_local
    return obj.__repr__()


def _author_parser(obj):
    """
    This parses a list of contributors into authors and editors
    @param obj: the Work to parse
    @return: a string representation of authors
    """
    if 'contributions' not in obj:
        return None

    author_dict = {}
    authors = ''

    for contributor in obj.contributions:
        if contributor.contributionType == 'AUTHOR':
            author_dict[contributor.contributionOrdinal] = contributor.fullName
        if contributor.contributionType == "EDITOR":
            author_dict[contributor.contributionOrdinal] = \
                contributor.fullName + " (ed.)"

    od_authors = collections.OrderedDict(sorted(author_dict.items()))

    for k, v in od_authors.items():
        authors += v + ', '

    return authors


def _date_parser(date):
    """
    Formats a date nicely
    @param date: the date string or None
    @return: a formatted date string
    """
    if date:
        return datetime.strptime(date, "%Y-%m-%d").year
    else:
        return "n.d."


def _price_parser(prices):
    if len(prices) > 0 and 'currencyCode' not in prices:
        return '({0}{1})'.format(prices[0].unitPrice, prices[0].currencyCode)
    elif 'currencyCode' in prices:
        return '{0}{1}'.format(prices.unitPrice, prices.currencyCode)
    else:
        return ''


# these are formatting statements for the endpoints
# they are injected to replace the default dictionary (Munch) __repr__ and
# __str__ methods. They let us create nice-looking string representations
# of objects, such as books

def _generic_formatter(format_object, type_name, output):
    """
    A generic formatter that returns either the input or the stored munch repr
    @param format_object: the object on which to operate
    @param type_name: the expected type name
    @param output: the f-string to substitute
    @return: a formatted string
    """
    if "__typename" in format_object and format_object.__typename == type_name:
        return output
    else:
        return f"{_munch_repr(format_object)}"


def _contribution_formatter(contribution):
    """
    A formatting string for contributions
    @param contribution: The contribution object
    @return: A formatted contribution object
    """
    format_str = f"{contribution.fullName} " \
                 f"({contribution.contributionType} of " \
                 f"{contribution.work.fullTitle}) " \
                 f"[{contribution.contributionId}]"
    return _generic_formatter(contribution, 'Contribution', format_str)


def _contributor_formatter(contributor):
    """
    A formatting string for contributors
    @param contributor: The contributor object
    @return: A formatted contributor object
    """
    format_str = f"{contributor.fullName} " \
                 f"({contributor.contributions[0].contributionType} of " \
                 f"{contributor.contributions[0].work.fullTitle}) " \
                 f"[{contributor.contributorId}]"
    return _generic_formatter(contributor, 'Contributor', format_str)


def _funder_formatter(funder):
    """
    A formatting string for funders
    @param funder: The funder object
    @return: A formatted funder object
    """
    format_str = f"{funder.funderName} " \
                 f"funded {len(funder.fundings)} books " \
                 f"[{funder.funderId}]"
    return _generic_formatter(funder, 'Funder', format_str)


def _funding_formatter(funding):
    """
    A formatting string for fundings
    @param funding: The funding object
    @return: A formatted funding object
    """
    format_str = f"{funding.funder.funderName} " \
                 f"funded {funding.work.fullTitle} " \
                 f"[{funding.fundingId}]"
    return _generic_formatter(funding, 'Funding', format_str)


def _imprint_formatter(imprint):
    """
    A formatting string for imprints
    @param imprint: The imprint object
    @return: A formatted imprint object
    """
    format_str = f"{imprint.imprintName} " \
                 f"({imprint.publisher.publisherName}/{imprint.publisherId}) " \
                 f"[{imprint.imprintId}]"
    return _generic_formatter(imprint, 'Imprint', format_str)


def _issue_formatter(issues):
    """
    A formatting string for issues
    @param issues: The issues object
    @return: A formatted issue object
    """
    format_str = f"{issues.work.fullTitle} " \
                 f"in {issues.series.seriesName} " \
                 f"({issues.series.imprint.publisher.publisherName}) " \
                 f"[{issues.issueId}]"
    return _generic_formatter(issues, 'Issue', format_str)


def _language_formatter(language):
    """
    A formatting string for languages
    @param language: The language object
    @return: A formatted language object
    """
    format_str = f"{language.work.fullTitle} " \
                 f"is in {language.languageCode} " \
                 f"({language.languageRelation}) " \
                 f"[{language.languageId}]"
    return _generic_formatter(language, 'Language', format_str)


def _price_formatter(price):
    """
    A formatting string for prices
    @param price: The price object
    @return: A formatted price object
    """
    format_str = f'{price.publication.work.fullTitle} ' \
                 f'({price.publication.work.place}: ' \
                 f'{price.publication.work.imprint.publisher.publisherName}, ' \
                 f'{_date_parser(price.publication.work.publicationDate)}) ' \
                 f"costs {_price_parser(price)} [{price.priceId}]"
    return _generic_formatter(price, 'Price', format_str)


def _publication_formatter(publication):
    """
    A formatting string for publications
    @param publication: the publication on which to operate
    @return: a formatted publication string
    """
    format_str = f'{_author_parser(publication.work)}' \
                 f'{publication.work.fullTitle} ' \
                 f'({publication.work.place}: ' \
                 f'{publication.work.imprint.publisher.publisherName}, ' \
                 f'{_date_parser(publication.work.publicationDate)}) ' \
                 f"[{publication.publicationType}] " \
                 f"{_price_parser(publication.prices)} " \
                 f"[{publication.publicationId}]"
    return _generic_formatter(publication, 'Publication', format_str)


def _publisher_formatter(publisher):
    """
    A formatting string for publishers
    @param publisher: the publisher on which to operate
    @return: a formatted publisher string
    """
    format_str = f"{publisher.publisherName} ({publisher.publisherId})"
    return _generic_formatter(publisher, 'Publisher', format_str)


def _series_formatter(series):
    """
    A formatting string for series
    @param series: the series on which to operate
    @return: a formatted series string
    """
    format_str = f"{series.seriesName} " \
                 f"({series.imprint.publisher.publisherName}) " \
                 f"[{series.seriesId}]"
    return _generic_formatter(series, 'Series', format_str)


def _subject_formatter(subject):
    """
    A formatting string for subjects
    @param subject: the subject on which to operate
    @return: a formatted subject string
    """
    format_str = f"{subject.work.fullTitle} " \
                 f"is in the {subject.subjectCode} " \
                 f"subject area " \
                 f"({subject.subjectType}) " \
                 f"[{subject.subjectId}]"
    return _generic_formatter(subject, 'Subject', format_str)


def _work_formatter(work):
    """
    A formatting string for works
    @param work: the work on which to operate
    @return: a formatted work string
    """
    format_str = f'{_author_parser(work)}' \
                 f'{work.fullTitle} ' \
                 f'({work.place}: ' \
                 f'{work.imprint.publisher.publisherName}, ' \
                 f'{_date_parser(work.publicationDate)}) ' \
                 f'[{work.workId}]'
    return _generic_formatter(work, 'Work', format_str)


default_fields = {
    "contribution": _contribution_formatter,
    "contributions": _contribution_formatter,
    "contributor": _contributor_formatter,
    "contributors": _contributor_formatter,
    "funder": _funder_formatter,
    "funders": _funder_formatter,
    "funding": _funding_formatter,
    "fundings": _funding_formatter,
    "imprint": _imprint_formatter,
    "imprints": _imprint_formatter,
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
    "works": _work_formatter,
}

# this stores the original function pointer of Munch.__repr__ so that we can
# re-inject it above in "_munch_repr"
munch_local = Munch.__repr__


class StructureBuilder:
    """A class to build a Thoth object structure"""

    def __init__(self, structure, data):
        self.structure = structure
        self.data = data

    def create_structure(self):
        """
        Creates an object structure from dictionary input
        @return: an object
        """
        structures = []
        if isinstance(self.data, list):
            for item in self.data:
                x = self._munch(item)
                structures.append(x)
        else:
            x = self._munch(self.data)
            return x

        return structures

    def _munch(self, item):
        """
        Converts our JSON or dict object into an addressable object.
        Also sets up the Munch __repr__ and __str__ functions.
        @param item: the item to convert
        @return: a converted object with string representation
        """
        x = Munch.fromDict(item)
        if self.structure in default_fields.keys():
            struct = default_fields[self.structure]
            Munch.__repr__ = Munch.__str__
            Munch.__str__ = struct
        return x
