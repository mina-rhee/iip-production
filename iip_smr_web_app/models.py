# -*- coding: utf-8 -*-

import datetime, glob, json, logging, os, pprint, random, subprocess, time
from django.db import models
# from django.utils.encoding import smart_unicode


log = logging.getLogger(__name__)


## django-model class ##

class StaticPage( models.Model ):
    slug = models.SlugField( max_length=100 )
    title_header = models.CharField( blank=True, max_length=100 )  # for page's html->head->title
    title = models.CharField( blank=True, max_length=100 )  # title as displayed within webapge
    content = models.TextField( blank=True, help_text='Markdown allowed.' )
    def __unicode__(self):
        return self.slug
    class Meta:
        verbose_name_plural = 'Static Pages'


## eof