# Generated by Django 4.2.2 on 2023-06-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
