# Generated by Django 4.1 on 2022-11-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_finder', '0006_globaldata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam',
            name='spam',
            field=models.CharField(choices=[('n', 'NOT_SPAM'), ('s', 'SPAM')], max_length=10),
        ),
    ]
