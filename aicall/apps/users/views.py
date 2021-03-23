from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token


class PhoneCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Phone.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PhoneSerializer


class PhoneAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Phone.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PhoneSerializer


class PhoneListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Phone.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PhoneSerializer


class TestCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Test.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CreateTestSerializer


class TestAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Test.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = TestSerializer


class TestListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Test.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = TestSerializer


class QuestionCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Question.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = QuestionSerializer


class QuestionAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Question.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = QuestionSerializer


class QuestionListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Question.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = QuestionSerializer

    def get_queryset(self):

        return Response(
            {

            }
        )


class ShortcodeCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Shortcode.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = ShortcodeSerializer


class ShortcodeAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Shortcode.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = ShortcodeSerializer


class ShortcodeListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Shortcode.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = ShortcodeSerializer


class UserCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CreateUserSerializer


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = UserSerializer


class UserListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GetUserSerializer


class UserPsycho(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def partial_update(self, request, *args, **kwargs):
        user = Token.objects.get(key=request.headers['Authorization']).user
        final_short = ''
        counter = {
            'E': 0,
            'I': 0,
            'S': 0,
            'N': 0,
            'T': 0,
            'F': 0,
            'J': 0,
            'P': 0,
        }
        for question in request.data['questions']:
            if question['id'] in [1, 5, 9]:
                if question['answer'] == 0:
                    counter['E'] += 1
                elif question['answer'] == 1:
                    counter['I'] += 1
            elif question['id'] in [2, 6, 10]:
                if question['answer'] == 0:
                    counter['S'] += 1
                elif question['answer'] == 1:
                    counter['N'] += 1
            elif question['id'] in [3, 7, 11]:
                if question['answer'] == 0:
                    counter['T'] += 1
                elif question['answer'] == 1:
                    counter['F'] += 1
            elif question['id'] in [4, 8, 12]:
                if question['answer'] == 0:
                    counter['J'] += 1
                elif question['answer'] == 1:
                    counter['P'] += 1
        final_short += 'E' if counter['E'] > counter['I'] else 'I'
        final_short += 'S' if counter['S'] > counter['N'] else 'N'
        final_short += 'T' if counter['T'] > counter['F'] else 'F'
        final_short += 'J' if counter['J'] > counter['P'] else 'P'

        shortcode = Shortcode.objects.get(shortcode=final_short)
        kwargs['partial'] = True
        user.psycho_type = shortcode
        user.save()
        return self.update(request, *args, **kwargs)
