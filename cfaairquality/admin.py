from django.contrib import admin
from .models import SensorDetails
from .models import Sensor1Data
from .models import Sensor2Data
from .models import Sensor3Data
from .models import Sensor4Data

# Register your models here.
admin.site.register (SensorDetails)
admin.site.register (Sensor1Data)
admin.site.register (Sensor2Data)
admin.site.register (Sensor3Data)
admin.site.register (Sensor4Data)
