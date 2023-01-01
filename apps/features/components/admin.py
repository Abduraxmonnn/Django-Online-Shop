# Django
from django.contrib import admin

# Project
from apps.features.components.models import Cpu, VideoCart


admin.site.register(Cpu)
admin.site.register(VideoCart)
