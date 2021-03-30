from django.urls import path
from .views import *

urlpatterns = [
    path('create-country/', CountryCreateAPI.as_view()),
    path('update-country/<int:pk>', CountryAPI.as_view()),
    path('delete-country/<int:pk>', CountryAPI.as_view()),
    path('get-country/<int:pk>', CountryAPI.as_view()),
    path('get-countries', CountryListAPI.as_view()),
    
    path('create-positive-side/', PositiveSideCreateAPI.as_view()),
    path('update-positive-side/<int:pk>', PositiveSideAPI.as_view()),
    path('delete-positive-side/<int:pk>', PositiveSideAPI.as_view()),
    path('get-positive-side/<int:pk>', PositiveSideAPI.as_view()),
    path('get-positive-sides', PositiveSideListAPI.as_view()),
    
    path('create-negative-side/', NegativeSideCreateAPI.as_view()),
    path('update-negative-side/<int:pk>', NegativeSideAPI.as_view()),
    path('delete-negative-side/<int:pk>', NegativeSideAPI.as_view()),
    path('get-negative-side/<int:pk>', NegativeSideAPI.as_view()),
    path('get-negative-sides', NegativeSideListAPI.as_view()),
    
    path('create-action-area/', CreateActionAreaAPI.as_view()),
    path('update-action-area/<int:pk>', ActionAreaAPI.as_view()),
    path('delete-action-area/<int:pk>', ActionAreaAPI.as_view()),
    path('get-action-area/<int:pk>', ActionAreaAPI.as_view()),
    path('get-action-areas', ActionAreaListAPI.as_view()),
    
    path('create-language/', CreateLanguageAPI.as_view()),
    path('update-language/<int:pk>', LanguageAPI.as_view()),
    path('delete-language/<int:pk>', LanguageAPI.as_view()),
    path('get-language/<int:pk>', LanguageAPI.as_view()),
    path('get-languages', LanguageListAPI.as_view()),
    
    path('create-education/', CreateEducationAPI.as_view()),
    path('update-education/<int:pk>', EducationAPI.as_view()),
    path('delete-education/<int:pk>', EducationAPI.as_view()),
    path('get-education/<int:pk>', EducationAPI.as_view()),
    path('get-educations', EducationListAPI.as_view()),
    
    path('create-talk-theme/', TalkThemesCreate.as_view()),
    path('update-talk-theme/<int:pk>', TalkThemesUpdate.as_view()),
    path('delete-talk-theme/<int:pk>', TalkThemesAPI.as_view()),
    path('get-talk-theme/<int:pk>', TalkThemesAPI.as_view()),
    path('get-talk-themes', TalkThemesListAPI.as_view()),

]
