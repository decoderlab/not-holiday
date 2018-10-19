# Generated by Django 2.1.2 on 2018-10-16 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('day', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('weekday', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10)),
                ('status', models.CharField(choices=[('Holiday', 'Holiday'), ('NotHoliday', 'NotHoliday')], max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]