# Generated by Django 5.1.7 on 2025-03-27 08:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='book/icons/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('audio', models.FileField(blank=True, null=True, upload_to='book/audio/')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='book/pdf/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('page_order', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserBookChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
