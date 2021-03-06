# Generated by Django 3.0.6 on 2020-05-27 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0004_auto_20200527_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(choices=[(True, 'Available'), (False, 'Busy')], verbose_name='Available')),
            ],
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.Provider', verbose_name='Service Provider')),
                ('service', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='website.Service', verbose_name='Service')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='Order Placed At')),
                ('active', models.BooleanField(choices=[(True, 'Available'), (False, 'Busy')], verbose_name='Available')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.UserDetail', verbose_name='Customer')),
                ('detail', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='website.ServiceDetail', verbose_name='Service Provided')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.Provider', verbose_name='Service Provider')),
            ],
        ),
    ]
