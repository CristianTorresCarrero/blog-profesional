# Generated by Django 5.1.6 on 2025-02-15 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('image_profile', models.ImageField(upload_to='profile_images/')),
                ('cv_pdf', models.FileField(upload_to='cv_pdfs/')),
            ],
        ),
    ]
