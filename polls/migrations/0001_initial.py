# Generated by Django 2.2.1 on 2019-05-03 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sorular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soru_metni', models.CharField(max_length=200)),
                ('tarih', models.DateTimeField(verbose_name='tarihi')),
            ],
        ),
        migrations.CreateModel(
            name='Secim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secim_metni', models.CharField(max_length=200)),
                ('oylar', models.IntegerField(default=0)),
                ('soru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Sorular')),
            ],
        ),
    ]