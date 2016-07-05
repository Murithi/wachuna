# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='state',
            field=django_fsm.FSMField(default=b'new', max_length=50, choices=[(b'new', b'New'), (b'features_added', b'Features Added'), (b'images_added', b'Images Added'), (b'awaiting_admin_approval', b'Awaiting Admin Approval'), (b'published', b'Published'), (b'inactive', b'Inactive')]),
            preserve_default=True,
        ),
    ]
