from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from sorl.thumbnail import ImageField
from django.utils.safestring import mark_safe


class ProjectTag(models.Model):
    name = models.TextField()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(ProjectTag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Project(models.Model):

    name = models.TextField(verbose_name='Project Name')
    description = models.TextField()
    tags = models.ManyToManyField(ProjectTag, related_name="projects", blank=True, null=True)

    thumbnail = ImageField(upload_to='./project-pics/thumbnails/', blank=True, null=True)

    slug = models.SlugField(blank=True, null=True)

    #Has 'pictures' related objects from ProjectPicture model

    #Has 'links' related objects from ProjectLinks

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_url(self):
        return reverse('project', kwargs={'slug':self.slug})

    def hover_color(self):
        rem = self.id % 5

        colors = ['red', 'purple', 'green', 'orange', 'blue']

        return colors[rem]

    def get_tag_string(self):
        return ', '.join([str(x) for x in self.tags.all()])

    def get_first_picture(self):
        if self.pictures.count():
            return self.pictures.all()[0]


class ProjectPicture(models.Model):

    picture = ImageField(upload_to='./project-pics/')
    project = models.ForeignKey(Project, related_name="pictures", blank=True, null=True)

    def __unicode__(self):
        return self.picture.name


class ProjectLink(models.Model):
    LINK_TYPES = (
        ('W', 'WWW'),
        ('G', 'GitHub'),
        ('B', 'BitBucket'),
    )
    type = models.CharField(max_length=1, choices=LINK_TYPES)

    url = models.URLField()
    project = models.ForeignKey(Project, related_name="links")

    def __unicode__(self):
        return self.url

    def render(self):
        icon_html = ''

        if self.type == 'W':
            icon = 'icon-globe'
        elif self.type == 'G':
            icon = 'icon-github'
        elif self.type == 'B':
            icon = 'icon-bitbucket'
        else:
            icon = ''

        if icon:
            icon_html = '<i class="%s"></i>' % icon

        result = '<h2 class="url"><a href="%s" target="_blank">%s %s</a></h2>' % (self.url, icon_html, self.url)

        return mark_safe(result)