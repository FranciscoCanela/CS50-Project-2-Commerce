# Generated by Django 3.2 on 2021-04-27 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='comments',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listing'),
        ),
    ]
