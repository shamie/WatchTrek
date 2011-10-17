from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
import random

def root(request):
    seasons = [1, 2, 3, 4]
    season1 = []
    season2 = []
    season3 = []
    season4 = []

    # creates a list of each episode in each season
    for i in range(1, 26):
	    season1.append(i)

    for i in range(1, 27):
	    season2.append(i)

    for i in range(1, 25):
	    season3.append(i)
	
    for i in range(1, 23):
	    season4.append(i)

    random.shuffle(seasons)
    season = seasons[0]

    if season == 1:
	    random.shuffle(season1)
	    e = season1[0]
    elif season == 2:
	    random.shuffle(season2)
	    e = season2[0]
    elif season == 3:
	    random.shuffle(season3)
	    e = season3[0]
    else:
	    random.shuffle(season4)
	    e = season4[0]
	    
    return HttpResponse("Season: " + str(season) + ", Episode: " + str(e) )
