# Generated by Django 3.2.5 on 2022-04-29 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_alter_message_options'),
        ('Post', '0026_groupchat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward', models.CharField(choices=[('pawn', 10), ('rook', 35), ('bishop', 30), ('knight', 20), ('queen', 80), ('king', 100)], max_length=200)),
                ('group_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_post_r', to='Post.postgroup')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', to='Profile.profile')),
            ],
        ),
    ]
