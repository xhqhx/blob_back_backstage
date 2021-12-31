# Generated by Django 4.0 on 2021-12-30 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('news', '0002_personalarticle_article_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowsingHistory',
            fields=[
                ('browsinghistory_id', models.AutoField(primary_key=True, serialize=False)),
                ('browsing_datetime', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.personalarticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'BrowsingHistory',
            },
        ),
    ]
