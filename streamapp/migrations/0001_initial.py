# Generated by Django 3.0.7 on 2020-06-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cam_name', models.CharField(default='My Cam', max_length=40)),
                ('framecount', models.IntegerField(default=0)),
                ('is_webcam', models.BooleanField()),
            ],
        ),
    ]
