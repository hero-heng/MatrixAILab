# Generated by Django 3.1.3 on 2020-11-19 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tree', '0006_auto_20201118_1057'),
        ('Project', '0004_node_graph'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='function',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tree.function'),
        ),
    ]