# Generated by Django 3.1.3 on 2020-11-18 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
        ('File', '0002_auto_20201114_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.project'),
        ),
    ]
