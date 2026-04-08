"""GraphQL field selections for the Thoth 1.0.0 client."""

CANONICAL_TITLES = (
    "titles(order: {field: CANONICAL, direction: DESC}, markupFormat: JATS_XML)"
    " { titleId localeCode fullTitle title subtitle canonical __typename }"
)
CANONICAL_ABSTRACTS = (
    "abstracts(order: {field: CANONICAL, direction: DESC}, markupFormat: JATS_XML)"
    " { abstractId localeCode content abstractType canonical __typename }"
)
CANONICAL_BIOGRAPHIES = (
    "biographies(order: {field: CANONICAL, direction: DESC}, markupFormat: JATS_XML)"
    " { biographyId localeCode content canonical __typename }"
)

WORK_LINK = (
    "work { workId doi publicationDate place "
    + CANONICAL_TITLES +
    " imprint { imprintId imprintName publisher { publisherId publisherName __typename } __typename } "
    "__typename }"
)

PUBLISHER_LINK = (
    "publisher { publisherId publisherName publisherShortname publisherUrl "
    "__typename }"
)

FILE_FIELDS = [
    "fileId",
    "fileType",
    "workId",
    "publicationId",
    "additionalResourceId",
    "workFeaturedVideoId",
    "objectKey",
    "cdnUrl",
    "mimeType",
    "bytes",
    "sha256",
    "createdAt",
    "updatedAt",
    "__typename",
]

WORK_FULL_FIELDS = [
    "workId",
    "workType",
    "workStatus",
    "reference",
    "edition",
    "imprintId",
    "doi",
    "publicationDate",
    "withdrawnDate",
    "place",
    "pageCount",
    "pageBreakdown",
    "imageCount",
    "tableCount",
    "audioCount",
    "videoCount",
    "license",
    "copyrightHolder",
    "landingPage",
    "lccn",
    "oclc",
    "generalNote",
    "bibliographyNote",
    "toc",
    "resourcesDescription",
    "coverUrl",
    "coverCaption",
    "firstPage",
    "lastPage",
    "pageInterval",
    "createdAt",
    "updatedAt",
    CANONICAL_TITLES,
    CANONICAL_ABSTRACTS,
    "languages { languageId languageCode languageRelation __typename }",
    (
        "publications { publicationId publicationType isbn accessibilityStandard "
        "accessibilityAdditionalStandard accessibilityException accessibilityReportUrl "
        "file { fileId fileType cdnUrl __typename } "
        "locations { locationId landingPage fullTextUrl locationPlatform canonical __typename } "
        "__typename }"
    ),
    (
        "contributions(order: {field: CONTRIBUTION_ORDINAL, direction: ASC}) "
        "{ contributionId contributorId contributionType mainContribution firstName "
        "lastName fullName contributionOrdinal "
        + CANONICAL_BIOGRAPHIES +
        " affiliations { affiliationId affiliationOrdinal position institution { institutionId institutionName ror __typename } __typename } "
        "contributor { contributorId firstName lastName fullName orcid website __typename } "
        "__typename }"
    ),
    "subjects { subjectId subjectType subjectCode subjectOrdinal __typename }",
    (
        "relations { workRelationId relatedWorkId relationType relationOrdinal "
        "relatedWork { workId doi " + CANONICAL_TITLES + " __typename } "
        "__typename }"
    ),
    "references { referenceId referenceOrdinal doi unstructuredCitation url __typename }",
    (
        "fundings { fundingId grantNumber program projectName projectShortname "
        "institution { institutionId institutionName institutionDoi ror __typename } "
        "__typename }"
    ),
    (
        "issues { issueId issueOrdinal issueNumber "
        "series { seriesId seriesName issnPrint issnDigital __typename } "
        "__typename }"
    ),
    (
        "additionalResources { workResourceId resourceType "
        "title(markupFormat: JATS_XML) description(markupFormat: JATS_XML) "
        "resourceOrdinal file { fileId fileType cdnUrl __typename } __typename }"
    ),
    (
        "awards { awardId title(markupFormat: JATS_XML) "
        "prizeStatement(markupFormat: JATS_XML) awardOrdinal __typename }"
    ),
    (
        "endorsements { endorsementId authorName text(markupFormat: JATS_XML) "
        "endorsementOrdinal __typename }"
    ),
    (
        "bookReviews { bookReviewId title(markupFormat: JATS_XML) "
        "text(markupFormat: JATS_XML) reviewOrdinal __typename }"
    ),
    (
        "featuredVideo { workFeaturedVideoId title url width height "
        "file { fileId fileType cdnUrl __typename } __typename }"
    ),
    (
        "imprint { imprintId imprintName publisherId defaultCurrency "
        "defaultPlace defaultLocale __typename "
        + PUBLISHER_LINK +
        " }"
    ),
    "__typename",
]

