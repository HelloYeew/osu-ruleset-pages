# Generated by Django 3.2.6 on 2021-09-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_tag_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
