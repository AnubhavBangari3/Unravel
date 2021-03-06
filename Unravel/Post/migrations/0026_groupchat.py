# Generated by Django 3.2.5 on 2022-04-16 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_alter_message_options'),
        ('Post', '0025_delete_rewards'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_body', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('group_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_chat', to='Post.joingroup')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_message', to='Profile.profile')),
            ],
        ),
    ]
