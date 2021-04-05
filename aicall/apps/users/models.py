import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill
from apps.utils.func import user_avatar
from apps.info.models import *
from unixtimestampfield.fields import UnixTimeStampField
from dateutil.relativedelta import relativedelta
import datetime


SEX = [
    (2, "Мужской"),
    (1, "Женский"),
    (0, "Не выбран")
]

FAMILY_STATUS = [
    (1, "В браке"),
    (0, "Свободен")
]

TYPES_SHORTOCDES = [
    ('ESFJ', 'ESFJ'),
    ('ESFP', 'ESFP'),
    ('ESTJ', 'ESTJ'),
    ('ESTP', 'ESTP'),

    ('ENFJ', 'ENFJ'),
    ('ENFP', 'ENFP'),
    ('ENTJ', 'ENTJ'),
    ('ENTP', 'ENTP'),
    
    ('ISFJ', 'ISFJ'),
    ('ISFP', 'ISFP'),
    ('ISTJ', 'ISTJ'),
    ('ISTP', 'ISTP'),

    ('INFJ', 'INFJ'),
    ('INFP', 'INFP'),
    ('INTJ', 'INTJ'),
    ('INTP', 'INTP'),


]

class Question(models.Model):
    name_ru = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)

class Shortcode(models.Model):
    shortcode = models.CharField(max_length=4, choices=TYPES_SHORTOCDES, unique=True)
    name_ru = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255)
    description_ru = models.TextField()
    description_eng = models.TextField()


class User(AbstractUser):
    email = models.EmailField(
        'E-mail',
        unique=True,
        help_text='Required',
        error_messages={
            'unique': "A user with that E-mail already exists.",
        },
        null=True,
        db_index=True
    )
    phone = models.CharField(
        'Phone',
        unique=True,
        max_length=20
    )
    username = models.CharField(
        'Username', max_length=255, null=True, blank=True, unique=True)
    birthday_date = UnixTimeStampField(verbose_name='Date of birthday in timestamp', null=True, blank=True)
    sex = models.IntegerField('Sex', choices=SEX, null=True, default=0)
    family = models.IntegerField(
        'Family', choices=FAMILY_STATUS, null=True, default=0)
    notifications = models.BooleanField('Notifications', default=False)
    languages = models.ManyToManyField(Language, related_name='user_language', blank=True)
    country = models.ForeignKey(Country, related_name='user_country', on_delete=models.DO_NOTHING, null=True, blank=True)
    education = models.ForeignKey(Education, related_name='user_education', on_delete=models.DO_NOTHING, null=True, blank=True)
    action_area = models.ForeignKey(
        ActionArea, related_name='user_action_area', on_delete=models.DO_NOTHING, null=True, blank=True)
    psycho_type = models.ForeignKey(Shortcode, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    mobile_book_access = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = [
        'username',
        'email'
    ]

    @staticmethod
    def _create_user(username, password, birthday_date, email, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        user = User.objects.create(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, birthday_date, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, birthday_date, email, **extra_fields)

    def create_superuser(self, username, birthday_date, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, birthday_date, email, **extra_fields)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Phone(models.Model):
    phone = models.BigIntegerField(db_index=True)
    code = models.IntegerField('Code', db_index=True)
    is_checked = models.BooleanField('Is checked', default=False)
    created_at = models.DateTimeField('Created at', auto_now=True)
    expires_at = models.DateTimeField('Expires at', default=datetime.date.today() + relativedelta(minutes=20))

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

class Test(models.Model):
    user = models.ForeignKey(User, related_name='user_answer', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='test_question', on_delete=models.CASCADE)
    answer = models.IntegerField()

class Characteristic(models.Model):
    sender = models.ForeignKey(User, related_name='characteristic_sender', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='characteristic_reciever', on_delete=models.CASCADE)
    grade = models.IntegerField(verbose_name='Rating grade')
    sender_name = models.CharField('Characterisric sender name', max_length=100)
    reciever_name = models.CharField('Characterisric sender name', max_length=100, default=str(datetime.datetime.timestamp(datetime.datetime.now())))
    positive_sides = models.ManyToManyField(PositiveSide, related_name='Characteristic_positive_sides')
    negative_sides = models.ManyToManyField(NegativeSide, related_name='Characteristic_negative_sides')
    compatible = models.BooleanField(default=False)
    readed = models.BooleanField(default=False)

class UserContanctPhone(models.Model):
    owner = models.ForeignKey(User, related_name='phone_owner', on_delete=models.CASCADE)
    phone = models.CharField('User phone', max_length=15)
