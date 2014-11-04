# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        # # Adding model 'Page'
        # db.create_table(u'talents_page', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('content', self.gf('django.db.models.fields.TextField')()),
        #     ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        # ))
        # db.send_create_signal(u'talents', ['Page'])

        # # Adding model 'Talent'
        # db.create_table(u'talents_talent', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        #     ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
        #     ('number', self.gf('django.db.models.fields.CharField')(max_length=10)),
        #     ('complement', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('cep', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
        #     ('district', self.gf('django.db.models.fields.CharField')(max_length=100)),
        #     ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
        #     ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
        #     ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
        #     ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
        #     ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
        #     ('date_birth', self.gf('django.db.models.fields.DateField')()),
        #     ('sex', self.gf('django.db.models.fields.CharField')(max_length=10)),
        #     ('formation', self.gf('django.db.models.fields.CharField')(max_length=10)),
        #     ('qualification', self.gf('django.db.models.fields.TextField')()),
        #     ('experience', self.gf('django.db.models.fields.TextField')()),
        #     ('enterprise1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('contact1', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        #     ('period1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('post1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('activies1', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        #     ('enterprise2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('contact2', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        #     ('period2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('post2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('activies2', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        #     ('enterprise3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('contact3', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
        #     ('period3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('post3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        #     ('activies3', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        #     ('courses', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        #     ('referrals', self.gf('django.db.models.fields.TextField')()),
        #     ('attach', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        # ))
        # db.send_create_signal(u'talents', ['Talent'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'talents_page')

        # Deleting model 'Talent'
        db.delete_table(u'talents_talent')


    models = {
        u'talents.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
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
