# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        # # Adding model 'ProductGroup'
        # db.create_table(u'catalog_productgroup', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        #     ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        #     ('description', self.gf('django.db.models.fields.CharField')(max_length=125)),
        #     ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        #     ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        # ))
        # db.send_create_signal(u'catalog', ['ProductGroup'])

        # # Adding model 'Product'
        # db.create_table(u'catalog_product', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('product_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.ProductGroup'])),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        #     ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        #     ('description', self.gf('django.db.models.fields.TextField')(max_length=250)),
        #     ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        #     ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        # ))
        # db.send_create_signal(u'catalog', ['Product'])

        # # Adding model 'ProductInfo'
        # db.create_table(u'catalog_productinfo', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('product_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.ProductGroup'])),
        #     ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.Product'])),
        #     ('description', self.gf('django.db.models.fields.IntegerField')()),
        #     ('amount', self.gf('django.db.models.fields.CharField')(max_length=30)),
        #     ('value', self.gf('django.db.models.fields.CharField')(default='**', max_length=2)),
        #     ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        # ))
        # db.send_create_signal(u'catalog', ['ProductInfo'])


    def backwards(self, orm):
        # Deleting model 'ProductGroup'
        db.delete_table(u'catalog_productgroup')

        # Deleting model 'Product'
        db.delete_table(u'catalog_product')

        # Deleting model 'ProductInfo'
        db.delete_table(u'catalog_productinfo')


    models = {
        u'catalog.product': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'product_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.ProductGroup']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'catalog.productgroup': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ProductGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'catalog.productinfo': {
            'Meta': {'object_name': 'ProductInfo'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Product']"}),
            'product_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.ProductGroup']"}),
            'value': ('django.db.models.fields.CharField', [], {'default': "'**'", 'max_length': '2'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['catalog']
