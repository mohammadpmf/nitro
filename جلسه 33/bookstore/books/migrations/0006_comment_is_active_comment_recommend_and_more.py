# Generated by Django 4.1.3 on 2022-12-12 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_alter_comment_book_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True, verbose_name='پیشنهاد می شود'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book', verbose_name='نام کتاب'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='متن پیام'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
