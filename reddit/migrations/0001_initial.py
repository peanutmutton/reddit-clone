# Generated by Django 5.0.2 on 2024-02-16 09:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=100, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
