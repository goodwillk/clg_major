# Generated by Django 4.1.2 on 2022-10-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_remove_problem_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='website',
            field=models.CharField(choices=[('leetcode', 'Leetcode'), ('codechef', 'Codechef'), ('gfg', 'GeekForGeeks')], default='leetcode', max_length=200),
        ),
    ]
