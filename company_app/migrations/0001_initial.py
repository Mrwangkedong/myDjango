# Generated by Django 2.2.1 on 2019-07-21 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('company', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='company_depart', to='company_app.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('phone_number', models.CharField(default='', max_length=11)),
                ('email', models.CharField(default='', max_length=32)),
                ('password', models.CharField(default='123456', max_length=32)),
                ('level', models.IntegerField()),
                ('coming_time', models.DateTimeField()),
                ('company', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='per_group', to='company_app.Group')),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='per_dep', to='company_app.Department')),
                ('group', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='per_com', to='company_app.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kill', models.BooleanField(default=False)),
                ('radio_call', models.BooleanField(default=True)),
                ('real_time_video', models.BooleanField(default=True)),
                ('incoming_call', models.BooleanField(default=True)),
                ('out_call', models.BooleanField(default=True)),
                ('FM_call', models.BooleanField(default=True)),
                ('enterprise_control', models.BooleanField(default=False)),
                ('p_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='person_power', to='company_app.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Fm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('info', models.CharField(max_length=200)),
                ('max_persons', models.IntegerField(default=20)),
                ('creater', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='per_fmcreater', to='company_app.Person')),
                ('users', models.ManyToManyField(to='company_app.Person')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='department',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='group_company', to='company_app.Group'),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('creater', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='per_talkcreter', to='company_app.Person')),
                ('users', models.ManyToManyField(to='company_app.Person')),
            ],
        ),
    ]