# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActivityLog'
        db.create_table(u'activity_log_activitylog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('request_url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('response_code', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('extra_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
        ))
        db.send_create_signal(u'activity_log', ['ActivityLog'])


    def backwards(self, orm):
        # Deleting model 'ActivityLog'
        db.delete_table(u'activity_log_activitylog')


    models = {
        u'activity_log.activitylog': {
            'Meta': {'object_name': 'ActivityLog'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'extra_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'request_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'response_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['activity_log']
