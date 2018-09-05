# Generated by Django 2.1 on 2018-09-05 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0007_auto_20180904_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('message', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='projectusercomment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='projectusercomment',
            name='project',
        ),
        migrations.DeleteModel(
            name='ProjectUserComment',
        ),
    ]
