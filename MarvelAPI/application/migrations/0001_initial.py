# Generated by Django 2.1.3 on 2018-11-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntityStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_id', models.IntegerField()),
                ('metrid_id', models.CharField(max_length=100)),
                ('year', models.IntegerField(null=True)),
                ('value', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('identity', models.CharField(max_length=100, null=True)),
                ('align', models.CharField(max_length=100, null=True)),
                ('eye', models.CharField(max_length=100, null=True)),
                ('hair', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(max_length=100, null=True)),
                ('alive', models.CharField(max_length=100, null=True)),
                ('first_appearance', models.CharField(max_length=100, null=True)),
                ('year', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Villain',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('identity', models.CharField(max_length=100, null=True)),
                ('align', models.CharField(max_length=100, null=True)),
                ('eye', models.CharField(max_length=100, null=True)),
                ('hair', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(max_length=100, null=True)),
                ('alive', models.CharField(max_length=100, null=True)),
                ('first_appearance', models.CharField(max_length=100, null=True)),
                ('year', models.IntegerField(null=True)),
                ('at_large', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
