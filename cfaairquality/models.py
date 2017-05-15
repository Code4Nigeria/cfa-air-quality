from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
# Every sensor has its table for easier and cleaner access to its data

class SensorDetails (models.Model):
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
    sensor_data_interval = models.CharField (max_length =50, null =True, blank=True)
    sensor_data_owner =models.CharField (max_length =50, null =True, blank=True)
    sensor_created_date =models.DateTimeField(auto_now_add=True, blank=True)
    sensor_modified_date =models.DateTimeField(auto_now_add=True, blank=True)
    sensor_data_offset=models.IntegerField(default=0)
    sensor_offset_date =models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.sensor_name #this is what it returns when requested. we can get primary key here also but since we specified a string, it returns sensor_name

    def city (self):
        return self.city

class Sensor1Data (models.Model):
    #sensor1data_id / primary key.
    sensor_details = models.ForeignKey(SensorDetails, on_delete=models.CASCADE)
    co_data= models.CharField (max_length =50, null =True, blank=True)
    o3_data= models.CharField (max_length =50, null =True, blank=True)
    no2_data= models.CharField (max_length =50, null =True, blank=True)
    pm25_data= models.CharField (max_length =50, null =True, blank=True)
    pm10_data= models.CharField (max_length =50, null =True, blank=True)
    so2_data= models.CharField (max_length =50, null =True, blank=True)

    #hourly average
    co_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    o3_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    no2_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm25_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm10_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    so2_hr_ave= models.CharField (max_length =50, null =True, blank=True)

    #8hours-average
    co_8hr_ave= models.CharField (max_length =50, null =True, blank=True)
    o3_8hr_ave= models.CharField (max_length =50, null =True, blank=True)
    so2_8hr_ave= models.CharField (max_length =50, null =True, blank=True)

    #24 hours average.
    so2_24hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm25_24hr_ave=models.CharField (max_length =50, null =True, blank=True)
    pm10_24hr_ave= models.CharField (max_length =50, null =True, blank=True)

    # IAQI data
    co_iaqi= models.CharField (max_length =50, null =True, blank=True)
    o3_iaqi= models.CharField (max_length =50, null =True, blank=True)
    no2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm25_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm10_iaqi= models.CharField (max_length =50, null =True, blank=True)
    so2_iaqi= models.CharField (max_length =50, null =True, blank=True)

    # NowCast
    pm_nowcast25= models.CharField (max_length =50, null =True, blank=True)
    pm_nowcast10= models.CharField (max_length =50, null =True, blank=True)

    #AQI
    aqi_data= models.CharField (max_length =50, null =True, blank=True)

    #other data
    log_data= models.CharField (max_length =50, null =True, blank=True)
    lat_data= models.CharField (max_length =50, null =True, blank=True)
    hgt_data= models.CharField (max_length =50, null =True, blank=True)
    tim_data= models.CharField (max_length =50, null =True, blank=True)
    battery_status_data= models.CharField (max_length =50, null =True, blank=True)
    temp_data= models.CharField (max_length =50, null =True, blank=True)
    hum_data= models.CharField (max_length =50, null =True, blank=True)

    #Monitoring Data
    data_no= models.CharField (max_length =50, null =True, blank=True)
    data_int= models.CharField (max_length =50, null =True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return str (self.pk) + " "+ str(self.sensor_details) #

    def datano(self):
        return self.data_no

class Sensor2Data (models.Model):
    #sensor2data_id
    sensor_details = models.ForeignKey(SensorDetails, on_delete=models.CASCADE)
    co_data= models.CharField (max_length =50, null =True, blank=True)
    o3_data= models.CharField (max_length =50, null =True, blank=True)
    no2_data= models.CharField (max_length =50, null =True, blank=True)
    pm25_data= models.CharField (max_length =50, null =True, blank=True)
    pm10_data= models.CharField (max_length =50, null =True, blank=True)
    so2_data= models.CharField (max_length =50, null =True, blank=True)

    #hourly average
    co_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    o3_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    no2_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm25_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm10_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    so2_hr_ave= models.CharField (max_length =50, null =True, blank=True)

    #8hours-average
    co_8hr_ave= models.CharField (max_length =50, null =True, blank=True)
    o3_8hr_ave= models.CharField (max_length =50, null =True, blank=True)
    so2_8hr_ave= models.CharField (max_length =50, null =True, blank=True)

    #24 hours average.
    so2_24hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm25_24hr_ave=models.CharField (max_length =50, null =True, blank=True)
    pm10_24hr_ave= models.CharField (max_length =50, null =True, blank=True)

    # IAQI data
    co_iaqi= models.CharField (max_length =50, null =True, blank=True)
    o3_iaqi= models.CharField (max_length =50, null =True, blank=True)
    no2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm25_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm10_iaqi= models.CharField (max_length =50, null =True, blank=True)
    so2_iaqi= models.CharField (max_length =50, null =True, blank=True)

    # NowCast
    pm_nowcast25= models.CharField (max_length =50, null =True, blank=True)
    pm_nowcast10= models.CharField (max_length =50, null =True, blank=True)

    #AQI
    aqi_data= models.CharField (max_length =50, null =True, blank=True)

    #other data
    log_data= models.CharField (max_length =50, null =True, blank=True)
    lat_data= models.CharField (max_length =50, null =True, blank=True)
    hgt_data= models.CharField (max_length =50, null =True, blank=True)
    tim_data= models.CharField (max_length =50, null =True, blank=True)
    battery_status_data= models.CharField (max_length =50, null =True, blank=True)
    temp_data= models.CharField (max_length =50, null =True, blank=True)
    hum_data= models.CharField (max_length =50, null =True, blank=True)

    #Monitoring Data
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
    co_data= models.CharField (max_length =50, null =True, blank=True)
    o3_data= models.CharField (max_length =50, null =True, blank=True)
    no2_data= models.CharField (max_length =50, null =True, blank=True)
    pm25_data= models.CharField (max_length =50, null =True, blank=True)
    pm10_data= models.CharField (max_length =50, null =True, blank=True)
    so2_data= models.CharField (max_length =50, null =True, blank=True)

    #hourly average
    co_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    o3_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    no2_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm25_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm10_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    so2_hr_ave= models.CharField (max_length =50, null =True, blank=True)

    #8hours-average
    co_8hr_ave= models.CharField (max_length =50, null =True, blank=True)
    o3_8hr_ave= models.CharField (max_length =50, null =True, blank=True)
    so2_8hr_ave= models.CharField (max_length =50, null =True, blank=True)

    #24 hours average.
    so2_24hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm25_24hr_ave=models.CharField (max_length =50, null =True, blank=True)
    pm10_24hr_ave= models.CharField (max_length =50, null =True, blank=True)

    # IAQI data
    co_iaqi= models.CharField (max_length =50, null =True, blank=True)
    o3_iaqi= models.CharField (max_length =50, null =True, blank=True)
    no2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm25_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm10_iaqi= models.CharField (max_length =50, null =True, blank=True)
    so2_iaqi= models.CharField (max_length =50, null =True, blank=True)

    # NowCast
    pm_nowcast25= models.CharField (max_length =50, null =True, blank=True)
    pm_nowcast10= models.CharField (max_length =50, null =True, blank=True)

    #AQI
    aqi_data= models.CharField (max_length =50, null =True, blank=True)

    #other data
    log_data= models.CharField (max_length =50, null =True, blank=True)
    lat_data= models.CharField (max_length =50, null =True, blank=True)
    hgt_data= models.CharField (max_length =50, null =True, blank=True)
    tim_data= models.CharField (max_length =50, null =True, blank=True)
    battery_status_data= models.CharField (max_length =50, null =True, blank=True)
    temp_data= models.CharField (max_length =50, null =True, blank=True)
    hum_data= models.CharField (max_length =50, null =True, blank=True)

    #Monitoring Data
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
    co_data= models.CharField (max_length =50, null =True, blank=True)
    o3_data= models.CharField (max_length =50, null =True, blank=True)
    no2_data= models.CharField (max_length =50, null =True, blank=True)
    pm25_data= models.CharField (max_length =50, null =True, blank=True)
    pm10_data= models.CharField (max_length =50, null =True, blank=True)
    so2_data= models.CharField (max_length =50, null =True, blank=True)

    #hourly average
    co_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    o3_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    no2_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm25_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm10_hr_ave= models.CharField (max_length =50, null =True, blank=True)
    so2_hr_ave= models.CharField (max_length =50, null =True, blank=True)

    #8hours-average
    co_8hr_ave= models.CharField (max_length =50, null =True, blank=True)
    o3_8hr_ave= models.CharField (max_length =50, null =True, blank=True)
    so2_8hr_ave= models.CharField (max_length =50, null =True, blank=True)

    #24 hours average.
    so2_24hr_ave= models.CharField (max_length =50, null =True, blank=True)
    pm25_24hr_ave=models.CharField (max_length =50, null =True, blank=True)
    pm10_24hr_ave= models.CharField (max_length =50, null =True, blank=True)

    # IAQI data
    co_iaqi= models.CharField (max_length =50, null =True, blank=True)
    o3_iaqi= models.CharField (max_length =50, null =True, blank=True)
    no2_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm25_iaqi= models.CharField (max_length =50, null =True, blank=True)
    pm10_iaqi= models.CharField (max_length =50, null =True, blank=True)
    so2_iaqi= models.CharField (max_length =50, null =True, blank=True)

    # NowCast
    pm_nowcast25= models.CharField (max_length =50, null =True, blank=True)
    pm_nowcast10= models.CharField (max_length =50, null =True, blank=True)

    #AQI
    aqi_data= models.CharField (max_length =50, null =True, blank=True)

    #other data
    log_data= models.CharField (max_length =50, null =True, blank=True)
    lat_data= models.CharField (max_length =50, null =True, blank=True)
    hgt_data= models.CharField (max_length =50, null =True, blank=True)
    tim_data= models.CharField (max_length =50, null =True, blank=True)
    battery_status_data= models.CharField (max_length =50, null =True, blank=True)
    temp_data= models.CharField (max_length =50, null =True, blank=True)
    hum_data= models.CharField (max_length =50, null =True, blank=True)

    #Monitoring Data
    data_no= models.CharField (max_length =50, null =True, blank=True)
    data_int= models.CharField (max_length =50, null =True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return str (self.sensor_details)
    def datano(self):
        return self.data_no
