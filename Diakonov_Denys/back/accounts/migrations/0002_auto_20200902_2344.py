# Generated by Django 3.1.1 on 2020-09-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
