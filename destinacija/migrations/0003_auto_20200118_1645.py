# Generated by Django 3.0.2 on 2020-01-18 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinacija', '0002_destinacija_mapa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Regije',
            },
        ),
        migrations.AddField(
            model_name='destinacija',
            name='regija',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='destinacija.Regija'),
        ),
    ]