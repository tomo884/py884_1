# Generated by Django 3.1.2 on 2020-11-24 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='evalution',
            new_name='evaluation',
        ),
    ]
