# Generated by Django 3.1.5 on 2021-01-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('branch', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
