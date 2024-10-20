# Generated by Django 5.1.2 on 2024-10-17 20:42

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_congreso_is_active_entidad_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=django_countries.fields.CountryField(default='HN', max_length=2),
        ),
        migrations.AddField(
            model_name='person',
            name='identification',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='person',
            name='type_identification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.identificationtype'),
        ),
    ]
