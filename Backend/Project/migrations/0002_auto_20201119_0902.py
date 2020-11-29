# Generated by Django 3.1.3 on 2020-11-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='createdData',
            field=models.DateTimeField(auto_now_add=True, verbose_name='项目创建时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='describe',
            field=models.TextField(blank=True, default='', max_length=1024, null=True, verbose_name='项目描述'),
        ),
        migrations.AlterField(
            model_name='project',
            name='updatedData',
            field=models.DateTimeField(auto_now_add=True, verbose_name='项目更新时间'),
        ),
    ]