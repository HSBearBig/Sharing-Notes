# Generated by Django 4.0.1 on 2022-01-09 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academy', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=20)),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.academy')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.department')),
            ],
        ),
        migrations.CreateModel(
            name='NoteUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('images', models.ImageField(upload_to='upload_images/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.subject')),
            ],
        ),
    ]
