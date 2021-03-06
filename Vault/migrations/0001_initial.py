# Generated by Django 2.0.4 on 2018-05-01 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=200)),
                ('volume', models.IntegerField()),
                ('issue', models.IntegerField()),
                ('writer', models.CharField(max_length=200)),
                ('illustrator', models.CharField(max_length=200)),
                ('colorist', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('cover_art', models.URLField()),
                ('spoiler_free_synopsis', models.CharField(max_length=500)),
                ('full_synopsis', models.CharField(max_length=500)),
                ('characters', models.CharField(max_length=200)),
                ('average_rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ComicComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('content', models.CharField(max_length=500)),
                ('comic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.Comic')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NewsfeedComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NewsfeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('comic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comic_id', to='Vault.Comic')),
                ('general_news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general_news_id', to='Vault.Comic')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.Comic')),
            ],
        ),
        migrations.CreateModel(
            name='TimelineComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TimelinePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('content', models.CharField(max_length=500)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=300)),
                ('preferences', models.CharField(max_length=300)),
                ('comic_persona', models.CharField(max_length=30)),
                ('profile_picture', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='timelinepost',
            name='user_profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.UserProfile'),
        ),
        migrations.AddField(
            model_name='timelinecomment',
            name='timeline_post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.TimelinePost'),
        ),
        migrations.AddField(
            model_name='timelinecomment',
            name='user_profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.UserProfile'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user_profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.UserProfile'),
        ),
        migrations.AddField(
            model_name='newsfeedcomment',
            name='newsfeed_item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.NewsfeedItem'),
        ),
        migrations.AddField(
            model_name='newsfeedcomment',
            name='user_profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.UserProfile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='id_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_1', to='Vault.UserProfile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='id_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_2', to='Vault.UserProfile'),
        ),
        migrations.AddField(
            model_name='comiccomment',
            name='user_profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.UserProfile'),
        ),
    ]
