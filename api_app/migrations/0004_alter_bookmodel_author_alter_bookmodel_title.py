# Generated by Django 4.2.6 on 2023-10-18 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_alter_bookmodel_author_alter_bookmodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='author',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='title',
            field=models.CharField(null=True),
        ),
    ]
