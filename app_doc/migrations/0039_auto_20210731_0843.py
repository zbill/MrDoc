# Generated by Django 2.2.24 on 2021-07-31 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0038_project_is_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='last_view_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='最后浏览时间'),
        ),
        migrations.AddField(
            model_name='doc',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='浏览次数'),
        ),
    ]