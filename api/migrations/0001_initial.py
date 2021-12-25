# Generated by Django 4.0 on 2021-12-25 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog', models.TextField(max_length=600)),
                ('like', models.IntegerField(default=0)),
                ('comment', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, null=True, unique=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=250)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.blogmodel')),
            ],
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]