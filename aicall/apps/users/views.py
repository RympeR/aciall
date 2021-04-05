from django.http import request
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from .raw_sql import UserFilter
from .psychotype import Psycho
from django.db.models import Q

psycho = Psycho()


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


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

class UserLogin(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny)
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)


class UpdatePassword(APIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        print(User)
        user.set_password(request.data['new_password'])
        user.save()
        return Response({
            "phone": user.phone,
            "curr_password": request.data['new_password'],
            "status": True
        })


class UsersList(APIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    userfilter = UserFilter()
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):

        data = self.userfilter.get_users(request, 'postgres', '1111')
        result = {
            "results": []
        }
        for ind, row in enumerate(data):
            result['results'].append({
                "id": row[0],
                "phone": row[1],
                "username": row[2],
            })
        return Response(
            {
                "results": result['results']
            }
        )


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CreateUserSerializer

    def partial_update(self, request, pk, *args, **kwargs):

        return self.update(request, *args, **kwargs)

class GetUserAPI(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GetUserSerializer


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


class ContactPhoneCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserContanctPhone.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = UserPhoneSerializer


class ContactPhoneAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserContanctPhone.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = UserPhoneSerializer


class GetContactPhoneAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = UserContanctPhone.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GetUserPhoneSerializer

    def get_queryset(self):
        user = Token.objects.get(
            key=self.request.headers['Authorization']).user
        phones = UserContanctPhone.objects.filter(owner=user)
        return phones


class CharacteristicListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Characteristic.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GetCharacteristicSerializer


class CharacteristicCreateAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Characteristic.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CharacteristicSerializer

    def perform_create(self, serializer):
        sender = self.request.data['sender']
        reciever = self.request.data['reciever']
        sender = User.objects.get(pk=sender).psycho_type
        reciever = User.objects.get(pk=reciever).psycho_type
        compatimble = psycho.get_compatible(
            sender,
            reciever
        )
        data = dict(request.data)
        data['compatible'] = bool(compatimble)
        serializer.save(data=data)


class CharacteristicAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Characteristic.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GetCharacteristicSerializer

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class CharacteristicListAPI(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Characteristic.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = GetCharacteristicSerializer


class UpdateCharacteristic(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
