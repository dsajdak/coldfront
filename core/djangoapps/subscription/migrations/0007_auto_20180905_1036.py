# Generated by Django 2.1 on 2018-09-05 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0006_auto_20180905_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriptionusermessage',
            old_name='Message',
            new_name='message',
        ),
    ]
