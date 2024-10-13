from django.urls import path
from .views import homepage, tag_detail, startup_list, startup_detail


urlpatterns = [
    path('tag/', homepage, name='organizer_tag_list'),
    path('tag/<slug:slug>/', tag_detail, name='organizer_tag_detail'),
    path('startup/', startup_list, name='organizer_startup_list'),
    path('startup/<slug:slug>', startup_detail, name='organizer_startup_detail'),
]