# Generated by Django 4.1 on 2022-11-21 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spam_finder', '0007_alter_spam_spam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globaldata',
            name='contacts',
        ),
    ]