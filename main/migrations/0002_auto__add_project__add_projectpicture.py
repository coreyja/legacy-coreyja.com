# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'main_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['Project'])

        # Adding M2M table for field pictures on 'Project'
        m2m_table_name = db.shorten_name(u'main_project_pictures')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'main.project'], null=False)),
            ('projectpicture', models.ForeignKey(orm[u'main.projectpicture'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'projectpicture_id'])

        # Adding model 'ProjectPicture'
        db.create_table(u'main_projectpicture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('is_thumbnail', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'main', ['ProjectPicture'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'main_project')

        # Removing M2M table for field pictures on 'Project'
        db.delete_table(db.shorten_name(u'main_project_pictures'))

        # Deleting model 'ProjectPicture'
        db.delete_table(u'main_projectpicture')


    models = {
        u'main.project': {
            'Meta': {'object_name': 'Project'},
            'Name': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictures': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.ProjectPicture']", 'symmetrical': 'False'})
        },
        u'main.projectpicture': {
            'Meta': {'object_name': 'ProjectPicture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_thumbnail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['main']