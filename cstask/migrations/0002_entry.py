# Generated by Django 2.0.7 on 2018-08-01 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cstask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cstask.Topic')),
            ],
        ),
    ]
