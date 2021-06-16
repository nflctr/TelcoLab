# Generated by Django 3.2 on 2021-05-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telcoWeb', '0002_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('tipe', models.CharField(max_length=50)),
                ('isi', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]
