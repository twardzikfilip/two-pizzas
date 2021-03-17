# Generated by Django 3.1.7 on 2021-03-17 14:31

from django.db import migrations, models

def initialize_products(apps, *args):
    Person = apps.get_model('yourappname', 'Person')
    Person.objects.create({
        'name': 'Margharita',
        'sizes': '["medium", "large"]'
    })
    Person.objects.create({
        'name': 'Salami',
        'sizes': '["small", "medium", "large"]'
    })
    Person.objects.create({
        'name': 'Diavolo',
        'sizes': '["small", "medium", "large"]'
    })
    
class Migration(migrations.Migration):

    dependencies = [
        ('online_orders', '0002_order_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=320),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_size',
            field=models.CharField(choices=[('S', 'small'), ('M', 'medium'), ('L', 'large')], default='S', max_length=20),
        ),
        migrations.RunPython(initialize_products),
    ]