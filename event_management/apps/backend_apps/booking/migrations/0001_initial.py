# Generated by Django 2.2.4 on 2021-02-13 20:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booking_id', models.CharField(max_length=50)),
                ('booking_for', models.CharField(max_length=250)),
                ('booking_description', models.TextField(blank=True)),
                ('booking_remark', models.TextField(blank=True)),
                ('status', models.CharField(default='inactive', max_length=180, validators=[django.core.validators.RegexValidator])),
                ('trash', models.BooleanField(default=False)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_event_id', to='event.Cl')),
            ],
        ),
    ]
