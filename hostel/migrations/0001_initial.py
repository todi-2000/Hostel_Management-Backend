# Generated by Django 3.1.5 on 2021-01-25 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostelDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('description', models.TextField(max_length=100000)),
                ('category', models.CharField(choices=[('Government', 'Government'), ('Semi-Government', 'Semi-Government'), ('Private', 'Private')], max_length=1000)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('fees', models.IntegerField()),
                ('total_rooms', models.IntegerField()),
                ('vacant_rooms', models.IntegerField()),
            ],
        ),
    ]
