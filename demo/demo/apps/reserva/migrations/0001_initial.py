# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'cliente'
        db.create_table(u'reserva_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mail', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Telefono', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'reserva', ['cliente'])

        # Adding model 'producto'
        db.create_table(u'reserva_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('stock', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'reserva', ['producto'])

        # Adding model 'reserva'
        db.create_table(u'reserva_reserva', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreCasa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombreCliente', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'reserva', ['reserva'])


    def backwards(self, orm):
        # Deleting model 'cliente'
        db.delete_table(u'reserva_cliente')

        # Deleting model 'producto'
        db.delete_table(u'reserva_producto')

        # Deleting model 'reserva'
        db.delete_table(u'reserva_reserva')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'stock': ('django.db.models.fields.IntegerField', [], {})
        },
        u'reserva.reserva': {
            'Meta': {'object_name': 'reserva'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombreCasa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombreCliente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        }
    }

    complete_apps = ['reserva']