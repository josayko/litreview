# Generated by Django 4.0.1 on 2022-02-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollow',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
