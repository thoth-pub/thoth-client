"""
(c) ΔQ Programming LLP, 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Publisher(models.Model):
    publisher_name = models.TextField(blank=True, null=True)
    thoth_id = models.UUIDField()
    thoth_instance = models.URLField(default='https://api.thoth.pub')

    def __str__(self):
        return self.publisher_name


class BIC(models.Model):
    class Meta:
        verbose_name = _("BIC Code")
        verbose_name_plural = _("BIC Codes")
    code = models.CharField(max_length=20)
    heading = models.CharField(max_length=255)


class BISAC(models.Model):
    class Meta:
        verbose_name = _("BISAC Code")
        verbose_name_plural = _("BISAC Codes")
    code = models.CharField(max_length=20)
    heading = models.CharField(max_length=255)


class Thema(models.Model):
    class Meta:
        verbose_name = _("Thema Code")
        verbose_name_plural = _("Thema Codes")

    code = models.CharField(max_length=20)
    heading = models.CharField(max_length=255)


class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    work_type = models.CharField(max_length=255, blank=True, null=True)
    full_title = models.TextField(blank=True, null=True)
    doi = models.CharField(max_length=255, blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)
    cover_caption = models.TextField(blank=True, null=True)
    thoth_id = models.UUIDField()
    thoth_instance = models.URLField(default='https://api.thoth.pub')
    landing_page = models.URLField(default=None, null=True, blank=True)
    long_abstract = models.TextField(default='')
    short_abstract = models.TextField(default='')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  null=True)
    license = models.CharField(max_length=255, default='')
    published_date = models.CharField(max_length=255, default='n.d.')

    @property
    def thoth_export_url(self):
        return self.thoth_instance.replace('api', 'export')

    def __str__(self):
        try:
            dt = datetime.strptime(self.published_date, '%Y-%m-%d')
            return '{0} ({1}, {2})'.format(self.full_title,
                                           self.publisher,
                                           dt.year)
        except ValueError as e:
            return '{0} ({1}, {2})'.format(self.full_title,
                                           self.publisher,
                                           self.published_date)


class Subject(models.Model):
    thoth_id = models.UUIDField()
    thoth_instance = models.URLField(default='https://api.thoth.pub')
    subject_type = models.CharField(max_length=255)
    subject_ordinal = models.IntegerField(blank=True, null=True)
    subject_code = models.CharField(max_length=255)
    BIC_code = models.ForeignKey(BIC, null=True, on_delete=models.CASCADE)
    thema_code = models.ForeignKey(Thema, null=True, on_delete=models.CASCADE)
    BISAC_code = models.ForeignKey(BISAC, null=True, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

    @property
    def subject_display(self):
        if self.subject_type == "BIC" and self.BIC_code:
            return self.BIC_code.heading
        elif self.subject_type == "THEMA" and self.thema_code:
            return self.thema_code.heading
        elif self.subject_type == "BISAC" and self.BISAC_code:
            return self.BISAC_code.heading
        else:
            return self.subject_code


class Contributor(models.Model):
    contributor_id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    orcid = models.URLField(blank=True, null=True)
    thoth_id = models.UUIDField()
    thoth_instance = models.URLField(default='https://api.thoth.pub')

    def __str__(self):
        return self.full_name


class Contribution(models.Model):
    contribution_id = models.AutoField(primary_key=True)
    institution = models.TextField(blank=True, null=True)
    contribution_ordinal = models.IntegerField(blank=True, null=True)
    thoth_id = models.UUIDField()
    contribution_type = models.CharField(max_length=255, blank=True, null=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, null=True)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE,
                                    null=True)
    thoth_instance = models.URLField(default='https://api.thoth.pub')

    def __str__(self):
        if self.contributor and self.work:
            return '{0} as {1} on {2}'.format(self.contributor.full_name,
                                              self.contribution_type,
                                              self.work)
        else:
            return "Contribution"



