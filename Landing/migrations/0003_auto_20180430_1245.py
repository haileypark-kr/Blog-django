# Generated by Django 2.0.2 on 2018-04-30 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Landing', '0002_auto_20180430_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exp',
            old_name='positioon',
            new_name='position',
        ),
    ]