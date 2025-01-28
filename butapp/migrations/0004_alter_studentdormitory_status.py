# Generated by Django 5.1.5 on 2025-01-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('butapp', '0003_alter_studentdormitory_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdormitory',
            name='status',
            field=models.CharField(choices=[('درخواست در حال بررسی : درخواست ثبت نام شما در حال بررسی می\u200cباشد ، لطفا تا زمان بررسی درخواست شکیبا باشید', 'در حال بررسی'), ('درخواست رد شده : درخواست شما از طرف کارشناس امور خوابگاه ها رد شده است ، جهت پیگیری در تایم اداری با شماره ۰۱۱۴۴۴۴۲۱۳۵ با داخلی ۱۴۹ تماس حاصل فرمایید', 'رد شده'), ('درخواست قبول شده : وضعیت درخواست ثبت نام شما در مرحله قبول شده می\u200cباشد ، لطفا در زمان اعلامی از طرف دانشگاه نسبت به نهایی کردن ثبت نام خود اقدام نمایید', 'تایید شده')], default='درخواست در حال بررسی : درخواست ثبت نام شما در حال بررسی می\u200cباشد ، لطفا تا زمان بررسی درخواست شکیبا باشید', max_length=200, verbose_name='وضعیت'),
        ),
    ]
