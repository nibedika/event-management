# Generated by Django 2.2.4 on 2021-02-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('about_id', models.CharField(max_length=50)),
                ('about_txt', models.TextField(blank=True)),
                ('about_img', models.FileField(blank=True, upload_to='')),
                ('cv_file', models.FileField(blank=True, upload_to='')),
                ('home_img', models.FileField(blank=True, upload_to='')),
                ('trash', models.BooleanField(default=False)),
            ],
        ),
    ]
