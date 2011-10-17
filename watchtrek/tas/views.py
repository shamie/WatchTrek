from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
import random

def root(request):
    seasons = [1, 2]
    season1 = []
    season2 = []

    # creates a list of each episode in each season

    for i in range(1, 17):
	    season1.append(i)

    for i in range(1, 7):
	    season2.append(i)

    # picks and prints random season
    random.shuffle(seasons)
    season = seasons[0]
    print "Season: %d" % season

    # picks and prints random episode based on season
    if season == 1:
	    random.shuffle(season1)
	    e = season1[0]
    else:
	    random.shuffle(season2)
	    e = season2[0]
	
    return HttpResponse("Season: " + str(season) + ", Episode: " + str(e) )
