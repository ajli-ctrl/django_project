# Generated by Django 3.1.4 on 2020-12-23 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primer', '0002_auto_20201223_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadprimer',
            old_name='upload_date',
            new_name='excel_date',
        ),
        migrations.RenameField(
            model_name='uploadprimer',
            old_name='upload_file',
            new_name='excel_file',
        ),
    ]