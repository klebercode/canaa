# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.language'
        db.add_column(u'catalog_product', 'language',
                      self.gf('slim.models.fields.LanguageField')(default='pt-br', max_length=10),
                      keep_default=False)

        # Adding field 'Product.translation_of'
        db.add_column(u'catalog_product', 'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='translations', null=True, to=orm['catalog.Product']),
                      keep_default=False)

        # Adding field 'ProductGroup.language'
        db.add_column(u'catalog_productgroup', 'language',
                      self.gf('slim.models.fields.LanguageField')(default='pt-br', max_length=10),
                      keep_default=False)

        # Adding field 'ProductGroup.translation_of'
        db.add_column(u'catalog_productgroup', 'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='translations', null=True, to=orm['catalog.ProductGroup']),
                      keep_default=False)

        # Adding field 'ProductInfo.language'
        db.add_column(u'catalog_productinfo', 'language',
                      self.gf('slim.models.fields.LanguageField')(default='pt-br', max_length=10),
                      keep_default=False)

        # Adding field 'ProductInfo.translation_of'
        db.add_column(u'catalog_productinfo', 'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='translations', null=True, to=orm['catalog.ProductInfo']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.language'
        db.delete_column(u'catalog_product', 'language')

        # Deleting field 'Product.translation_of'
        db.delete_column(u'catalog_product', 'translation_of_id')

        # Deleting field 'ProductGroup.language'
        db.delete_column(u'catalog_productgroup', 'language')

        # Deleting field 'ProductGroup.translation_of'
        db.delete_column(u'catalog_productgroup', 'translation_of_id')

        # Deleting field 'ProductInfo.language'
        db.delete_column(u'catalog_productinfo', 'language')

        # Deleting field 'ProductInfo.translation_of'
        db.delete_column(u'catalog_productinfo', 'translation_of_id')


    models = {
        u'catalog.product': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Product'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'language': ('slim.models.fields.LanguageField', [], {'default': "'pt-br'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'product_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.ProductGroup']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['catalog.Product']"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'catalog.productgroup': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ProductGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'language': ('slim.models.fields.LanguageField', [], {'default': "'pt-br'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['catalog.ProductGroup']"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'catalog.productinfo': {
            'Meta': {'object_name': 'ProductInfo'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('slim.models.fields.LanguageField', [], {'default': "'pt-br'", 'max_length': '10'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.Product']"}),
            'product_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalog.ProductGroup']"}),
            'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['catalog.ProductInfo']"}),
            'value': ('django.db.models.fields.CharField', [], {'default': "'**'", 'max_length': '2'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['catalog']