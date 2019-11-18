# Generated by Django 2.2.7 on 2019-11-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poli_name', models.CharField(max_length=500)),
                ('job', models.CharField(max_length=500)),
                ('region', models.CharField(max_length=500)),
                ('comments', models.TextField()),
                ('commentslikes', models.TextField()),
                ('commentsdislikes', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Politicians',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_name', models.CharField(max_length=500)),
                ('authority', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Regions',
            },
        ),
    ]