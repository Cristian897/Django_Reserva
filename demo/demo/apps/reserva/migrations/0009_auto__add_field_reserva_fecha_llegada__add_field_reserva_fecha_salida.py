# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'reserva.fecha_llegada'
        db.add_column(u'reserva_reserva', 'fecha_llegada',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)

        # Adding field 'reserva.fecha_salida'
        db.add_column(u'reserva_reserva', 'fecha_salida',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'reserva.fecha_llegada'
        db.delete_column(u'reserva_reserva', 'fecha_llegada')

        # Deleting field 'reserva.fecha_salida'
        db.delete_column(u'reserva_reserva', 'fecha_salida')


    models = {
        u'reserva.cliente': {
            'Meta': {'object_name': 'cliente'},
            'Telefono': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'reserva.producto': {
            'Meta': {'object_name': 'producto'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha_final': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'reserva.reserva': {
            'Meta': {'object_name': 'reserva'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha_llegada': ('django.db.models.fields.DateField', [], {}),
            'fecha_salida': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombreCasa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombreCliente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['reserva']