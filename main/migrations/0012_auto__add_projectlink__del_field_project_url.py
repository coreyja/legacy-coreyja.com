# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectLink'
        db.create_table(u'main_projectlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links', to=orm['main.Project'])),
        ))
        db.send_create_signal(u'main', ['ProjectLink'])

        # Deleting field 'Project.url'
        db.delete_column(u'main_project', 'url')


    def backwards(self, orm):
        # Deleting model 'ProjectLink'
        db.delete_table(u'main_projectlink')

        # Adding field 'Project.url'
        db.add_column(u'main_project', 'url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    models = {
        u'main.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['main.ProjectTag']"}),
            'thumbnail': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.projectlink': {
            'Meta': {'object_name': 'ProjectLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': u"orm['main.Project']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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