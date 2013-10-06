from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


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

    thumbnail = models.ImageField(upload_to='./project-pics/thumbnails/', blank=True, null=True)
    #Has 'pictures' related objects from ProjectPicture model

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_url(self):
        return reverse('project', kwargs={'slug':self.slug})

    def get_hover_color(self):
        rem = self.id % 5

        colors = ['red', 'purple', 'green', 'orange', 'blue']

        return colors[rem]

    def get_tag_string(self):
        return ', '.join([str(x) for x in self.tags.all()])

    def get_six_pictures(self):
        return self.pictures.all()[:6]

    def get_first_picture(self):
        if self.pictures.count():
            return self.pictures.all()[0]


class ProjectPicture(models.Model):

    picture = models.ImageField(upload_to='./project-pics/')
    project = models.ForeignKey(Project, related_name="pictures", blank=True, null=True)

    def __unicode__(self):
        return self.picture.name