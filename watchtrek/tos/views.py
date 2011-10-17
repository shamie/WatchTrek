from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
import random


def root(request):
        
    seasons = [1, 2, 3]
    season1 = []
    season2 = []
    season3 = []

    # creates a list of each episode in each season
    # may want to simplify for later series with more seasons

    for i in range(1, 31):
        season1.append(i)

    for i in range(1, 27):
        season2.append(i)

    for i in range(1, 25):
        season3.append(i)

    random.shuffle(seasons)
    season = seasons[0]
    print "Season: %d" % season

    if season == 1:
        random.shuffle(season1)
        e = season1[0]
    elif season == 2:
        random.shuffle(season2)
        e = season2[0]
    else:
        random.shuffle(season3)
        e = season3[0]

    return HttpResponse("Season: " + str(season) + ", Episode: " + str(e) )

