# Generated by Django 5.1.7 on 2025-03-26 06:23

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('details', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField()),
                ('hypertension', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('heart_disease', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('ever_married', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('residence_type', models.IntegerField(choices=[(0, 'Rural'), (1, 'Urban')])),
                ('avg_glucose_level', models.FloatField()),
                ('bmi', models.FloatField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=10)),
                ('work_type', models.CharField(choices=[('Govt_job', 'Government Job'), ('Never_worked', 'Never Worked'), ('Private', 'Private'), ('Self-employed', 'Self-employed'), ('children', 'Children')], max_length=20)),
                ('smoking_status', models.CharField(choices=[('Unknown', 'Unknown'), ('formerly smoked', 'Formerly Smoked'), ('never smoked', 'Never Smoked'), ('smokes', 'Smokes')], max_length=20)),
                ('stroke', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True)),
                ('still_working', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
