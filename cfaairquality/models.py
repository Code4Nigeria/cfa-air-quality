from django.db import models
from django.utils import timezone

# Create your models here.
# Every sensor has its table for easier and cleaner access to its data

class SensorDetails (models.Model):
    #sensor_details_id
    sensor_name = models.CharField (max_length =50)
    sensor_city = models.CharField (max_length =50)
    sensor_installed =models.IntegerField(default =0)
    sensor_incare_of = models.CharField (max_length =50, null =True, blank=True)
    sensor_organisation = models.CharField (max_length =50, null =True, blank=True)
    sensor_phoneno = models.CharField (max_length =50, null =True, blank=True)
    sensor_pollutants_var = models.CharField (max_length =50, null =True, blank=True)
    sensor_country = models.CharField (max_length =50, null =True, blank=True)
    sensor_log= models.CharField (max_length =50, null =True, blank=True)
    sensor_lat= models.CharField (max_length =50, null =True, blank=True)
    sensor_height= models.CharField (max_length =50, null =True, blank=True)

    def __str__(self):
        return self.sensor_name #this is what it retruns when requested. we can get primary key here also.

    def city (self):
        return self.city
    
class Sensor1Data (models.Model):
    #sensor1data_id
    sensor_details = models.ForeignKey(SensorDetails, on_delete=models.CASCADE)
    co_data= models.CharField (max_length =50)
    o3_data= models.CharField (max_length =50)
    no2_data= models.CharField (max_length =50)
    pm25_data= models.CharField (max_length =50)
    pm10_data= models.CharField (max_length =50)
    so2_data= models.CharField (max_length =50)
    co_iaqi= models.CharField (max_length =50, null =True, blank=True)
    o3_iaqi= models.CharField (max_length =50, null =True, blank=True)
    no2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm25_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm10_iaqi= models.CharField (max_length =50, null =True, blank=True)
    so2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm_nowcast= models.CharField (max_length =50, null =True, blank=True)
    aqi_data= models.CharField (max_length =50, null =True, blank=True)
    log_data= models.CharField (max_length =50, null =True, blank=True)
    lat_data= models.CharField (max_length =50, null =True, blank=True)
    hgt_data= models.CharField (max_length =50, null =True, blank=True)
    tim_data= models.CharField (max_length =50, null =True, blank=True)
    battery_status_data= models.CharField (max_length =50, null =True, blank=True)
    temp_data= models.CharField (max_length =50, null =True, blank=True)
    hum_data= models.CharField (max_length =50, null =True, blank=True)
    data_no= models.CharField (max_length =50, null =True, blank=True)
    data_int= models.CharField (max_length =50, null =True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str (self.sensor_details)
    def datano(self):
        return self.data_no

class Sensor2Data (models.Model):
    #sensor2data_id
    sensor_details = models.ForeignKey(SensorDetails, on_delete=models.CASCADE)
    co_data= models.CharField (max_length =50)
    o3_data= models.CharField (max_length =50)
    no2_data= models.CharField (max_length =50)
    pm25_data= models.CharField (max_length =50)
    pm10_data= models.CharField (max_length =50)
    so2_data= models.CharField (max_length =50)
    co_iaqi= models.CharField (max_length =50, null =True, blank=True)
    o3_iaqi= models.CharField (max_length =50, null =True, blank=True)
    no2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm25_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm10_iaqi= models.CharField (max_length =50, null =True, blank=True)
    so2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm_nowcast= models.CharField (max_length =50, null =True, blank=True)
    aqi_data= models.CharField (max_length =50, null =True, blank=True)
    log_data= models.CharField (max_length =50, null =True, blank=True)
    lat_data= models.CharField (max_length =50, null =True, blank=True)
    hgt_data= models.CharField (max_length =50, null =True, blank=True)
    tim_data= models.CharField (max_length =50, null =True, blank=True)
    battery_status_data= models.CharField (max_length =50, null =True, blank=True)
    temp_data= models.CharField (max_length =50, null =True, blank=True)
    hum_data= models.CharField (max_length =50, null =True, blank=True)
    data_no= models.CharField (max_length =50, null =True, blank=True)
    data_int= models.CharField (max_length =50, null =True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str (self.sensor_details)
    def datano(self):
        return self.data_no

class Sensor3Data (models.Model):
    #sensor3data_id
    sensor_details = models.ForeignKey(SensorDetails, on_delete=models.CASCADE)
    co_data= models.CharField (max_length =50)
    o3_data= models.CharField (max_length =50)
    no2_data= models.CharField (max_length =50)
    pm25_data= models.CharField (max_length =50)
    pm10_data= models.CharField (max_length =50)
    so2_data= models.CharField (max_length =50)
    co_iaqi= models.CharField (max_length =50, null =True, blank=True)
    o3_iaqi= models.CharField (max_length =50, null =True, blank=True)
    no2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm25_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm10_iaqi= models.CharField (max_length =50, null =True, blank=True)
    so2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm_nowcast= models.CharField (max_length =50, null =True, blank=True)
    aqi_data= models.CharField (max_length =50, null =True, blank=True)
    log_data= models.CharField (max_length =50, null =True, blank=True)
    lat_data= models.CharField (max_length =50, null =True, blank=True)
    hgt_data= models.CharField (max_length =50, null =True, blank=True)
    tim_data= models.CharField (max_length =50, null =True, blank=True)
    battery_status_data= models.CharField (max_length =50, null =True, blank=True)
    temp_data= models.CharField (max_length =50, null =True, blank=True)
    hum_data= models.CharField (max_length =50, null =True, blank=True)
    data_no= models.CharField (max_length =50, null =True, blank=True)
    data_int= models.CharField (max_length =50, null =True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str (self.sensor_details)
    def datano(self):
        return self.data_no
    
class Sensor4Data (models.Model):
    #sensor4data_id
    sensor_details = models.ForeignKey(SensorDetails, on_delete=models.CASCADE)
    co_data= models.CharField (max_length =50)
    o3_data= models.CharField (max_length =50)
    no2_data= models.CharField (max_length =50)
    pm25_data= models.CharField (max_length =50)
    pm10_data= models.CharField (max_length =50)
    so2_data= models.CharField (max_length =50)
    co_iaqi= models.CharField (max_length =50, null =True, blank=True)
    o3_iaqi= models.CharField (max_length =50, null =True, blank=True)
    no2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm25_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm10_iaqi= models.CharField (max_length =50, null =True, blank=True)
    so2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm_nowcast= models.CharField (max_length =50, null =True, blank=True)
    aqi_data= models.CharField (max_length =50, null =True, blank=True)
    log_data= models.CharField (max_length =50, null =True, blank=True)
    lat_data= models.CharField (max_length =50, null =True, blank=True)
    hgt_data= models.CharField (max_length =50, null =True, blank=True)
    tim_data= models.CharField (max_length =50, null =True, blank=True)
    battery_status_data= models.CharField (max_length =50, null =True, blank=True)
    temp_data= models.CharField (max_length =50, null =True, blank=True)
    hum_data= models.CharField (max_length =50, null =True, blank=True)
    data_no= models.CharField (max_length =50, null =True, blank=True)
    data_int= models.CharField (max_length =50, null =True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str (self.sensor_details) #returns the name of the sensor sending this data (No two sesnor has same name), as a string.
    def datano(self):
        return self.data_no


