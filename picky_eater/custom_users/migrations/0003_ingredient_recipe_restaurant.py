# Generated by Django 2.0.4 on 2018-05-25 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('custom_users', '0002_auto_20180404_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alternative_names', models.ForeignKey(blank=True, null=True, on_delete='protect', to='custom_users.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('ingredients', models.ForeignKey(on_delete='cascade', to='custom_users.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('NIP', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text="I don't have any idea what i'm doing but i keep on going for it.", related_name='restaurants_set', related_query_name='restaurant', to='auth.Group', verbose_name='Restaurants_group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='restaurant_set', related_query_name='restaurant', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
