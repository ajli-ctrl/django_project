# Generated by Django 3.1.4 on 2021-01-07 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollform', '0002_auto_20210105_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='form',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='responses',
            name='responder',
        ),
        migrations.RemoveField(
            model_name='responses',
            name='response',
        ),
        migrations.RemoveField(
            model_name='responses',
            name='response_to',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
        migrations.DeleteModel(
            name='Form',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Responses',
        ),
    ]
