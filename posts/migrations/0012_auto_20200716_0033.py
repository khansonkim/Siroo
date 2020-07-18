# Generated by Django 3.0.8 on 2020-07-15 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200716_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tags',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tagincomment',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='taginpost',
        ),
        migrations.CreateModel(
            name='Tag_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Tag')),
            ],
        ),
    ]
