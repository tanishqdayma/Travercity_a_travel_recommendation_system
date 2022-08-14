# Generated by Django 2.2.7 on 2019-11-25 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usersignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('contact_no', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=8)),
                ('marital_status', models.CharField(max_length=8)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adventure', models.IntegerField(default=0)),
                ('heritage', models.IntegerField(default=0)),
                ('wildlife', models.IntegerField(default=0)),
                ('nature', models.IntegerField(default=0)),
                ('pilgrimage', models.IntegerField(default=0)),
                ('couple', models.IntegerField(default=0)),
                ('friends', models.IntegerField(default=0)),
                ('family', models.IntegerField(default=0)),
                ('winter', models.IntegerField(default=0)),
                ('spring', models.IntegerField(default=0)),
                ('summer', models.IntegerField(default=0)),
                ('monsoon', models.IntegerField(default=0)),
                ('autumn', models.IntegerField(default=0)),
                ('young', models.IntegerField(default=0)),
                ('mid_age', models.IntegerField(default=0)),
                ('old', models.IntegerField(default=0)),
                ('visited_state', models.CharField(default='null', max_length=20)),
                ('visited_city', models.CharField(default='null', max_length=20)),
                ('rate_place', models.IntegerField(default=0)),
                ('budget', models.IntegerField(default=0)),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='travel_app.Usersignup')),
            ],
        ),
    ]
