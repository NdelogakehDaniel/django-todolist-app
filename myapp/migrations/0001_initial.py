# Generated by Django 4.0 on 2021-12-27 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=500)),
                ('done', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'list',
            },
        ),
    ]