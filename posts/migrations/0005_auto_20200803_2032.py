# Generated by Django 3.0.8 on 2020-08-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200803_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vil', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='post_vil',
            field=models.ManyToManyField(blank=True, related_name='vil_post', to='posts.Vil'),
        ),
    ]