# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Step.language'
        db.add_column(u'core_step', 'language',
                      self.gf('slim.models.fields.LanguageField')(default='pt-br', max_length=10),
                      keep_default=False)

        # Adding field 'Step.translation_of'
        db.add_column(u'core_step', 'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='translations', null=True, to=orm['core.Step']),
                      keep_default=False)

        # Adding field 'Banner.language'
        db.add_column(u'core_banner', 'language',
                      self.gf('slim.models.fields.LanguageField')(default='pt-br', max_length=10),
                      keep_default=False)

        # Adding field 'Banner.translation_of'
        db.add_column(u'core_banner', 'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='translations', null=True, to=orm['core.Banner']),
                      keep_default=False)

        # Adding field 'Sale.language'
        db.add_column(u'core_sale', 'language',
                      self.gf('slim.models.fields.LanguageField')(default='pt-br', max_length=10),
                      keep_default=False)

        # Adding field 'Sale.translation_of'
        db.add_column(u'core_sale', 'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='translations', null=True, to=orm['core.Sale']),
                      keep_default=False)

        # Adding field 'Institutional.language'
        db.add_column(u'core_institutional', 'language',
                      self.gf('slim.models.fields.LanguageField')(default='pt-br', max_length=10),
                      keep_default=False)

        # Adding field 'Institutional.translation_of'
        db.add_column(u'core_institutional', 'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='translations', null=True, to=orm['core.Institutional']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Step.language'
        db.delete_column(u'core_step', 'language')

        # Deleting field 'Step.translation_of'
        db.delete_column(u'core_step', 'translation_of_id')

        # Deleting field 'Banner.language'
        db.delete_column(u'core_banner', 'language')

        # Deleting field 'Banner.translation_of'
        db.delete_column(u'core_banner', 'translation_of_id')

        # Deleting field 'Sale.language'
        db.delete_column(u'core_sale', 'language')

        # Deleting field 'Sale.translation_of'
        db.delete_column(u'core_sale', 'translation_of_id')

        # Deleting field 'Institutional.language'
        db.delete_column(u'core_institutional', 'language')

        # Deleting field 'Institutional.translation_of'
        db.delete_column(u'core_institutional', 'translation_of_id')


    models = {
        u'core.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'language': ('slim.models.fields.LanguageField', [], {'default': "'pt-br'", 'max_length': '10'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['core.Banner']"}),
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language': ('slim.models.fields.LanguageField', [], {'default': "'pt-br'", 'max_length': '10'}),
            'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['core.Institutional']"})
        },
        u'core.sale': {
            'Meta': {'object_name': 'Sale'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language': ('slim.models.fields.LanguageField', [], {'default': "'pt-br'", 'max_length': '10'}),
            'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['core.Sale']"})
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
            'language': ('slim.models.fields.LanguageField', [], {'default': "'pt-br'", 'max_length': '10'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['core.Step']"})
        }
    }

    complete_apps = ['core']