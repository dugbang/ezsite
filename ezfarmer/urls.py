from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ezfarmer import views

app_name = 'ezfarmer'
urlpatterns = [

    path('api/plant/', views.PlantList.as_view(), name='api_plant_list'),
    path('api/plant/<int:pk>', views.PlantDetail.as_view(), name='api_plant_detail'),

    path('api/report/', views.ReportList.as_view(), name='api_report_list'),
    path('api/controller/<pk>/', views.ControllerDetail.as_view(), name='api_controller_detail'),

    path('plant/', views.PlantLV.as_view(), name='plant'),
    path('capture/', views.CaptureLV.as_view(), name='capture_list'),

    path('capture/upload/', views.CaptureCreateView.as_view(), name='capture_upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