WORK_LIST_FIELDS = [
    "workId",
    "workType",
    "workStatus",
    "doi",
    "publicationDate",
    "place",
    "updatedAt",
    CANONICAL_TITLES,
    CANONICAL_ABSTRACTS,
    "languages { languageId languageCode languageRelation __typename }",
    "publications { publicationId publicationType isbn __typename }",
    (
        "contributions(order: {field: CONTRIBUTION_ORDINAL, direction: ASC}) "
        "{ contributionId contributionType fullName contributionOrdinal "
        + CANONICAL_BIOGRAPHIES +
        " __typename }"
    ),
    "subjects { subjectId subjectType subjectCode subjectOrdinal __typename }",
    "references { referenceId referenceOrdinal doi __typename }",
    "fundings { fundingId grantNumber program __typename }",
    "additionalResources { workResourceId resourceType resourceOrdinal __typename }",
    "awards { awardId awardOrdinal __typename }",
    "endorsements { endorsementId endorsementOrdinal __typename }",
    "bookReviews { bookReviewId reviewOrdinal __typename }",
    "featuredVideo { workFeaturedVideoId title __typename }",
    "imprint { imprintId imprintName " + PUBLISHER_LINK + " __typename }",
    "__typename",
]

CONTRIBUTION_FIELDS = [
    "contributionId",
    "contributorId",
    "workId",
    "contributionType",
    "mainContribution",
    "firstName",
    "lastName",
    "fullName",
    "contributionOrdinal",
    "createdAt",
    "updatedAt",
    CANONICAL_BIOGRAPHIES,
    "affiliations { affiliationId affiliationOrdinal position institution { institutionId institutionName ror __typename } __typename }",
    WORK_LINK,
    "contributor { contributorId firstName lastName fullName orcid website __typename }",
    "__typename",
]

CONTRIBUTOR_FIELDS = [
    "contributorId",
    "firstName",
    "lastName",
    "fullName",
    "orcid",
    "website",
    "createdAt",
    "updatedAt",
    "contributions { contributionId contributionType fullName contributionOrdinal __typename }",
    "__typename",
]

INSTITUTION_FIELDS = [
    "institutionId",
    "institutionName",
    "institutionDoi",
    "countryCode",
    "ror",
    "createdAt",
    "updatedAt",
    "fundings { fundingId grantNumber program projectName projectShortname __typename }",
    "affiliations { affiliationId affiliationOrdinal position __typename }",
    "__typename",
]

FUNDING_FIELDS = [
    "fundingId",
    "workId",
    "institutionId",
    "program",
    "projectName",
    "projectShortname",
    "grantNumber",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "institution { institutionId institutionName institutionDoi ror __typename }",
    "__typename",
]

IMPRINT_FIELDS = [
    "imprintId",
    "publisherId",
    "imprintName",
    "imprintUrl",
    "crossmarkDoi",
    "s3Bucket",
    "cdnDomain",
    "cloudfrontDistId",
    "defaultCurrency",
    "defaultPlace",
    "defaultLocale",
    "createdAt",
    "updatedAt",
    PUBLISHER_LINK,
    "__typename",
]

ISSUE_FIELDS = [
    "issueId",
    "workId",
    "seriesId",
    "issueOrdinal",
    "issueNumber",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "series { seriesId seriesName seriesType issnPrint issnDigital __typename }",
    "__typename",
]

LANGUAGE_FIELDS = [
    "languageId",
    "workId",
    "languageCode",
    "languageRelation",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "__typename",
]

LOCATION_FIELDS = [
    "locationId",
    "publicationId",
    "landingPage",
    "fullTextUrl",
    "locationPlatform",
    "canonical",
    "createdAt",
    "updatedAt",
    (
        "publication { publicationId publicationType isbn "
        "work { workId " + CANONICAL_TITLES + " __typename } __typename }"
    ),
    "__typename",
]

PRICE_FIELDS = [
    "priceId",
    "publicationId",
    "currencyCode",
    "unitPrice",
    "createdAt",
    "updatedAt",
    (
        "publication { publicationId publicationType isbn prices { priceId currencyCode unitPrice __typename } "
        "work { workId publicationDate place " + CANONICAL_TITLES +
        " imprint { publisher { publisherName publisherId __typename } __typename } "
        "contributions { fullName contributionType mainContribution contributionOrdinal __typename } "
        "__typename } __typename }"
    ),
    "__typename",
]

