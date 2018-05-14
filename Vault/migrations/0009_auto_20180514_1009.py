# Generated by Django 2.0.4 on 2018-05-14 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vault', '0008_auto_20180505_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('content', models.CharField(max_length=500)),
                ('generalnews_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.GeneralNews')),
                ('user_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vault.UserProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='newsfeedcomment',
            name='newsfeed_item_id',
        ),
        migrations.RemoveField(
            model_name='newsfeedcomment',
            name='user_profile_id',
        ),
        migrations.DeleteModel(
            name='NewsfeedComment',
        ),
    ]
