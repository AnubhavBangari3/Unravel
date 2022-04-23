# Generated by Django 3.2.5 on 2022-02-07 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_alter_profile_friends'),
        ('Post', '0011_alter_joingroup_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joingroup',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='Profile.profile'),
        ),
    ]
