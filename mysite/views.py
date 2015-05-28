from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse
import settings

def index(request):
    myapps = []
    for app in settings.INSTALLED_APPS:
        if not app.startswith('django'):
            myapps.append(app);
    return render(request, 'mysite/index.html',
                  {'myapps': myapps})