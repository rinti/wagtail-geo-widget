# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtailgeowidget.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('geopage', '0006_geostreampage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassicGeoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='geostreampage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('map', wagtailgeowidget.blocks.GeoBlock()), ('map_struct', wagtail.wagtailcore.blocks.StructBlock([('address', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('map', wagtailgeowidget.blocks.GeoBlock(address_field='address'))], icon='user'))]),
        ),
    ]