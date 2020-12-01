# Generated by Django 3.1.3 on 2020-11-07 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='数据集名')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=1024, upload_to='media/')),
                ('dataset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='File.dataset')),
            ],
            options={
                'unique_together': {('dataset', 'file')},
            },
        ),
    ]