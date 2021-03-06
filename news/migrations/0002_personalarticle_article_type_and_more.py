# Generated by Django 4.0 on 2021-12-30 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalarticle',
            name='article_type',
            field=models.CharField(choices=[('I', '图片'), ('V', '视频'), ('C', '纯文本')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='personalarticle',
            name='category',
            field=models.CharField(choices=[('H', '前线热线'), ('Z', '疫情实事'), ('X', '国际疫情事件')], default='Z', max_length=1),
        ),
    ]
