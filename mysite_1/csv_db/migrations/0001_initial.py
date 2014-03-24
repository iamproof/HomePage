# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CountryList'
        db.create_table('csv_db_countrylist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Common_Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Formal_Name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Type', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('Sub_Type', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('Sovereignty', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('Capital', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('Currency_Code', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('Currency_Name', self.gf('django.db.models.fields.CharField')(default=None, max_length=50)),
            ('Telephone_Code', self.gf('django.db.models.fields.CharField')(default=None, max_length=10)),
            ('Letter_Code', self.gf('django.db.models.fields.CharField')(default=None, max_length=10)),
            ('ISO_Number', self.gf('django.db.models.fields.CharField')(default=None, max_length=10)),
            ('Country_Code_TLD', self.gf('django.db.models.fields.CharField')(default=None, max_length=5)),
        ))
        db.send_create_signal('csv_db', ['CountryList'])


    def backwards(self, orm):
        # Deleting model 'CountryList'
        db.delete_table('csv_db_countrylist')


    models = {
        'csv_db.countrylist': {
            'Capital': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'Common_Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Country_Code_TLD': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '5'}),
            'Currency_Code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'Currency_Name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'Formal_Name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ISO_Number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10'}),
            'Letter_Code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10'}),
            'Meta': {'object_name': 'CountryList'},
            'Sovereignty': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'Sub_Type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'Telephone_Code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10'}),
            'Type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['csv_db']