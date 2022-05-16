# Generated by Django 3.2.5 on 2022-04-30 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_alter_message_options'),
        ('Post', '0028_rewards_reward_earner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='reward_earner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward_earner', to='Profile.profile'),
        ),
    ]
