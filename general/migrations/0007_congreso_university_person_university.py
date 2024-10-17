# Generated by Django 5.1.2 on 2024-10-17 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_alter_congreso_owner_alter_congreso_place_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='congreso',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.university'),
        ),
        migrations.AddField(
            model_name='person',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.university'),
        ),
    ]
