# Generated by Django 3.2.9 on 2021-11-06 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('folder_id', models.AutoField(primary_key=True, serialize=False)),
                ('folder_name', models.CharField(max_length=120, verbose_name='Folder Name')),
                ('folder_description', models.CharField(max_length=255, verbose_name='Folder Description')),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=120, verbose_name='Topic Name')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('doc_id', models.AutoField(primary_key=True, serialize=False)),
                ('doc_name', models.CharField(max_length=120, verbose_name='Document Name')),
                ('doc_path', models.CharField(max_length=255, verbose_name='Document Location')),
                ('folder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spekit_app.folders')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spekit_app.topics')),
            ],
        ),
    ]
