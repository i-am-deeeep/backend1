from django.urls import path
from showsApp.views import ShowListGV, ShowDetailGV, PlatformListAV, PlatformDetailAV


urlpatterns = [
    path('show/list/', ShowListGV.as_view(), name='show-list'),
    path('show/<int:pk>/', ShowDetailGV.as_view(), name='show-detail'),
    path('platform/list/', PlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:pk>/', PlatformDetailAV.as_view(), name='platform-detail'),
]