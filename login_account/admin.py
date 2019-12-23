# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile, Post

admin.register(UserProfile, Post)(admin.ModelAdmin)
# Register your models here.
