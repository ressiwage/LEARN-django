# Generated by Django 5.0 on 2023-12-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_option_alter_choice_question_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='option',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
