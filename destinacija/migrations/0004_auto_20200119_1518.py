# Generated by Django 3.0.2 on 2020-01-19 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinacija', '0003_auto_20200118_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinacija',
            name='regija',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='destinacija.Regija'),
        ),
    ]
