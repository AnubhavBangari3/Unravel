# Generated by Django 3.2.5 on 2022-04-14 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['created']},
        ),
    ]
