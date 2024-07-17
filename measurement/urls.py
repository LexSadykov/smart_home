from django.urls import path
from .views import SensorListCreateView, SensorUpdateView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorUpdateView.as_view(), name='sensor-update'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'), 
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]