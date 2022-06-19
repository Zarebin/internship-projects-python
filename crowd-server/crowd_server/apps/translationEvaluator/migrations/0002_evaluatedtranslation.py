# Generated by Django 4.0.4 on 2022-06-14 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('translationEvaluator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluatedTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('previous', 'previous'), ('skip', 'skip'), ('true', 'true'), ('false', 'false')], max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluated_translation', to='translationEvaluator.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluated_translation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]