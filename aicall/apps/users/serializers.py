
from rest_framework import serializers
from .models import *
from apps.info.serializers import *


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return value.timestamp()


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Phone


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Question


class ShortcodeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Shortcode


class CreateTestSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Test


class CreateUserSerializer(serializers.ModelSerializer):

    birthday_date = TimestampField(required=False)

    class Meta:
        exclude = (
            'password',
            'user_permissions',
            'groups',
            'date_joined',
            'last_login'
        )
        model = User

class UserSerializer(serializers.ModelSerializer):

    birthday_date = TimestampField(required=False)
    psycho_type = ShortcodeSerializer(required=False)

    class Meta:
        exclude = (
            'password',
            'user_permissions',
            'groups',
            'date_joined',
            'last_login'
        )
        model = User


class GetUserSerializer(serializers.ModelSerializer):
    country = CountrySerializer(required=False)
    education = EducationSerializer(required=False)
    action_area = ActionAreaSerializer(required=False)
    languages = LanguageSerializer(required=False, many=True)
    birthday_date = TimestampField(required=False)
    date_joined = TimestampField(required=False)
    last_login = TimestampField(required=False)
    psycho_type = ShortcodeSerializer(required=False)

    class Meta:
        exclude = (
            'password',
            'user_permissions',
            'groups',
        )
        model = User


class TestSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    question = QuestionSerializer()

    class Meta:
        fields = '__all__'
        model = Test
