from django.shortcuts import render
import json
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from .models import SensorDetails
from .models import Sensor1Data
from .models import Sensor2Data
from .models import Sensor3Data
from .models import Sensor4Data

# Create your views here.

def introduction (request):
    return render (request, 'cfaairquality/introduction.html', {})

def about_codeforafrica (request):
    return render (request, 'cfaairquality/introduction.html', {})

    #the sensor fires a single URL to update API platform about itself. API platform return sucessful code.
    #Alternatively, can be set by Admin from websource.

def sensor_setup (request):
    if request.method == "GET":
        s = request.GET #assign the request.GET dict to 's' for futher use, to make things look simple

        #check if we have the sensor registerd before.
        k=0
        try:
            name =s['n']
        except:
            return HttpResponse ("improper request, n missing " )

        try:
            p=SensorDetails.objects.get(sensor_name=name) #if registered before, then it want to modify.
        except:
            k=1
        if k==1:

            hold_sensor_credentials = SensorDetails(sensor_name=s['n'], sensor_city=s['c'], sensor_installed=s['i'], sensor_incare_of=s['e'],
                                            sensor_organisation =s['o'],sensor_phoneno=s['p'],sensor_pollutants_var=s['va'],
                                            sensor_country=s['t'],sensor_log=s['l'],sensor_lat=s['a'],sensor_height=s['h'],
                                            sensor_data_interval=s['v'],sensor_data_owner=s['r'])
            hold_sensor_credentials.save()
            return HttpResponse ("sucessful registerd new sensor " )
        else:
            p=SensorDetails.objects.get(sensor_name=name)
            p.sensor_name=s['n']
            p.sensor_city=s['c']
            p.sensor_installed=s['i'] #please change this guy to string from model, its presently in int.
            p.sensor_incare_of=s['e']
            p.sensor_organisation =s['o']
            p.sensor_phoneno=s['p']
            p.sensor_pollutants_var=s['va']
            p.sensor_country=s['t']
            p.sensor_log=s['l']
            p.sensor_lat=s['a']
            p.sensor_height=s['h']
            p.sensor_data_interval=s['v']
            p.sensor_data_owner=s['r']
            p.save() #save

            return HttpResponse ("sucessfully edited " )


    else:
        return HttpResponse ("unsucessful " )


        #sync sensor timing with server timing.



def input_sensor_data (request):
    if request.method == "GET":
        q = request.GET #assign the request.GET dict to 'q' for futher use, to make things look simple
        hold =0 #Sensor1Data() #just hold a random data first. it will be replaced.
        former=0 # hold a random data first. it will be replaced.
        #check which of the sensors data is coming from and load appropraite object.
        try:
            q['d']=='1'

        except:
            return render (request, 'cfaairquality/sensorresponse.html', {})

        if q['s'] == '1' or q['s'] == '0' : # i am debugging dont add the timing palava.

            # we want to ensure the first data, data_no 1 starts at 00:00 to 00:15 on a particular day....................................................
            #sync data timing of sensor with that of database.
            #check if offset has been done.
            try:
                sensor_property = SensorDetails.objects.get(pk=int(q['d'].strip('"')))
            except:
                return HttpResponse ("Please add sensor")
            sync_time =sensor_property.sensor_offset_date
            #return HttpResponse ("sync_time is %s" % sync_time)

            now_time = datetime.now()

            #check if datetime corrolate to know if daily offset has been recorded.......................................................................

            if sync_time != None and sync_time.year == now_time.year and sync_time.month == now_time.month and sync_time.day ==now_time.day:
                pass
            else:
                timelist = [15,30,45,60,115,130,145,160,215,230,245,260,315,330,345,360,415,430,445,460,515,530,545,560,615,630,645,660,715,730,745,
                        760,815,830,845,860,915,930,945,960,1015,1030,1045,1060,1115,1130,1145,1160,1215,1230,1245,1260,1315,1330,1345,1360,
                        1415,1430,1445,1460,1515,1530,1545,1560,1615,1630,1645,1660,1715,1730,1745,1760,1815,1830,1845,1860,1915,1930,1945,1960,
                        2015,2030,2045,2060,2115,2130,2145,2160,2215,2230,2245,2260,2315,2330,2345,2360]

                #take time hrs and minuts and convert to string so you could check time
                h=str(now_time.hour)
                m=str(now_time.minute)

                if len(h) == 1:
                    h=str('0'+h) # because the hr and min is output as a single digit, we append 0 to it to make it work the way we want
                if len(m) == 1:
                    m=str('0'+m)

                timedata = int(h+m) # we add up the string of hours and minutes to get something like HHMM like 1759

                #return HttpResponse ("timedata is %s" % timedata)

                timetracker =1
                for times in timelist:
                    if timedata > times:
                        timetracker = timetracker + 1
                    else:
                        offset = -1 * (timetracker - int(q['dn'].strip('"'))) #q['dn'] is the data_no coming from sensor. we need to save this into a place in database so we can adjust new data with it, we negate it to get right answers for offset.
                        correct_data_no = str (int(q['dn'].strip('"')) - offset) # update the data_no with the appropraite data no that should come in at that time.
                        sensor_property.sensor_data_offset = offset #store the offest data into corresponding sensordetails space.
                        sensor_property.sensor_offset_date = datetime.now() # update the new time when sensor offset has been updated, usually ocuurs once perday.
                        #sensor_property.save() #save it. #uncomment this, only  when testing is over.


                #return HttpResponse ("the accurate datano is %s" %correct_data_no)
            #completed.................................................................................................................................
        else:
            correct_data_no = q['dn'] #for debugging purpose only, so that you can run through data number 1 to 96, remove this else and correspoding if, when set


        #check the time, we want to assign the first sensor data between 0000 to 0015 to data_no 1, even if the data_no of the reading coming at that point might not be 1
        #time = timezone.now() #take time zone of the country.
        #process time to usable format YYYYMMDDHHMMSS, then save as a list
        #if processed_time is between 00.01 and 00.15
        #Check if we have offset. offset is stored in the sensordetails corresponding to the sensor, and it is updated once a day at 00:00-00:15
        #then assign data_no to 1. i.e hold.data_no = data_no - offset.

        if q['d']=='1':
            hold = Sensor1Data() #instatiate the Sensor1Data object to hold new data to be processed, but dont save to database yet.
            former =Sensor1Data #assign the class to the name 'former' so that we can get data aleady in database
            #return HttpResponse ("what the fuck 1 %s" % str(former.objects.all()))
            hold.sensor_details = SensorDetails.objects.get(pk=int(q['d'].strip('"'))) # Assign the sensordetails instance to it.

        elif q['d']=='2':
            hold = Sensor2Data()
            former =Sensor2Data
           # return HttpResponse ("what the fuck 2 error %s" % str(former.objects.all()))
            hold.sensor_details = SensorDetails.objects.get(pk=int(q['d'].strip('"'))) # Assign the sensordetails instance to it.

        elif q['d']=='3':
            hold = Sensor3Data()
            former =Sensor3Data
           # return HttpResponse ("what the fuck 3 error %s" % str(former.objects.all()))
            hold.sensor_details = SensorDetails.objects.get(pk=int(q['d'].strip('"'))) # Assign the sensordetails instance to it.
        elif q['d']=='4':
            hold= Sensor4Data()
            former =Sensor4Data
           # return HttpResponse ("what the fuck 4 error %s" % str(former.objects.all()))
            hold.sensor_details = SensorDetails.objects.get(pk=int(q['d'].strip('"'))) # Assign the sensordetails instance to it.
        else:
            return HttpResponse ("Please add sensor:" % q['d'])

        #check for data_no, to know when to calculate IAQI's, typically calculate IAQI & AQI every hour i.e data_no multiple of 4
        #PM is every 24hrs
        #O3 is every hrs

        #gotten raw from sensor
        hold.sensor_details_id = SensorDetails.objects.get(pk=int(q['d'].strip('"'))).pk #, Because we have a foreign key of SensorDetails, we must assign the foreign key id, so tha we can have a pk here
        hold.co_data=q['c']
        hold.o3_data= q['o3']
        hold.no2_data= q['n']
        hold.pm25_data= q['p2']
        hold.pm10_data=q['p1']
        hold.so2_data=q['s']
        hold.log_data=q['lo']
        hold.lat_data=q['l']
        hold.hgt_data=q['h']
        hold.tim_data=q['t']
        hold.battery_status_data= q['b']
        hold.temp_data=q['tm']
        hold.hum_data=q['hu']
        hold.data_no= correct_data_no #ensure that this data when its 1, syncs with 12.00-12:15am
        hold.data_int=q['di']
        #hourly average
        hold.co_hr_ave= '0'
        hold.o3_hr_ave= '0'
        hold.no2_hr_ave= '0'
        hold.pm25_hr_ave= '0'
        hold.pm10_hr_ave= '0'
        hold.so2_hr_ave= '0'
        #8hours-average
        hold.co_8hr_ave= '0'
        hold.o3_8hr_ave= '0'
        hold.so2_8hr_ave= '0'
        #24 hours average.
        hold.so2_24hr_ave= '0'
        hold.pm25_24hr_ave= '0'
        hold.pm10_24hr_ave= '0'
        #Nowcast
        hold.pm_nowcast25= '0'
        hold.pm_nowcast10='0'
        #IAQI
        hold.co_iaqi='0'
        hold.o3_iaqi='0'
        hold.no2_iaqi='0'
        hold.pm25_iaqi='0'
        hold.pm10_iaqi='0'
        hold.so2_iaqi='0'
        #AQI
        hold.aqi_data='f'

        #let us know which AQi to calculate.
        calcoiaqi= False
        calpm25iaqi= False
        calpm10iaqi= False
        calpm10nowcast= False
        calpm25nowcast= False
        calaqi= False

        #hold.save()
        #return HttpResponse ("i saved")
        #return HttpResponse ("what the fuck error %s" % hold.aqi_data) #has pk =sensor_details_id, then has a sensor_details, wich is a foreign object
        #SensorDetails.objects.get(pk=int(q['d'].strip('"'))).sensor_phoneno
        #return HttpResponse ("what the fuck error %s" % hold.sensor_details_id )
        #to be calculated from raw sensor value based on data_no. (i.e every hour (15mins*60sec*4=3600secs)
        j=int(hold.data_int.strip('"')) #only int () throws this error: invalid literal for int() with base 10: and cannot convert string to float since data is coming in as '"300"'
        k=int(hold.data_no.strip('"'))
        time_to_calculate_aqi_in_secs = 3600 # calculate AQI every hour.
        if (j*k)/(k/(time_to_calculate_aqi_in_secs/j)) == time_to_calculate_aqi_in_secs: # Every 15mins.
            #return HttpResponse ("i got here %s" % hold.data_no)
            #ave1=0  ave2=0  ave3=0 #Hold freshly calculated values of averages
            data1=[]

            data2=[]
            data3=[]#Hold data extract from database

            #we need to average PM2.5 and PM10 data every 1hour, 12hrs and 24hrs. i.e since our interval is 15 mins, every 4th readings.
            #for 1 hr  we need to pull out the last X data, where X=3 if we want to average over 1 hr i.e when data_no is multiple of   4:1*4
            #for 12 hr,we need to pull out the last X data, where X=47 if we want to average over 12 hr i.e when data_no is multiple of 12:12*4.
            #for 24 hr,we need to pull out the last X data, where X=95 if we want to average over 24 hr i.e when data_no is multiple of 24:24*4.

            #we need to average CO data every 1 hrs and 8 hrs i.e since our interval is 15 mins, every 4th readings.
            #for 1 hr  we need to pull out the last X data, where X=3 if we want to average over 1 hr i.e when data_no is multiple of 4:1*4
            #for 8 hr  we need to pull out the last X data, where X=31 if we want to average over 8 hr i.e when data_no is multiple of 8:8*4.

            #code for checking what average should be calculated and it does this based on the data_no, so for data no 4,32,48,96 pull last X=3 data(min), 7 data(hr), 11 data(hr), 23 data(hr). we need to pull out data.

            #but we start measuring data from the start of the day 12.01, how do we ensure it equates to the data_no=1 provided by our sensor.
            #what we wil do is have another data_no_db, which will always set to 1 to data_no of any data coming between 00.00 and 00.15

            #get last inserted ID and get all data from last inserted ID,ID-1,ID-2 then add to the current Data and get avergae.
        if (int(hold.data_no.strip('"')) % 4 == 0): #fetch '3' data
            #notneeded1#last_data = former.objects.latest('pk').pk # Model.objects.filter().latest('pk') work fine with ordered list,like primary key. 43,42,41: (43-41)=2
            #return HttpResponse ("i got here %s" % hold.data_no)
            u = former.objects.all().order_by('-id')[:(int(hold.data_no.strip('"'))-1)] # pull the pk of last n-1 data.
            #notneeded2#for i in range ((last_data - (int(hold.data_no.strip('"'))- 2)), (last_data + 1)): #take 3 other data above the last data in database. (the 2 + 1 indicates we are taking 3), we can increase 2 to take more data, but the 1 is constant.
            for i in u: #take the primary keys
                data1.append(former.objects.get(pk=i.pk).pm25_data) #add all the data you just got from the database into a list
                data2.append(former.objects.get(pk=i.pk).pm10_data) #add all the data you just got from the database into a list
                data3.append(former.objects.get(pk=i.pk).co_data) #add all the data you just got from the database into a list
            data1.append(q['p2']) #add the latest pm25_data data coming in.
            data2.append(q['p1']) #add the latest pm25_data data coming in.
            data3.append(q['c']) #add the latest pm25_data data coming in.
            data1=[float(x.strip('"')) for x in data1] #convert them to float
            data2=[float(x.strip('"')) for x in data2] #convert them to float
            data3=[float(x.strip('"')) for x in data3] #convert them to float
            #hourly average
            hold.co_hr_ave= str(sum(data3)/len(data3))
            hold.o3_hr_ave= 'p'
            hold.no2_hr_ave= 'p'
            hold.pm25_hr_ave= str(sum(data1)/len(data1))
            hold.pm10_hr_ave= str(sum(data2)/len(data2))
            hold.so2_hr_ave= 'p'

            #check if you already have a nowcast, so that you can calculate it. After you got the first value.

            if hold.data_no =='32' or hold.data_no =='64' or hold.data_no=='96': #fetch 31 data for CO
                #last_data = former.objects.latest('pk').pk # Model.objects.filter().latest('pk') work fine with ordered list,like primary key. 43,42,41: (43-41)=2
                u = former.objects.all().order_by('-id')[:(int(hold.data_no.strip('"'))-1)] # pull the pk of last n-1 data.
                #for i in range ((last_data - (int(hold.data_no.strip('"'))- 2)), (last_data + 1)): #take 3 other data above the last data in database. (the 30 + 1 indicates we are taking 31), we can increase 2 to take more data, but the 1 is constant.
                for i in u: #take the primary keys
                    data3.append(former.objects.get(pk=i.pk).co_data) #add all the data you just got from the database into a list
                    data3.append(q['c']) #add the latest pm25_data data coming in.
                    data3=[str(x) for x in data3]
                    data3=[float(x.strip('"')) for x in data3] #convert them to float
                    #8hours-average
                hold.co_8hr_ave= str(sum(data3)/len(data3))
                hold.o3_8hr_ave= 'a'
                hold.so2_8hr_ave= 'a'
                #caclate AQI
                calcoiaqi= True
                calaqi= True


            if int(hold.data_no.strip('"')) >= 48 and int(hold.data_no.strip('"'))<= 95: #fetch data for calculating PM NowCast from the 12th hr upward
                #last_data = former.objects.latest('pk').pk # Model.objects.filter().latest('pk') work fine with ordered list,like primary key. 43,42,41: (43-41)=2
                #data1.append(former.objects.get(pk=(last_data - (int(hold.data_no.strip('"'))- 2))).pm25_data) #add all the data you just got from the database into a list
                #data2.append(former.objects.get(pk=(last_data - (int(hold.data_no.strip('"'))- 2))).pm10_data) #add all the data you just got from the database into a list
                u = former.objects.all().order_by('-id')[:(int(hold.data_no.strip('"'))-1)] # pull the pk of last n-1 data.
                #for i in range ((last_data - (int(hold.data_no.strip('"'))- 2) + 4), (last_data + 1), 4): # Here i am taking interval of 4 i.e: 8, 12, 16. so the formulashould givefor i in range(1+4,48,4), print(i-1), after the loop which ends 48                    data1.append(former.objects.get(pk=(i-1)).pm25_data) #add all the data you just got from the database into a list
                for i in u: #take the primary keys
                    data1.append(former.objects.get(pk=i.pk).pm25_hr_ave) #add all the data you just got from the database into a list
                    data2.append(former.objects.get(pk=i.pk).pm10_hr_ave) #add all the data you just got from the database into a list
                data1.append(q['p2']) #add the latest pm25_data data coming in which is the 48th data
                data2.append(q['p1']) #add the latest pm25_data data coming in which is the 48th data
                data1=[str(x) for x in data1] #convert them to float
                data2=[str(x) for x in data2] #convert them to float

                data1=[float(x.strip('"')) for x in data1] #convert them to float
                data2=[float(x.strip('"')) for x in data2] #convert them to float
                #Nowcast
                #find the Max and Min
                w25=min(data1)/max(data1)
                w10=min(data2)/max(data2)
                if w25 > 0.5:
                    datan=[]
                    dataw=[]
                    for i in range (1,13):
                        datan.append((w25**i) * data1[i-1])
                        dataw.append(w25**i)
                    hold.pm_nowcast25= str(sum(datan)/sum(dataw))
                elif w25 <= 0.5:
                    w25=0.5
                    datan=[]
                    dataw=[]
                    for i in range (1,13):
                        datan.append((w25**i) * data1[i-1])
                    hold.pm_nowcast25= str(sum(datan))
                if w10 > 0.5:
                    datan=[]
                    dataw=[]
                    for i in range (1,13):
                        datan.append((w10**i) * data1[i-1])
                        dataw.append(w10**i)
                    hold.pm_nowcast10= str(sum(datan)/sum(dataw))
                elif w10 <= 0.5:
                    w25=0.5
                    datan=[]
                    dataw=[]
                    for i in range (1,13):
                        datan.append((w10**i) * data1[i-1])
                    hold.pm_nowcast10= str(sum(datan))
                    #hold.pm_nowcast25= sum(data2)/len(data2)

                calpm10nowcast= True
                calpm25nowcast= True
                calaqi= True

            if hold.data_no == '96': #fetch 95 data
                #last_data = former.objects.latest('pk').pk # Model.objects.filter().latest('pk') work fine with ordered list,like primary key. 43,42,41: (43-41)=2
                u = former.objects.all().order_by('-id')[:(int(hold.data_no.strip('"'))-1)] # pull the pk of last n-1 data.
                #for i in range ((last_data - (int(hold.data_no.strip('"'))- 2)), (last_data + 1)): #take 3 other data above the last data in database. (the 94 + 1 indicates we are taking 95), we can increase 2 to take more data, but the 1 is constant.
                for i in u: #take the primary keys
                    data1.append(former.objects.get(pk=i.pk).pm25_data) #add all the data you just got from the database into a list
                    data2.append(former.objects.get(pk=i.pk).pm10_data) #add all the data you just got from the database into a list
                    data3.append(former.objects.get(pk=i.pk).co_data) #add all the data you just got from the database into a list
                data1.append(q['p2']) #add the latest pm25_data data coming in.
                data2.append(q['p1']) #add the latest pm25_data data coming in.
                data3.append(q['c']) #add the latest pm25_data data coming in.
                data1=[float(str(x).strip('"')) for x in data1] #convert them to float
                data2=[float(str(x).strip('"')) for x in data2] #convert them to float
                data3=[float(str(x).strip('"')) for x in data3] #convert them to float
                #24 hours average.
                hold.so2_24hr_ave= 'y'
                hold.pm25_24hr_ave= str(sum(data1)/len(data1))
                hold.pm10_24hr_ave= str(sum(data2)/len(data2))
                calpm25iaqi= True
                calpm10iaqi= True
                calaqi= True

            if calaqi==False:
                try:
                    hold.save() #save the 15 mins data
                except:
                    return HttpResponse ("didnt save to database 1st" )

                return HttpResponse ("Hourly average added" )

        else:
            try:
                hold.save() #save the 15 mins data
            except:
                return HttpResponse ("didnt save to database 2nd" )

            return HttpResponse ("15mins average data added" )

        if calaqi==True :
            #PM2.5 Breakpoint Conceentration C_low & C_high and corresponding AQI for C over a 24 hrs average.
            pm25_breakpoint_for_c =[[0.0, 12, 0, 50],\
                                    [12.1, 35.4, 51, 100],\
                                    [35.5, 55.4, 101, 150],\
                                    [55.5, 150.4, 151, 200],\
                                    [150.5, 250.4, 201, 300],\
                                    [250.5, 350.4, 301, 400],\
                                    [350.5, 500.4, 401, 500] ]

            #PM10 Breakpoint Conceentration C_low & C_high and corresponding AQI for C over a 24 hrs average.
            pm10_breakpoint_for_c =[[0, 54, 0, 50],\
                                    [55, 154, 51, 100],\
                                    [155, 254, 101, 150],\
                                    [255, 354, 151, 200],\
                                    [355, 424, 201, 300],\
                                    [425, 504, 301, 400],\
                                    [505, 604, 401, 500] ]

            #C0 Breakpoint Conceentration C_low & C_high and corresponding AQI for C over a 8 hrs average.
            CO_breakpoint_for_c =[[0.0, 4.4, 0, 50],\
                                    [4.5, 9.4, 51, 100],\
                                    [9.5, 12.4, 101, 150],\
                                    [12.5, 15.4, 151, 200],\
                                    [15.5, 30.4, 201, 300],\
                                    [30.5, 40.4, 301, 400],\
                                    [40.5, 50.4, 401, 500] ]
            # AQI = Air quality Index
            # C = the pollutant concentration
            # CL=  the concentration breakpoint that is ≤ C
            # CH=  the concentration breakpoint that is ≥ C
            # IH = the index breakpoint corresponding to C_high
            # IL = the index breakpoint corresponding to C_low


            if calcoiaqi ==True:
                temp1_pm_nowcast10=0
                temp2_pm_nowcast25=0
                aqi_data=0

                if float(hold.co_8hr_ave.strip('"')) > 50.4:
                    hold.co_iaqi= 500
                else:
                    for breakpoint in CO_breakpoint_for_c:
                        if breakpoint[0] <= float(hold.co_8hr_ave.strip('"')) <= breakpoint[1]:
                            CL = breakpoint[0]
                            CH = breakpoint[1]
                            IL = breakpoint[2]
                            IH = breakpoint[3]
                            hold.co_iaqi =(((IH-IL)/(CH-CL))*(float(hold.co_8hr_ave.strip('"'))-CL))+IL


                            if float(hold.co_iaqi)>aqi_data:
                                aqi_data=hold.co_iaqi

                if calpm25iaqi== True:
                    if float(hold.pm25_24hr_ave.strip('"')) > 500.4:
                        hold.pm25_iaqi= 500
                    else:
                        for breakpoint in pm25_breakpoint_for_c:
                            if breakpoint[0] <= float(hold.pm25_24hr_ave.strip('"')) <= breakpoint[1]:
                                CL = breakpoint[0]
                                CH = breakpoint[1]
                                IL = breakpoint[2]
                                IH = breakpoint[3]
                                hold.pm25_iaqi = (((IH-IL)/(CH-CL))*(float(hold.pm25_24hr_ave.strip('"'))-CL))+IL

                                if float (hold.pm25_iaqi)>aqi_data:
                                    aqi_data=hold.pm25_iaqi

                if calpm10iaqi== True:
                    if float(hold.pm10_24hr_ave.strip('"')) > 604:
                        hold.pm10_iaqi= 500
                    else:
                        for breakpoint in pm10_breakpoint_for_c:
                            if breakpoint[0] <= float(hold.pm10_24hr_ave.strip('"')) <= breakpoint[1]:
                                CL = breakpoint[0]
                                CH = breakpoint[1]
                                IL = breakpoint[2]
                                IH = breakpoint[3]
                                hold.pm10_iaqi = (((IH-IL)/(CH-CL))*(float(hold.pm10_24hr_ave.strip('"'))-CL))+IL
                                if float(hold.pm10_iaqi)>aqi_data:
                                    aqi_data=hold.pm10_iaqi

                if calpm10nowcast== True:
                    if float(hold.pm_nowcast10.strip('"')) > 604:
                        temp1_pm_nowcast10= 500
                    else:
                        for breakpoint in pm10_breakpoint_for_c:
                            if breakpoint[0] <= float(hold.pm_nowcast10.strip('"')) <= breakpoint[1]:
                                CL = breakpoint[0]
                                CH = breakpoint[1]
                                IL = breakpoint[2]
                                IH = breakpoint[3]
                                temp1_pm_nowcast10 = (((IH-IL)/(CH-CL))*(float(hold.pm_nowcast10.strip('"'))-CL))+IL
                                if temp1_pm_nowcast10>aqi_data:
                                    aqi_data=temp1_pm_nowcast10

                if calpm25nowcast== True:
                    if float(hold.pm_nowcast25.strip('"')) > 500.4:
                        temp2_pm_nowcast25= 500
                    else:
                        for breakpoint in pm25_breakpoint_for_c:
                            if breakpoint[0] <= float(hold.pm_nowcast25.strip('"')) <= breakpoint[1]:
                                CL = breakpoint[0]
                                CH = breakpoint[1]
                                IL = breakpoint[2]
                                IH = breakpoint[3]
                                temp2_pm_nowcast25 = (((IH-IL)/(CH-CL))*(float(hold.pm_nowcast25.strip('"'))-CL))+IL
                                if temp2_pm_nowcast25>aqi_data:
                                    aqi_data=temp2_pm_nowcast25

                #get highest AQI number and make overall AQI.

                hold.aqi_data= aqi_data

            hold.save()
            return HttpResponse ("Hourly data added and calculated AQI" )

        else:
            hold.save()
            return HttpResponse ("Hourly data added but no AQI calculated" )

        #very important to get GMT time and in string.  from time import gmtime, strftime
        #strftime("%Y-%m-%d %H:%M:%S", gmtime())

