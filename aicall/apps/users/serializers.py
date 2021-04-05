
from rest_framework import serializers
from .models import *
import sys
sys.path.append('..')
from ..info.serializers import *
from django.db.models import Avg

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return value.timestamp()
    
    def to_internal_value(self, value):
        return value


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

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username',
            'password'
        )
    
        model = User

class CreateUserSerializer(serializers.ModelSerializer):

    birthday_date = TimestampField(required=False)

    class Meta:
        exclude = (
            'is_superuser',
            'last_name',
            'is_staff',
            'password',
            'user_permissions',
            'groups',
            'last_login'
        )
        model = User

class UserSerializer(serializers.ModelSerializer):

    birthday_date = TimestampField(required=False)

    class Meta:
        exclude = (
            'password',
            'user_permissions',
            'groups',
            'last_login'
        )
        model = User

class UserPartialSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('password')
        model = User


class GetUserSerializer(serializers.ModelSerializer):
    country = CountrySerializer(required=False)
    education = EducationSerializer(required=False)
    action_area = ActionAreaSerializer(required=False)
    languages = LanguageSerializer(required=False, many=True)
    birthday_date = TimestampField(required=False)
    date_joined = TimestampField(required=False)
    average_rating = serializers.SerializerMethodField('user_average_rating')

    def user_average_rating(self, user):
        return Characteristic.objects.filter(reciever=user).aggregate(Avg('grade'))['grade__avg']

    class Meta:
        exclude = (
            'first_name',
            'last_name',
            'is_superuser',
            'password',
            'user_permissions',
            'groups',
            'is_staff',
            'is_active',
            'last_login'
        )
        model = User


class TestSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    question = QuestionSerializer()

    class Meta:
        fields = '__all__'
        model = Test

class GetCharacteristicSerializer(serializers.ModelSerializer):

    sender = UserSerializer()
    reciever = UserSerializer()
    positive_sides = PositiveSideSerializer()
    negative_sides = NegativeSideSerializer()
    class Meta:
        fields = '__all__'
        model = Characteristic

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Characteristic

class CharacteristicPartialSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(required=False)
    reciever_name = serializers.CharField(required=False)
    class Meta:
        fields = ('sender_name', 'reciever_name')
        model = Characteristic

class GetCharacteristicSerializer(serializers.ModelSerializer):

    sender = UserSerializer()
    reciever = UserSerializer()
    positive_sides = PositiveSideSerializer(many=True)
    negative_sides = NegativeSideSerializer(many=True)
    class Meta:
        exclude = ('sender_name', ) 
        model = Characteristic

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Characteristic

class GetUserPhoneSerializer(serializers.ModelSerializer):

    owner = UserSerializer()
    class Meta:
        fields = '__all__'
        model = UserContanctPhone

class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserContanctPhone