from rest_framework import serializers
from .models import Country, Language, Education, ActionArea, TalkThemes

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Country


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Education


class ActionAreaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = ActionArea


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Language


class TalkThemesSerializer(serializers.ModelSerializer):
    image_png = serializers.SerializerMethodField()
    image_svg = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = TalkThemes
    
    def get_image_png(self, image):
        request = self.context.get('request')
        photo_url = image.image_png.url
        return request.build_absolute_uri(photo_url)

    def get_image_svg(self, image):
        request = self.context.get('request')
        photo_url = image.image_svg.url
        return request.build_absolute_uri(photo_url)


class TalkThemesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = TalkThemes
