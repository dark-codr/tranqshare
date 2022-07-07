# Generated by Django 3.2.12 on 2022-06-15 18:30

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Middle Name')),
                ('ref', models.CharField(blank=True, max_length=25, verbose_name='Referral Link')),
                ('bonus', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('roi', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('phone', models.CharField(blank=True, help_text='eg: 018276475673', max_length=17)),
                ('dp', stdimage.models.StdImageField(blank=True, upload_to='user/dp')),
                ('eth_address', models.CharField(blank=True, max_length=250)),
                ('btc_address', models.CharField(blank=True, max_length=250)),
                ('usdt_address', models.CharField(blank=True, max_length=250)),
                ('first_investment', models.BooleanField(default=True)),
                ('has_invested', models.BooleanField(default=False)),
                ('has_toped', models.BooleanField(default=False)),
                ('can_withdraw', models.BooleanField(default=False)),
                ('can_topup', models.BooleanField(default=False)),
                ('can_withdraw_roi', models.BooleanField(default=False)),
                ('confirm', models.BooleanField(default=False)),
                ('country', models.ForeignKey(blank=True, default='US', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='countries_plus.country')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('recommended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ref_by', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('amount', models.DecimalField(decimal_places=7, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Crypto Currency',
                'verbose_name_plural': 'Crypto Currencies',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('question', models.CharField(max_length=700)),
                ('answer', models.TextField(verbose_name='Answer')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Legals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=700)),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Legal',
                'verbose_name_plural': 'Legals',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=700)),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Privacy',
                'verbose_name_plural': 'Privacies',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SmartsUpp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('script', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Smartsupp Upload',
                'verbose_name_plural': 'Smartsupp Uploads',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TradeOpen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('open', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Trade Week Open/Close',
                'verbose_name_plural': 'Trade Week Open/Close',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.CharField(blank=True, max_length=35)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('FAILED', 'FAILED'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=15)),
                ('wallet', models.CharField(blank=True, max_length=250)),
                ('amount', models.DecimalField(decimal_places=7, default=0.0, max_digits=20)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdraw', to='users.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withraw', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Withdraw History',
                'verbose_name_plural': 'Withdraw Histories',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('btc', models.DecimalField(decimal_places=5, default=0.0, max_digits=20)),
                ('eth', models.DecimalField(decimal_places=5, default=0.0, max_digits=20)),
                ('usdt', models.DecimalField(decimal_places=5, default=0.0, max_digits=20)),
                ('invested_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Wallet',
                'verbose_name_plural': 'User Wallets',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.CharField(blank=True, max_length=35, unique=True)),
                ('transaction_type', models.CharField(choices=[('AFFILIATE', 'AFFILIATE'), ('DEPOSIT', 'DEPOSIT'), ('WITHDRAW', 'WITHDRAW'), ('ROI', 'ROI')], default='DEPOSIT', max_length=15)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('FAILED', 'FAILED'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=15)),
                ('amount', models.DecimalField(decimal_places=7, default=0.0, max_digits=20)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='users.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction History',
                'verbose_name_plural': 'Transaction Histories',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='KYCVerify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('pass_front', stdimage.models.StdImageField(blank=True, upload_to='passport/front')),
                ('pass_back', stdimage.models.StdImageField(blank=True, upload_to='passport/back')),
                ('approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kyc', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'KYC Verification',
                'verbose_name_plural': 'KYC Verifications',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.CharField(blank=True, max_length=35)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('FAILED', 'FAILED'), ('SUCCESS', 'SUCCESS')], default='PENDING', max_length=15)),
                ('amount', models.DecimalField(decimal_places=7, default=0.0, max_digits=20)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit', to='users.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depsit', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Deposit History',
                'verbose_name_plural': 'Deposit Histories',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('wallet', models.CharField(blank=True, max_length=250)),
                ('qr', stdimage.models.StdImageField(blank=True, upload_to='qr/')),
                ('active', models.BooleanField(default=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='users.currency')),
            ],
            options={
                'verbose_name': 'Wallet Address',
                'verbose_name_plural': 'Wallet Addresses',
                'ordering': ['-modified'],
                'managed': True,
            },
        ),
    ]