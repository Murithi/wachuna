# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import autoslug.fields
import django.utils.timezone
from django.conf import settings
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=50)),
                ('author', models.ForeignKey(related_name='cities_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='cities_update', verbose_name='last_updated_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=30)),
                ('author', models.ForeignKey(related_name='features_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='features_update', verbose_name='last_updated_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=20)),
                ('author', models.ForeignKey(related_name='neighbourhoods_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('city', models.ForeignKey(to='properties.City')),
                ('updated_by', models.ForeignKey(related_name='neighbourhoods_update', verbose_name='last_updated_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('bedrooms', models.IntegerField(blank=True, max_length=5, null=True, choices=[(1, b'1'), (1, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15')])),
                ('bathrooms', models.CharField(blank=True, max_length=15, null=True, choices=[(b'all_ensuite', b'All Ensuite'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')])),
                ('structure_size', models.PositiveIntegerField(help_text=b'Size of the structure in square feet', null=True, blank=True)),
                ('lot_size', models.DecimalField(help_text=b'Size of the lot in acres', null=True, max_digits=10, decimal_places=2, blank=True)),
                ('category', models.CharField(blank=True, max_length=14, choices=[(b'letting', b'Letting'), (b'sale', b'For Sale')])),
                ('property_type', models.CharField(blank=True, max_length=20, choices=[(b'apartment', b'Apartment'), (b'house', b'House'), (b'office', b'Office'), (b'land', b'Land'), (b'townhouse', b'Townhouse')])),
                ('is_premium', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('agency', models.ForeignKey(related_name='property', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(related_name='properties_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('city', models.ForeignKey(to='properties.City')),
                ('features', models.ManyToManyField(related_name='property', null=True, to='properties.Feature', blank=True)),
                ('neighbourhood', models.ForeignKey(to='properties.Neighbourhood')),
                ('updated_by', models.ForeignKey(related_name='properties_update', verbose_name='last_updated_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('file', models.ImageField(upload_to=b'images', max_length=255, verbose_name=b'File')),
                ('caption', models.CharField(max_length=200, null=True, verbose_name='Caption', blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('property', models.ForeignKey(related_name='images', verbose_name='Property', to='properties.Property')),
            ],
            options={
                'verbose_name': 'Property Image',
                'verbose_name_plural': 'Property Images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PropertyMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('message', models.TextField()),
                ('sent', models.BooleanField(default=False)),
                ('author', models.ForeignKey(related_name='property messages_create', verbose_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('property', models.ForeignKey(to='properties.Property')),
                ('updated_by', models.ForeignKey(related_name='property messages_update', verbose_name='last_updated_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='propertyimage',
            unique_together=set([('property', 'file')]),
        ),
    ]
