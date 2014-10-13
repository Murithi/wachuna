# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PropertyMessage'
        db.create_table(u'properties_propertymessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone_number', self.gf('phonenumber_field.modelfields.PhoneNumberField')(max_length=128)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['properties.Property'])),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'property messages_create', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'property messages_update', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'properties', ['PropertyMessage'])


        # Changing field 'Property.price'
        db.alter_column(u'properties_property', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2))

    def backwards(self, orm):
        # Deleting model 'PropertyMessage'
        db.delete_table(u'properties_propertymessage')


        # Changing field 'Property.price'
        db.alter_column(u'properties_property', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'properties.city': {
            'Meta': {'object_name': 'City'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cities_create'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cities_update'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'properties.feature': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Feature'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'features_create'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'features_update'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'properties.neighbourhood': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Neighbourhood'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'neighbourhoods_create'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['properties.City']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'neighbourhoods_update'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'properties.property': {
            'Meta': {'object_name': 'Property'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'property'", 'to': u"orm['auth.User']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'properties_create'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'bathrooms': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'bedrooms': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['properties.City']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'property'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['properties.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_premium': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lot_size': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'neighbourhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['properties.Neighbourhood']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'property_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"}),
            'state': ('django_states.fields.StateField', [], {'default': "'new'", 'max_length': '100'}),
            'structure_size': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'properties_update'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'properties.propertyimage': {
            'Meta': {'unique_together': "(('property', 'file'),)", 'object_name': 'PropertyImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['properties.Property']"})
        },
        u'properties.propertymessage': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'PropertyMessage'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'property messages_create'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '128'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['properties.Property']"}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'property messages_update'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'properties.propertystatelog': {
            'Meta': {'object_name': 'PropertyStateLog'},
            'from_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'on': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'state_history'", 'to': u"orm['properties.Property']"}),
            'serialized_kwargs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'state': ('django_states.fields.StateField', [], {'default': "'transition_initiated'", 'max_length': '100'}),
            'to_state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['properties']