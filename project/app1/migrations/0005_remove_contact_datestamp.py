# Generated by Django 4.0.1 on 2022-01-20 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_contact_datestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='datestamp',
        ),
    ]
