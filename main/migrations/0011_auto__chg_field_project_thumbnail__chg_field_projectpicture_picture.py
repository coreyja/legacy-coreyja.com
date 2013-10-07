# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.thumbnail'
        db.alter_column(u'main_project', 'thumbnail', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True))

        # Changing field 'ProjectPicture.picture'
        db.alter_column(u'main_projectpicture', 'picture', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Project.thumbnail'
        db.alter_column(u'main_project', 'thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'ProjectPicture.picture'
        db.alter_column(u'main_projectpicture', 'picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'main.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['main.ProjectTag']"}),
            'thumbnail': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'main.projectpicture': {
            'Meta': {'object_name': 'ProjectPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pictures'", 'null': 'True', 'to': u"orm['main.Project']"})
        },
        u'main.projecttag': {
            'Meta': {'object_name': 'ProjectTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']