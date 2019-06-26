from django.urls import path

from .views import ImageView,WordView

app_name = 'image_recognition'

urlpatterns =[
    path('classify',ImageView.as_view(), name='classify'),
    path('word',WordView.as_view(), name='word')
]