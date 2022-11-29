# Generated by Django 4.1 on 2022-11-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_finder', '0004_contacts_delete_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone_number', models.IntegerField()),
                ('spam', models.CharField(default='SPAM', max_length=255)),
            ],
        ),
    ]