PUBLICATION_FIELDS = [
    "publicationId",
    "publicationType",
    "workId",
    "isbn",
    "widthMm: width(units: MM)",
    "widthIn: width(units: IN)",
    "heightMm: height(units: MM)",
    "heightIn: height(units: IN)",
    "depthMm: depth(units: MM)",
    "depthIn: depth(units: IN)",
    "weightG: weight(units: G)",
    "weightOz: weight(units: OZ)",
    "accessibilityStandard",
    "accessibilityAdditionalStandard",
    "accessibilityException",
    "accessibilityReportUrl",
    "createdAt",
    "updatedAt",
    "file { fileId fileType cdnUrl mimeType bytes sha256 __typename }",
    "locations { locationId landingPage fullTextUrl locationPlatform canonical __typename }",
    "prices { priceId currencyCode unitPrice __typename }",
    (
        "work { workId doi publicationDate place "
        + CANONICAL_TITLES +
        " contributions { fullName contributionType mainContribution contributionOrdinal __typename } "
        "imprint { publisher { publisherName publisherId __typename } __typename } "
        "__typename }"
    ),
    "__typename",
]

PUBLISHER_FIELDS = [
    "publisherId",
    "publisherName",
    "publisherShortname",
    "publisherUrl",
    "zitadelId",
    "accessibilityStatement",
    "accessibilityReportUrl",
    "createdAt",
    "updatedAt",
    "imprints { imprintId imprintName imprintUrl __typename }",
    "contacts { contactId contactType email __typename }",
    "__typename",
]

SERIES_FIELDS = [
    "seriesId",
    "imprintId",
    "seriesType",
    "seriesName",
    "issnPrint",
    "issnDigital",
    "seriesUrl",
    "seriesDescription",
    "seriesCfpUrl",
    "createdAt",
    "updatedAt",
    "imprint { imprintId imprintName publisher { publisherId publisherName __typename } __typename }",
    "__typename",
]

SUBJECT_FIELDS = [
    "subjectId",
    "workId",
    "subjectType",
    "subjectCode",
    "subjectOrdinal",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "__typename",
]

AFFILIATION_FIELDS = [
    "affiliationId",
    "contributionId",
    "institutionId",
    "affiliationOrdinal",
    "position",
    "createdAt",
    "updatedAt",
    "institution { institutionId institutionName ror __typename }",
    "contribution { contributionId fullName contributionType __typename }",
    "__typename",
]

REFERENCE_FIELDS = [
    "referenceId",
    "workId",
    "referenceOrdinal",
    "doi",
    "unstructuredCitation",
    "issn",
    "isbn",
    "journalTitle",
    "articleTitle",
    "seriesTitle",
    "volumeTitle",
    "edition",
    "author",
    "volume",
    "issue",
    "firstPage",
    "componentNumber",
    "standardDesignator",
    "standardsBodyName",
    "standardsBodyAcronym",
    "url",
    "publicationDate",
    "retrievalDate",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "__typename",
]

WORK_RESOURCE_FIELDS = [
    "workResourceId",
    "workId",
    "title(markupFormat: JATS_XML)",
    "description(markupFormat: JATS_XML)",
    "attribution",
    "resourceType",
    "doi",
    "handle",
    "url",
    "date",
    "resourceOrdinal",
    "createdAt",
    "updatedAt",
    "file { fileId fileType cdnUrl mimeType bytes sha256 __typename }",
    WORK_LINK,
    "__typename",
]

AWARD_FIELDS = [
    "awardId",
    "workId",
    "title(markupFormat: JATS_XML)",
    "url",
    "category",
    "year",
    "jury",
    "country",
    "role",
    "prizeStatement(markupFormat: JATS_XML)",
    "awardOrdinal",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "__typename",
]

ENDORSEMENT_FIELDS = [
    "endorsementId",
    "workId",
    "authorName",
    "authorRole",
    "authorOrcid",
    "authorInstitutionId",
    "url",
    "text(markupFormat: JATS_XML)",
    "endorsementOrdinal",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "authorInstitution { institutionId institutionName __typename }",
    "__typename",
]

BOOK_REVIEW_FIELDS = [
    "bookReviewId",
    "workId",
    "title(markupFormat: JATS_XML)",
    "authorName",
    "reviewerOrcid",
    "reviewerInstitutionId",
    "url",
    "doi",
    "reviewDate",
    "journalName",
    "journalVolume",
    "journalNumber",
    "journalIssn",
    "pageRange",
    "text(markupFormat: JATS_XML)",
    "reviewOrdinal",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "reviewerInstitution { institutionId institutionName __typename }",
    "__typename",
]

WORK_FEATURED_VIDEO_FIELDS = [
    "workFeaturedVideoId",
    "workId",
    "title",
    "url",
    "width",
    "height",
    "createdAt",
    "updatedAt",
    WORK_LINK,
    "file { fileId fileType cdnUrl mimeType bytes sha256 __typename }",
    "__typename",
]

