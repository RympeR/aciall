from rest_framework import serializers
from .models import Country, Language, Education, ActionArea, TalkThemes, PositiveSide, NegativeSide


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Country

class NegativeSideSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = NegativeSide

class PositiveSideSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = PositiveSide


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
        try:
            request = self.context.get('request')
            photo_url = image.image_png.url
            return request.build_absolute_uri(photo_url)
        except Exception:
            return None

    def get_image_svg(self, image):
        request = self.context.get('request')
        try:
            photo_url = image.image_svg.url
            return request.build_absolute_uri(photo_url)
        except Exception:
            return None


class TalkThemesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = TalkThemes
