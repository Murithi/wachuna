# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'properties_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cities_create', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cities_update', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'properties', ['City'])

        # Adding model 'Neighbourhood'
        db.create_table(u'properties_neighbourhood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['properties.City'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'neighbourhoods_create', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'neighbourhoods_update', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'properties', ['Neighbourhood'])

        # Adding model 'Feature'
        db.create_table(u'properties_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'features_create', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'features_update', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'properties', ['Feature'])

        # Adding model 'Property'
        db.create_table(u'properties_property', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('bedrooms', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('bathrooms', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('structure_size', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('lot_size', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['properties.City'])),
            ('neighbourhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['properties.Neighbourhood'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=14, blank=True)),
            ('property_type', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='property', to=orm['auth.User'])),
            ('is_premium', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='properties_create', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='properties_update', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'properties', ['Property'])

        # Adding M2M table for field features on 'Property'
        m2m_table_name = db.shorten_name(u'properties_property_features')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('property', models.ForeignKey(orm[u'properties.property'], null=False)),
            ('feature', models.ForeignKey(orm[u'properties.feature'], null=False))
        ))
        db.create_unique(m2m_table_name, ['property_id', 'feature_id'])

        # Adding model 'PropertyImage'
        db.create_table(u'properties_propertyimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['properties.Property'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'properties', ['PropertyImage'])

        # Adding unique constraint on 'PropertyImage', fields ['property', 'file']
        db.create_unique(u'properties_propertyimage', ['property_id', 'file'])


    def backwards(self, orm):
        # Removing unique constraint on 'PropertyImage', fields ['property', 'file']
        db.delete_unique(u'properties_propertyimage', ['property_id', 'file'])

        # Deleting model 'City'
        db.delete_table(u'properties_city')

        # Deleting model 'Neighbourhood'
        db.delete_table(u'properties_neighbourhood')

        # Deleting model 'Feature'
        db.delete_table(u'properties_feature')

        # Deleting model 'Property'
        db.delete_table(u'properties_property')

        # Removing M2M table for field features on 'Property'
        db.delete_table(db.shorten_name(u'properties_property_features'))

        # Deleting model 'PropertyImage'
        db.delete_table(u'properties_propertyimage')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
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
            'bathrooms': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'neighbourhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['properties.Neighbourhood']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'property_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"}),
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
        }
    }

    complete_apps = ['properties']