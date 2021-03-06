# Generated by Django 4.0.4 on 2022-06-11 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_compare', '0003_alter_comparequestion_response_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparequestion',
            name='response_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comparison',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comparison', to='food_compare.comparequestion'),
        ),
        migrations.AlterField(
            model_name='comparison',
            name='response',
            field=models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('similar', 'Similar'), ('skip', 'Skip')], max_length=7),
        ),
        migrations.AlterField(
            model_name='comparison',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comparison', to=settings.AUTH_USER_MODEL),
        ),
    ]
