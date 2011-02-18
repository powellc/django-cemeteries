from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from django.db import models

import urllib
import settings

class Cemetery(TimeStampedModel):
    """Cemetery model."""
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique=True)
    town = models.CharField(_('town'), max_length=100)

    class Meta:
        verbose_name = _('cemetery')
        verbose_name_plural = _('cemeteries')
        ordering = ('title',)

    def __unicode__(self):
        return u'%s in %s' % (self.title, self.town)

    @models.permalink
    def get_absolute_url(self):
        return u'cemeteries/%s/' % (self.slug)


class Monument(TimeStampedModel):
    """Monument model."""
    cemetery=models.ForeignKey(Cemetery)
    last_name = models.CharField(_('last name'), max_length=100)
    full_name = models.CharField(_('full name'), max_length=255, blank=True, null=True)
    slug = models.SlugField(_('slug'))
    dob = models.IntegerField(_('D.O.B.'), blank=True, null=True, max_length=4)
    dod = models.IntegerField(_('D.O.D.'), blank=True, null=True, max_length=4)
    grave_lot = models.CharField(_('grave lot'), blank=True, null=True, max_length=10)
    grave_section = models.CharField(_('grave section'), blank=True, null=True, max_length=2)
    grave_display_name=models.CharField(_('grave display name'), blank=True, null=True, max_length=255)
    stone=models.BooleanField(_('grave stone?'), default=True) 
    stone_name=models.CharField(_('stone name'), blank=True, null=True, max_length=255)
    stone_lot = models.CharField(_('stone lot'), blank=True, null=True, max_length=10)
    stone_section = models.CharField(_('stone section'), blank=True, null=True, max_length=2)
    stone_photo_content=models.CharField(_('stone_surface_content'), blank=True, null=True, max_length=255)
    stone_photo=models.ImageField(_('stone photo'), upload_to='stones/', blank=True, null=True)
    stone_surface_transcription=models.TextField(_('stone surface transcription'), blank=True, null=True) 

    class Meta:
        verbose_name = _('monument')
        verbose_name_plural = _('monument')
        ordering = ('cemetery', 'last_name',)

    def __unicode__(self):
        return u'%s (%s) in %s' % (self.last_name, self.full_name, self.cemetery)

    @models.permalink
    def get_absolute_url(self):
        return u'%s/monuments/%s/' % (self.cemetery.slug, self.slug)

