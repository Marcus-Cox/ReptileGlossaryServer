# Generated by Django 4.1.1 on 2022-09-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reptileglossaryapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietguide',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reptileguide',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='specialneedsguide',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
