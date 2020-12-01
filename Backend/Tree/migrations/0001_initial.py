# Generated by Django 3.1.3 on 2020-11-15 05:39

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='目录名')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Tree.catalog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='类名')),
                ('nickname', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='昵称')),
                ('describe', models.TextField(verbose_name='描述')),
                ('belong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Tree.catalog', verbose_name='所属目录')),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='函数名')),
                ('nickname', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='昵称')),
                ('describe', models.TextField(verbose_name='描述')),
                ('belong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Tree.catalog', verbose_name='所属目录')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='参数名')),
                ('describe', models.TextField(verbose_name='描述')),
                ('value', models.TextField(blank=True, null=True)),
                ('belongClass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Tree.class')),
                ('belongFunction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Tree.function')),
            ],
        ),
    ]