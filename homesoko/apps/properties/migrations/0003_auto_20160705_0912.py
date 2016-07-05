# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import homesoko.apps.properties.models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyDocuments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('document', models.FileField(upload_to=homesoko.apps.properties.models.get_upload_file_name, max_length=255, verbose_name=b'document')),
                ('caption', models.CharField(max_length=200, null=True, verbose_name='Caption', blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('property', models.ForeignKey(related_name='documents', verbose_name='Property', to='properties.Property')),
            ],
            options={
                'verbose_name': 'Property Document',
                'verbose_name_plural': 'Property Documents',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='propertydocuments',
            unique_together=set([('property', 'document')]),
        ),
    ]
