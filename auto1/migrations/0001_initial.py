# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServerGroup'
        db.create_table('auto1_servergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('auto1', ['ServerGroup'])

        # Adding model 'Server'
        db.create_table('auto1_server', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auto1.ServerGroup'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('auto1', ['Server'])

        # Adding model 'Project'
        db.create_table('auto1_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('repository', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('auto1', ['Project'])

        # Adding M2M table for field server on 'Project'
        db.create_table('auto1_project_server', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['auto1.project'], null=False)),
            ('server', models.ForeignKey(orm['auto1.server'], null=False))
        ))
        db.create_unique('auto1_project_server', ['project_id', 'server_id'])

        # Adding model 'Branch'
        db.create_table('auto1_branch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auto1.Project'])),
        ))
        db.send_create_signal('auto1', ['Branch'])

        # Adding model 'Task'
        db.create_table('auto1_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('auto1', ['Task'])

    def backwards(self, orm):
        # Deleting model 'ServerGroup'
        db.delete_table('auto1_servergroup')

        # Deleting model 'Server'
        db.delete_table('auto1_server')

        # Deleting model 'Project'
        db.delete_table('auto1_project')

        # Removing M2M table for field server on 'Project'
        db.delete_table('auto1_project_server')

        # Deleting model 'Branch'
        db.delete_table('auto1_branch')

        # Deleting model 'Task'
        db.delete_table('auto1_task')

    models = {
        'auto1.branch': {
            'Meta': {'object_name': 'Branch'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auto1.Project']"})
        },
        'auto1.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'repository': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'server': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auto1.Server']", 'symmetrical': 'False'})
        },
        'auto1.server': {
            'Meta': {'object_name': 'Server'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auto1.ServerGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'auto1.servergroup': {
            'Meta': {'object_name': 'ServerGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'auto1.task': {
            'Meta': {'object_name': 'Task'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['auto1']