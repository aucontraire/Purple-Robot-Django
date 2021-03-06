# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PurpleRobotReport'
        db.create_table(u'purple_robot_app_purplerobotreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('probe', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('generated', self.gf('django.db.models.fields.DateTimeField')()),
            ('mime_type', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('report_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'purple_robot_app', ['PurpleRobotReport'])


    def backwards(self, orm):
        # Deleting model 'PurpleRobotReport'
        db.delete_table(u'purple_robot_app_purplerobotreport')


    models = {
        u'purple_robot_app.purplerobotconfiguration': {
            'Meta': {'object_name': 'PurpleRobotConfiguration'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'contents': ('django.db.models.fields.TextField', [], {'max_length': '1048576'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '1024'})
        },
        u'purple_robot_app.purplerobotevent': {
            'Meta': {'object_name': 'PurpleRobotEvent'},
            'event': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logged': ('django.db.models.fields.DateTimeField', [], {}),
            'payload': ('django.db.models.fields.TextField', [], {'max_length': '8388608', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'purple_robot_app.purplerobotpayload': {
            'Meta': {'object_name': 'PurpleRobotPayload'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'errors': ('django.db.models.fields.TextField', [], {'max_length': '65536', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payload': ('django.db.models.fields.TextField', [], {'max_length': '8388608'}),
            'process_tags': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'purple_robot_app.purplerobotreading': {
            'Meta': {'object_name': 'PurpleRobotReading'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logged': ('django.db.models.fields.DateTimeField', [], {}),
            'payload': ('django.db.models.fields.TextField', [], {'max_length': '8388608'}),
            'probe': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'purple_robot_app.purplerobotreport': {
            'Meta': {'object_name': 'PurpleRobotReport'},
            'generated': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'probe': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'report_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['purple_robot_app']