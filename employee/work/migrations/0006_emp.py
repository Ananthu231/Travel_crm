# Generated by Django 4.2.6 on 2023-11-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_alter_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=20)),
                ('salary', models.PositiveIntegerField()),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
    ]
