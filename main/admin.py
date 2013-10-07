from django.contrib import admin
from .models import Project, ProjectPicture, ProjectTag
from sorl.thumbnail.admin import AdminImageMixin


class ProjectPictureInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = ProjectPicture


class ProjectPictureAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('picture', 'project')
admin.site.register(ProjectPicture, ProjectPictureAdmin)


class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    exclude = ('slug', )
admin.site.register(ProjectTag, ProjectTagAdmin)


class ProjectAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [
        ProjectPictureInlineAdmin,
    ]
    exclude = ('slug', )
    list_display = ('name', 'slug', 'url', 'hover_color')
admin.site.register(Project, ProjectAdmin)