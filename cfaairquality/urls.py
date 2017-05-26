from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.introduction, name='introduction'),
    url(r'^$', views.about_codeforafrica, name='about_codeforafrica'),
    url(r'^sensor_setup/$', views.sensor_setup, name='sensor_setup'),
    url(r'^input_sensor_data/$', views.input_sensor_data, name='input_sensor_data'),
    url(r'^remotely_control_sensor/$', views.remotely_control_sensor, name='remotely_control_sensor'),
    url(r'^output_data/$', views.output_data, name='output_data'),
    url(r'^output_sensors_details/$', views.output_sensors_details, name='output_sensors_details'),
    url(r'^get_aqi_data/$', views.get_aqi_data, name='get_aqi_data'),
    url(r'^get_aqi_data1/$', views.get_aqi_data, name='get_aqi_data'),
    url(r'^get_aqi_data2/$', views.get_aqi_data2, name='get_aqi_data2'),
]
