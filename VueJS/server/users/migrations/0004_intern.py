# Generated by Django 3.2.5 on 2021-08-04 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_alter_ext_user_ismanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('jobtype', models.CharField(max_length=50)),
                ('pay', models.IntegerField()),
                ('description', models.TextField()),
                ('username', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'interns',
            },
        ),
    ]
