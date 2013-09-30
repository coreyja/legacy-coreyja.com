# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.thumbnail'
        db.add_column(u'main_project', 'thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ProjectPicture.is_thumbnail'
        db.delete_column(u'main_projectpicture', 'is_thumbnail')


    def backwards(self, orm):
        # Deleting field 'Project.thumbnail'
        db.delete_column(u'main_project', 'thumbnail')

        # Adding field 'ProjectPicture.is_thumbnail'
        db.add_column(u'main_projectpicture', 'is_thumbnail',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        u'main.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'pictures': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['main.ProjectPicture']"}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['main.ProjectTag']"}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.projectpicture': {
            'Meta': {'object_name': 'ProjectPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'main.projecttag': {
            'Meta': {'object_name': 'ProjectTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']