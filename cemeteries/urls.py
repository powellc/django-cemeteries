
from django.conf import settings
from django.conf.urls.defaults import *
from cemeteries.models import Cemetery, Monument 
from cemeteries import views

# custom views vendors
urlpatterns = patterns('cemeteries.views',
     url(r'cemeteries/$', view=views.cemetery_index, name="boat_index"),
     url(r'cemeteries/(?P<slug>[-\w]+)/$', view=views.cemetery_detail, name="cemetery_detail"),

     url(r'cemeteries/(?P<slug>[-\w]+)/monuments/$', view=views.monument_index, name="monument_index"),
     url(r'cemeteries/(?P<cemetery_slug>[-\w]+)/monuments/(?P<slug>[-\w]+)/$$', view=views.monument_detail, name="monument_detail"),
)

