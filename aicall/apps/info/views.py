from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CountryCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Country.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CountrySerializer


class CountryAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Country.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CountrySerializer


class CountryListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Country.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CountrySerializer


class CreateLanguageAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Language.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = LanguageSerializer


class LanguageAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Language.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = LanguageSerializer


class LanguageListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Language.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = LanguageSerializer


class CreateEducationAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Education.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = EducationSerializer


class EducationAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Education.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = EducationSerializer


class EducationListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Education.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = EducationSerializer


class CreateActionAreaAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = ActionArea.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = ActionAreaSerializer

class ActionAreaAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = ActionArea.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = ActionAreaSerializer


class ActionAreaListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = ActionArea.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = ActionAreaSerializer


class TalkThemesCreate(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = TalkThemes.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = TalkThemesCreateSerializer


class TalkThemesUpdate(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = TalkThemes.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = TalkThemesCreateSerializer


class TalkThemesAPI(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = TalkThemes.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = TalkThemesSerializer

    def get_serializer_context(self):
        context = super(generics.RetrieveDestroyAPIView,
                        self).get_serializer_context()
        context.update({"request": self.request})
        return context


class TalkThemesListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = TalkThemes.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = TalkThemesSerializer

    def get_serializer_context(self):
        context = super(generics.ListAPIView, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class PositiveSideCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = PositiveSide.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PositiveSideSerializer


class PositiveSideAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = PositiveSide.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PositiveSideSerializer


class PositiveSideListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = PositiveSide.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PositiveSideSerializer

class NegativeSideCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = NegativeSide.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = NegativeSideSerializer


class NegativeSideAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = NegativeSide.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = NegativeSideSerializer


class NegativeSideListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = NegativeSide.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = NegativeSideSerializer