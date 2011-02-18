from django.contrib.gis import admin
from cemeteries.models import Cemetery, Monument 

admin.site.register(Cemetery)
admin.site.register(Monument)
