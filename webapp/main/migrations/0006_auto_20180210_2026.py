# Generated by Django 2.0.1 on 2018-02-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171104_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('jsonString', models.CharField(max_length=1000000000000)),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
