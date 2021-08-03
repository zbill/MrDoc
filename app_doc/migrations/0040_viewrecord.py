# Generated by Django 2.2.24 on 2021-08-01 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0039_auto_20210731_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP地址')),
                ('view_date', models.DateField(blank=True, null=True, verbose_name='查看日期')),
                ('view_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='浏览次数')),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_doc.Doc', verbose_name='文档id')),
            ],
        ),
    ]