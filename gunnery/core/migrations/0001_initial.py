# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'core_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'core', ['Department'])

        # Adding model 'Application'
        db.create_table(u'core_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(related_name='applications', to=orm['core.Department'])),
        ))
        db.send_create_signal(u'core', ['Application'])

        # Adding unique constraint on 'Application', fields ['department', 'name']
        db.create_unique(u'core_application', ['department_id', 'name'])

        # Adding model 'Environment'
        db.create_table(u'core_environment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='environments', to=orm['core.Application'])),
            ('is_production', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'core', ['Environment'])

        # Adding unique constraint on 'Environment', fields ['application', 'name']
        db.create_unique(u'core_environment', ['application_id', 'name'])

        # Adding model 'ServerRole'
        db.create_table(u'core_serverrole', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(related_name='serverroles', to=orm['core.Department'])),
        ))
        db.send_create_signal(u'core', ['ServerRole'])

        # Adding unique constraint on 'ServerRole', fields ['department', 'name']
        db.create_unique(u'core_serverrole', ['department_id', 'name'])

        # Adding model 'Server'
        db.create_table(u'core_server', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default=22)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('environment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='servers', to=orm['core.Environment'])),
            ('method', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'core', ['Server'])

        # Adding unique constraint on 'Server', fields ['environment', 'name']
        db.create_unique(u'core_server', ['environment_id', 'name'])

        # Adding M2M table for field roles on 'Server'
        m2m_table_name = db.shorten_name(u'core_server_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('server', models.ForeignKey(orm[u'core.server'], null=False)),
            ('serverrole', models.ForeignKey(orm[u'core.serverrole'], null=False))
        ))
        db.create_unique(m2m_table_name, ['server_id', 'serverrole_id'])

        # Adding model 'ServerAuthentication'
        db.create_table(u'core_serverauthentication', (
            ('server', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Server'], unique=True, primary_key=True)),
            ('password', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['ServerAuthentication'])


    def backwards(self, orm):
        # Removing unique constraint on 'Server', fields ['environment', 'name']
        db.delete_unique(u'core_server', ['environment_id', 'name'])

        # Removing unique constraint on 'ServerRole', fields ['department', 'name']
        db.delete_unique(u'core_serverrole', ['department_id', 'name'])

        # Removing unique constraint on 'Environment', fields ['application', 'name']
        db.delete_unique(u'core_environment', ['application_id', 'name'])

        # Removing unique constraint on 'Application', fields ['department', 'name']
        db.delete_unique(u'core_application', ['department_id', 'name'])

        # Deleting model 'Department'
        db.delete_table(u'core_department')

        # Deleting model 'Application'
        db.delete_table(u'core_application')

        # Deleting model 'Environment'
        db.delete_table(u'core_environment')

        # Deleting model 'ServerRole'
        db.delete_table(u'core_serverrole')

        # Deleting model 'Server'
        db.delete_table(u'core_server')

        # Removing M2M table for field roles on 'Server'
        db.delete_table(db.shorten_name(u'core_server_roles'))

        # Deleting model 'ServerAuthentication'
        db.delete_table(u'core_serverauthentication')


    models = {
        u'core.application': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('department', 'name'),)", 'object_name': 'Application'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['core.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'core.department': {
            'Meta': {'ordering': "['name']", 'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'core.environment': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('application', 'name'),)", 'object_name': 'Environment'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'environments'", 'to': u"orm['core.Application']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_production': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'core.server': {
            'Meta': {'ordering': "['name']", 'unique_together': "(('environment', 'name'),)", 'object_name': 'Server'},
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'servers'", 'to': u"orm['core.Environment']"}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '22'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'servers'", 'symmetrical': 'False', 'to': u"orm['core.ServerRole']"}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'core.serverauthentication': {
            'Meta': {'object_name': 'ServerAuthentication'},
            'password': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'server': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Server']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.serverrole': {
            'Meta': {'unique_together': "(('department', 'name'),)", 'object_name': 'ServerRole'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'serverroles'", 'to': u"orm['core.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['core']