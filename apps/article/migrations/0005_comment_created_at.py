# Generated by Django 5.0.4 on 2024-05-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_slug_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
