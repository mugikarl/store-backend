# Generated by Django 5.1.3 on 2024-11-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField(blank=True, default=None)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
