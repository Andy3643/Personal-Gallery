from django.urls import URLPattern, path
from . import views




urlpatterns =[
    path('',views.index,name='index'),
    path('search/',views.search_images,name="search_images"),
]