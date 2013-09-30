from django.contrib import admin
from .models import Project, ProjectPicture, ProjectTag

admin.site.register(Project)

admin.site.register(ProjectPicture)

admin.site.register(ProjectTag)