from django.contrib import admin
from .models import Project, ProjectPicture, ProjectTag, ProjectLink
from sorl.thumbnail.admin import AdminImageMixin


### ProjectPicture
class ProjectPictureInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = ProjectPicture


class ProjectPictureAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('picture', 'project')
admin.site.register(ProjectPicture, ProjectPictureAdmin)


### ProjectTag
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    exclude = ('slug', )
admin.site.register(ProjectTag, ProjectTagAdmin)


### ProjectLink
class ProjectLinkInlineAdmin(AdminImageMixin, admin.TabularInline):
    model = ProjectLink


class ProjectLinkAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('type', 'url', 'project')
    list_display_links = ('type', 'url')
admin.site.register(ProjectLink, ProjectLinkAdmin)

### Project
class ProjectAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [
        ProjectPictureInlineAdmin,
        ProjectLinkInlineAdmin,
    ]
    exclude = ('slug', )
    list_display = ('name', 'slug', 'hover_color')
admin.site.register(Project, ProjectAdmin)