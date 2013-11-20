# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserData'
        db.create_table(u'userdata_userdata', (
            ('eeid', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('legal_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('manager', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('l1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('l2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('l3', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('hire_date', self.gf('django.db.models.fields.DateField')()),
            ('job_code', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'userdata', ['UserData'])

        # Adding model 'TrainingData'
        db.create_table(u'userdata_trainingdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uname', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userdata.UserData'])),
            ('lp_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('item_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('item_status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('item_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hire_date', self.gf('django.db.models.fields.DateField')()),
            ('due_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'userdata', ['TrainingData'])


    def backwards(self, orm):
        # Deleting model 'UserData'
        db.delete_table(u'userdata_userdata')

        # Deleting model 'TrainingData'
        db.delete_table(u'userdata_trainingdata')


    models = {
        u'userdata.trainingdata': {
            'Meta': {'object_name': 'TrainingData'},
            'due_date': ('django.db.models.fields.DateField', [], {}),
            'hire_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'item_status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userdata.UserData']"})
        },
        u'userdata.userdata': {
            'Meta': {'object_name': 'UserData'},
            'eeid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hire_date': ('django.db.models.fields.DateField', [], {}),
            'job_code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'l1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'l2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'l3': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'legal_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'manager': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'})
        }
    }

    complete_apps = ['userdata']