TITLE_FIELDS = [
    "titleId",
    "workId",
    "localeCode",
    "fullTitle",
    "title",
    "subtitle",
    "canonical",
    WORK_LINK,
    "__typename",
]

ABSTRACT_FIELDS = [
    "abstractId",
    "workId",
    "localeCode",
    "content",
    "canonical",
    "abstractType",
    WORK_LINK,
    "__typename",
]

BIOGRAPHY_FIELDS = [
    "biographyId",
    "contributionId",
    "localeCode",
    "content",
    "canonical",
    "work { workId " + CANONICAL_TITLES + " __typename }",
    "contribution { contributionId fullName contributionType __typename }",
    "__typename",
]

CONTACT_FIELDS = [
    "contactId",
    "publisherId",
    "contactType",
    "email",
    "createdAt",
    "updatedAt",
    PUBLISHER_LINK,
    "__typename",
]

QUERIES = {
    "contribution": {"fields": CONTRIBUTION_FIELDS},
    "contributions": {"fields": CONTRIBUTION_FIELDS},
    "contributor": {"fields": CONTRIBUTOR_FIELDS},
    "contributors": {"fields": CONTRIBUTOR_FIELDS},
    "institution": {"fields": INSTITUTION_FIELDS},
    "institutions": {"fields": INSTITUTION_FIELDS},
    "funding": {"fields": FUNDING_FIELDS},
    "fundings": {"fields": FUNDING_FIELDS},
    "imprint": {"fields": IMPRINT_FIELDS},
    "imprints": {"fields": IMPRINT_FIELDS},
    "issue": {"fields": ISSUE_FIELDS},
    "issues": {"fields": ISSUE_FIELDS},
    "language": {"fields": LANGUAGE_FIELDS},
    "languages": {"fields": LANGUAGE_FIELDS},
    "location": {"fields": LOCATION_FIELDS},
    "locations": {"fields": LOCATION_FIELDS},
    "price": {"fields": PRICE_FIELDS},
    "prices": {"fields": PRICE_FIELDS},
    "publication": {"fields": PUBLICATION_FIELDS},
    "publications": {"fields": PUBLICATION_FIELDS},
    "publisher": {"fields": PUBLISHER_FIELDS},
    "publishers": {"fields": PUBLISHER_FIELDS},
    "series": {"fields": SERIES_FIELDS},
    "serieses": {"fields": SERIES_FIELDS},
    "subject": {"fields": SUBJECT_FIELDS},
    "subjects": {"fields": SUBJECT_FIELDS},
    "work": {"fields": WORK_FULL_FIELDS},
    "workByDoi": {"fields": WORK_FULL_FIELDS},
    "bookByDoi": {"fields": WORK_FULL_FIELDS},
    "chapterByDoi": {"fields": WORK_FULL_FIELDS},
    "works": {"fields": WORK_LIST_FIELDS},
    "books": {"fields": WORK_LIST_FIELDS},
    "chapters": {"fields": WORK_LIST_FIELDS},
    "file": {"fields": FILE_FIELDS},
    "affiliation": {"fields": AFFILIATION_FIELDS},
    "affiliations": {"fields": AFFILIATION_FIELDS},
    "reference": {"fields": REFERENCE_FIELDS},
    "references": {"fields": REFERENCE_FIELDS},
    "additionalResource": {"fields": WORK_RESOURCE_FIELDS},
    "additionalResources": {"fields": WORK_RESOURCE_FIELDS},
    "award": {"fields": AWARD_FIELDS},
    "awards": {"fields": AWARD_FIELDS},
    "endorsement": {"fields": ENDORSEMENT_FIELDS},
    "endorsements": {"fields": ENDORSEMENT_FIELDS},
    "bookReview": {"fields": BOOK_REVIEW_FIELDS},
    "bookReviews": {"fields": BOOK_REVIEW_FIELDS},
    "workFeaturedVideo": {"fields": WORK_FEATURED_VIDEO_FIELDS},
    "workFeaturedVideos": {"fields": WORK_FEATURED_VIDEO_FIELDS},
    "title": {"fields": TITLE_FIELDS},
    "titles": {"fields": TITLE_FIELDS},
    "abstract": {"fields": ABSTRACT_FIELDS},
    "abstracts": {"fields": ABSTRACT_FIELDS},
    "biography": {"fields": BIOGRAPHY_FIELDS},
    "biographies": {"fields": BIOGRAPHY_FIELDS},
    "contact": {"fields": CONTACT_FIELDS},
    "contacts": {"fields": CONTACT_FIELDS},
}
