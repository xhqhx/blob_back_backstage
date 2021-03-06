# Generated by Django 4.0 on 2021-12-30 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('friend_id', models.AutoField(primary_key=True, serialize=False)),
                ('friend_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=1)),
            ],
            options={
                'db_table': 'Friend',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=1)),
                ('introduction', models.TextField(default='')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('wish_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('permission', models.CharField(choices=[('public', '公开'), ('private', '私密'), ('fans', '仅粉丝可见')], default='public', max_length=8)),
                ('post_datetime', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'Wish',
            },
        ),
        migrations.CreateModel(
            name='FriendRelationship',
            fields=[
                ('friend_relationship_id', models.AutoField(primary_key=True, serialize=False)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.friend')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'FriendRelationship',
            },
        ),
    ]