#///////

    else:
        return HttpResponse ("Which type of request is this " )


def output_data (request):
    sensor_data = Sensor1Data.objects.all()
    return render (request, 'cfaairquality/displaytable.html', {'sensor_data':sensor_data})

def output_sensors_details (request):
    sensor_details = SensorDetails.objects.all()
    return render (request, 'cfaairquality/displaydetails.html', {'sensor_details':sensor_details})

def get_aqi_data (request):
    #get the dateandtime, when request came in.
    sensor_aqi = Sensor1Data.objects.get(pk=136)
    #data= serializers.serialize("json", [sensor_aqi]), content_type="application/json")
    data= serializers.serialize("json", [sensor_aqi,])
    data2=json.loads(data)
    data = json.dumps(data2[0])
    return HttpResponse(data, content_type="application/json")
    #return HttpResponse(serializers.serialize("json", [sensor_aqi]), content_type="application/json")

# Ajax call
def get_aqi_data1(request):
    if request.GET(): #os request.GET()
        sensor_aqi = Sensor1Data.objects.get(pk=136)
        #data= serializers.serialize("json", [sensor_aqi]), content_type="application/json")
        data= serializers.serialize("json", [sensor_aqi,]) #[] to select only the first vale, should be remove when you need to send all objects
        data2=json.loads(data)
        data = json.dumps(data2[0])
        return JsonResponse(data)

def get_aqi_data2 (request):
    users = Sensor1Data.objects.all().values()  # or simply .values() to get all fields
    users_list = list(users)  # important: convert the QuerySet to a list object
    return JsonResponse(users_list, safe=False)

#control section.
def remotely_control_sensor (request):
    return render (request, 'cfaairquality/introduction.html', {})

#APIs to get sensor information from this platform
def json_data_sensor (request):
    return render (request, 'cfaairquality/introduction.html', {})