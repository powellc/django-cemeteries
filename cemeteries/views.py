from django.shortcuts import get_list_or_404, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.decorators import login_required
from cemeteries.models import Cemetery, Monument
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

import datetime

def cemetery_index(request):
    cemeteries=Cemetery.objects.all()
    return render_to_response('cemeteries/cemetery_index.html', locals(),
                              context_instance=RequestContext(request))

def cemetery_detail(request, slug):
    cemetery=Cemetery.objects.get(slug=slug)
    return render_to_response('cemeteries/cemetery_detail.html', locals(),
                              context_instance=RequestContext(request))

def monument_index(request, cemetery_slug):
    cemetery=Cemetery.objects.get(slug=cemetery_slug)
    monuments=Monument.objects.filter(cemetery=cemetery)
    return render_to_response('cemeteries/monument_index.html', locals(),
                              context_instance=RequestContext(request))

def monument_detail(request, cemetery_slug, slug):
    cemetery=Cemetery.objects.get(slug=cemetery_slug)
    monument=Monument.objects.filter(cemetery=cemetery, slug=slug)
    return render_to_response('cemeteries/monument_detail.html', locals(),
                              context_instance=RequestContext(request))
