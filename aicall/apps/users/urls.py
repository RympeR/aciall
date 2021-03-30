from django.urls import path
from .views import *

urlpatterns = [
    path('create-phone/', UserCreateAPI.as_view()),
    path('update-phone/<int:pk>', PhoneAPI.as_view()),
    path('delete-phone/<int:pk>', PhoneAPI.as_view()),
    path('get-phone/<int:pk>', PhoneAPI.as_view()),
    path('get-phones', PhoneListAPI.as_view()),
    
    path('create-contact-phone/', ContactPhoneCreateAPI.as_view()),
    path('update-contact-phone/<int:pk>', ContactPhoneAPI.as_view()),
    path('delete-contact-phone/<int:pk>', ContactPhoneAPI.as_view()),
    path('get-contact-phone/<int:pk>', ContactPhoneAPI.as_view()),
    path('get-contact-phones', GetContactPhoneAPI.as_view()),
    
    path('create-chararcteristics/', CharacteristicCreateAPI.as_view()),
    path('update-chararcteristics/<int:pk>', UpdateCharacteristic.as_view()),
    path('delete-chararcteristics/<int:pk>', CharacteristicAPI.as_view()),
    path('get-chararcteristics/<int:pk>', CharacteristicAPI.as_view()),
    path('get-chararcteristics-list', CharacteristicListAPI.as_view()),
    
    path('create-test/', TestCreateAPI.as_view()),
    path('update-test/<int:pk>', TestAPI.as_view()),
    path('delete-test/<int:pk>', TestAPI.as_view()),
    path('get-test/<int:pk>', TestAPI.as_view()),
    path('get-tests', TestListAPI.as_view()),

    path('get-users-list', UsersList.as_view() ,name='UsersList'),
    
    path('create-shortcode/', ShortcodeCreateAPI.as_view()),
    path('update-shortcode/<int:pk>', ShortcodeAPI.as_view()),
    path('delete-shortcode/<int:pk>', ShortcodeAPI.as_view()),
    path('get-shortcode/<int:pk>', ShortcodeAPI.as_view()),
    path('get-shortcodes', ShortcodeListAPI.as_view()),

    path('update-psychotype/<int:pk>', UserPsycho.as_view()),

    path('update-password/<int:pk>', UpdatePassword.as_view())
]
