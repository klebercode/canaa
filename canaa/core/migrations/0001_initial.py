# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        # # Adding model 'Customer'
        # db.create_table(u'core_customer', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        #     ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        #     ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        # ))
        # db.send_create_signal(u'core', ['Customer'])

        # # Adding model 'Institutional'
        # db.create_table(u'core_institutional', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('area', self.gf('django.db.models.fields.IntegerField')()),
        #     ('content', self.gf('django.db.models.fields.TextField')()),
        #     ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        # ))
        # db.send_create_signal(u'core', ['Institutional'])

        # # Adding model 'Step'
        # db.create_table(u'core_step', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('icon', self.gf('django.db.models.fields.CharField')(max_length=20)),
        #     ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
        #     ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        #     ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        # ))
        # db.send_create_signal(u'core', ['Step'])

        # # Adding model 'Banner'
        # db.create_table(u'core_banner', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('type', self.gf('django.db.models.fields.IntegerField')(default=1)),
        #     ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        #     ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        #     ('text', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('label', self.gf('django.db.models.fields.CharField')(max_length=40)),
        #     ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
        #     ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        # ))
        # db.send_create_signal(u'core', ['Banner'])

        # # Adding model 'Enterprise'
        # db.create_table(u'core_enterprise', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        #     ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=20)),
        #     ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
        #     ('number', self.gf('django.db.models.fields.CharField')(max_length=10)),
        #     ('complement', self.gf('django.db.models.fields.CharField')(max_length=100)),
        #     ('cep', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
        #     ('district', self.gf('django.db.models.fields.CharField')(max_length=100)),
        #     ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
        #     ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        #     ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
        #     ('phone1', self.gf('django.db.models.fields.CharField')(max_length=20)),
        #     ('phone2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        #     ('phone3', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        #     ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        # ))
        # db.send_create_signal(u'core', ['Enterprise'])

        # # Adding model 'Sale'
        # db.create_table(u'core_sale', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('content', self.gf('django.db.models.fields.TextField')()),
        #     ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        # ))
        # db.send_create_signal(u'core', ['Sale'])

        # # Adding model 'Seller'
        # db.create_table(u'core_seller', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('type', self.gf('django.db.models.fields.IntegerField')()),
        #     ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        #     ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
        #     ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
        #     ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        #     ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        #     ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        # ))
        # db.send_create_signal(u'core', ['Seller'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'core_customer')

        # Deleting model 'Institutional'
        db.delete_table(u'core_institutional')

        # Deleting model 'Step'
        db.delete_table(u'core_step')

        # Deleting model 'Banner'
        db.delete_table(u'core_banner')

        # Deleting model 'Enterprise'
        db.delete_table(u'core_enterprise')

        # Deleting model 'Sale'
        db.delete_table(u'core_sale')

        # Deleting model 'Seller'
        db.delete_table(u'core_seller')


    models = {
        u'core.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'core.customer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Customer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'core.enterprise': {
            'Meta': {'object_name': 'Enterprise'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone3': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'core.institutional': {
            'Meta': {'object_name': 'Institutional'},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'core.sale': {
            'Meta': {'object_name': 'Sale'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'core.seller': {
            'Meta': {'ordering': "('name', 'state', 'type')", 'object_name': 'Seller'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'core.step': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Step'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['core']
