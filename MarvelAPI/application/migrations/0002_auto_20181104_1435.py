# Generated by Django 2.1.3 on 2018-11-04 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entitystat',
            old_name='metrid_id',
            new_name='metric_id',
        ),
    ]