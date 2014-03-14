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

        # Adding model 'SokoProperty'
        db.create_table(u'properties_sokoproperty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('bedroom', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('bathroom', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=2, decimal_places=2, blank=True)),
            ('structure_size', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('lot_size', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=12, decimal_places=2, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['properties.City'])),
            ('neighbourhood', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['properties.Neighbourhood'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'soko propertys_create', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'soko propertys_update', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'properties', ['SokoProperty'])

        # Adding model 'Features'
        db.create_table(u'properties_features', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'featuress_create', null=True, to=orm['auth.User'])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'featuress_update', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'properties', ['Features'])

        # Adding M2M table for field soko_property on 'Features'
        m2m_table_name = db.shorten_name(u'properties_features_soko_property')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('features', models.ForeignKey(orm[u'properties.features'], null=False)),
            ('sokoproperty', models.ForeignKey(orm[u'properties.sokoproperty'], null=False))
        ))
        db.create_unique(m2m_table_name, ['features_id', 'sokoproperty_id'])

        # Adding model 'PropertyImage'
        db.create_table(u'properties_propertyimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('soko_property', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['properties.SokoProperty'])),
            ('original', self.gf('django.db.models.fields.files.ImageField')(max_length=255)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('display_order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'properties', ['PropertyImage'])

        # Adding unique constraint on 'PropertyImage', fields ['soko_property', 'display_order']
        db.create_unique(u'properties_propertyimage', ['soko_property_id', 'display_order'])


    def backwards(self, orm):
        # Removing unique constraint on 'PropertyImage', fields ['soko_property', 'display_order']
        db.delete_unique(u'properties_propertyimage', ['soko_property_id', 'display_order'])

        # Deleting model 'City'
        db.delete_table(u'properties_city')

        # Deleting model 'Neighbourhood'
        db.delete_table(u'properties_neighbourhood')

        # Deleting model 'SokoProperty'
        db.delete_table(u'properties_sokoproperty')

        # Deleting model 'Features'
        db.delete_table(u'properties_features')

        # Removing M2M table for field soko_property on 'Features'
        db.delete_table(db.shorten_name(u'properties_features_soko_property'))

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
        u'properties.features': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Features'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'featuress_create'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'soko_property': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'feature'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['properties.SokoProperty']"}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'featuress_update'", 'null': 'True', 'to': u"orm['auth.User']"})
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
        u'properties.propertyimage': {
            'Meta': {'ordering': "['display_order']", 'unique_together': "(('soko_property', 'display_order'),)", 'object_name': 'PropertyImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'original': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'soko_property': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['properties.SokoProperty']"})
        },
        u'properties.sokoproperty': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'SokoProperty'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'soko propertys_create'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'bathroom': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '2', 'blank': 'True'}),
            'bedroom': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['properties.City']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lot_size': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '12', 'decimal_places': '2', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'neighbourhood': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['properties.Neighbourhood']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'}),
            'structure_size': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'soko propertys_update'", 'null': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['properties']