# Generated by Django 2.2.7 on 2019-12-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0003_questionnaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
