# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table(u'account_customuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('timezone', self.gf('timezone_field.fields.TimeZoneField')(default='UTC')),
        ))
        db.send_create_signal(u'account', ['CustomUser'])

        # Adding M2M table for field groups on 'CustomUser'
        m2m_table_name = db.shorten_name(u'account_customuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'account.customuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CustomUser'
        m2m_table_name = db.shorten_name(u'account_customuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'account.customuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'permission_id'])

        # Adding model 'DepartmentGroup'
        db.create_table(u'account_departmentgroup', (
            (u'group_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.Group'], unique=True, primary_key=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groups', to=orm['core.Department'])),
            ('local_name', self.gf('django.db.models.fields.CharField')(max_length=124)),
            ('system_name', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal(u'account', ['DepartmentGroup'])


    def backwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table(u'account_customuser')

        # Removing M2M table for field groups on 'CustomUser'
        db.delete_table(db.shorten_name(u'account_customuser_groups'))

        # Removing M2M table for field user_permissions on 'CustomUser'
        db.delete_table(db.shorten_name(u'account_customuser_user_permissions'))

        # Deleting model 'DepartmentGroup'
        db.delete_table(u'account_departmentgroup')


    models = {
        u'account.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'timezone': ('timezone_field.fields.TimeZoneField', [], {'default': "'UTC'"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'account.departmentgroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'DepartmentGroup', '_ormbases': [u'auth.Group']},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': u"orm['core.Department']"}),
            u'group_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Group']", 'unique': 'True', 'primary_key': 'True'}),
            'local_name': ('django.db.models.fields.CharField', [], {'max_length': '124'}),
            'system_name': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.department': {
            'Meta': {'ordering': "['name']", 'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['account']