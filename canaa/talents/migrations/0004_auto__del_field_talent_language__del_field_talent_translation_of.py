# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Talent.language'
        db.delete_column(u'talents_talent', 'language')

        # Deleting field 'Talent.translation_of'
        db.delete_column(u'talents_talent', 'translation_of_id')


    def backwards(self, orm):
        # Adding field 'Talent.language'
        db.add_column(u'talents_talent', 'language',
                      self.gf('slim.models.fields.LanguageField')(default='pt-br', max_length=10),
                      keep_default=False)

        # Adding field 'Talent.translation_of'
        db.add_column(u'talents_talent', 'translation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['talents.Talent'], blank=True),
                      keep_default=False)


    models = {
        u'talents.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language': ('slim.models.fields.LanguageField', [], {'default': "'pt-br'", 'max_length': '10'}),
            'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'translations'", 'null': 'True', 'to': u"orm['talents.Page']"})
        },
        u'talents.talent': {
            'Meta': {'object_name': 'Talent'},
            'activies1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'activies2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'activies3': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'attach': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact1': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'contact2': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'contact3': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'courses': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_birth': ('django.db.models.fields.DateField', [], {}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'enterprise1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'enterprise2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'enterprise3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.TextField', [], {}),
            'formation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'period1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'period2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'period3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'post1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qualification': ('django.db.models.fields.TextField', [], {}),
            'referrals': ('django.db.models.fields.TextField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['talents']