# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from application.models import Hero, Villain, EntityStat

admin.site.register(Hero)
admin.site.register(Villain)
admin.site.register(EntityStat)
