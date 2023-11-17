# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Harvest Data(models.Model):

    #__Harvest Data_FIELDS__
    harvester_name = models.CharField(max_length=255, null=True, blank=True)
    field_id = models.CharField(max_length=255, null=True, blank=True)
    harvest_date = models.CharField(max_length=255, null=True, blank=True)

    #__Harvest Data_FIELDS__END

    class Meta:
        verbose_name        = _("Harvest Data")
        verbose_name_plural = _("Harvest Data")


class Harvester(models.Model):

    #__Harvester_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    church = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)

    #__Harvester_FIELDS__END

    class Meta:
        verbose_name        = _("Harvester")
        verbose_name_plural = _("Harvester")


class Field(models.Model):

    #__Field_FIELDS__
    link = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    owner = models.CharField(max_length=255, null=True, blank=True)

    #__Field_FIELDS__END

    class Meta:
        verbose_name        = _("Field")
        verbose_name_plural = _("Field")



#__MODELS__END
