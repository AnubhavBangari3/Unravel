# Generated by Django 3.2.5 on 2022-02-07 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_alter_profile_friends'),
        ('Post', '0008_auto_20220126_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joingroup',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='Profile.profile'),
        ),
    ]