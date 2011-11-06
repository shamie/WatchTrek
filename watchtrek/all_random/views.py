from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
import random

def root(request):
    def TOS():
	    seasons = [1, 2, 3]
	    season1 = []
	    season2 = []
	    season3 = []

	    for i in range(1, 31):
		    season1.append(i)

	    for i in range(1, 27):
		    season2.append(i)

	    for i in range(1, 25):
		    season3.append(i)

	    random.shuffle(seasons)
	    season = seasons[0]
	    
	    if season == 1:
		    random.shuffle(season1)
		    e = season1[0]
	    elif season == 2:
		    random.shuffle(season2)
		    e = season2[0]
	    else:
		    random.shuffle(season3)
		    e = season3[0]

    return HttpResponse("The Original Series, Season: " + str(season) + ", Episode: " + str(e))		

    def TAS():
	    seasons = [1, 2]
	    season1 = []
	    season2 = []

	    for i in range(1, 17):
		    season1.append(i)

	    for i in range(1, 7):
		    season2.append(i)

	    random.shuffle(seasons)
	    season = seasons[0]
	    
	    if season == 1:
		    random.shuffle(season1)
		    e = season1[0]
	    else:
		    random.shuffle(season2)
		    e = season2[0]

    return HttpResponse("The Animated Series, Season: " + str(season) + ", Episode: " + str(e) )
    
    def TNG():
	    seasons = [1, 2, 3, 4, 5, 6, 7]
	    season1 = []
	    season2 = []
	    season3 = []
	    season4 = []
	    season5 = []
	    season6 = []
	    season7 = []

	    for i in range(1, 27):
		    season1.append(i)

	    for i in range(1, 23):
		    season2.append(i)

	    for i in range(1, 27):
		    season3.append(i)
	
	    for i in range(1, 27):
		    season4.append(i)

	    for i in range(1, 27):
		    season5.append(i)

	    for i in range(1, 27):
		    season6.append(i)
	
	    for i in range(1, 27):
		    season7.append(i)

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
	    elif season == 4:
		    random.shuffle(season4)
		    e = season4[0]
	    elif season == 5:
		    random.shuffle(season5)
		    e = season5[0]
	    elif season == 6:
		    random.shuffle(season6)
		    e = season6[0]
	    else:
		    random.shuffle(season7)
		    e = season7[0]
        
    return HttpResponse("The Next Generation, Season: " + str(season) + ", Episode: " + str(e) )
    
    def DS9():
	    seasons = [1, 2, 3, 4, 5, 6, 7]
	    season1 = []
	    season2 = []
	    season3 = []
	    season4 = []
	    season5 = []
	    season6 = []
	    season7 = []

	    for i in range(1, 21):
		    season1.append(i)

	    for i in range(1, 27):
		    season2.append(i)

	    for i in range(1, 27):
		    season3.append(i)

	    for i in range(1, 27):
		    season4.append(i)

	    for i in range(1, 27):
		    season5.append(i)

	    for i in range(1, 27):
		    season6.append(i)

	    for i in range(1, 27):
		    season7.append(i)

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
	    elif season == 4:
		    random.shuffle(season4)
		    e = season4[0]
	    elif season == 5:
		    random.shuffle(season5)
		    e = season5[0]
	    elif season == 6:
		    random.shuffle(season6)
		    e = season6[0]
	    else:
		    random.shuffle(season7)
		    e = season7[0]
	
    return HttpResponse("Deep Space Nine, Season: " + str(season) + ", Episode: " + str(e) )
		    
    def VOY():
	    seasons = [1, 2, 3, 4, 5, 6, 7]
	    season1 = []
	    season2 = []
	    season3 = []
	    season4 = []
	    season5 = []
	    season6 = []
	    season7 = []

	    for i in range(1, 17):
		    season1.append(i)

	    for i in range(1, 27):
		    season2.append(i)

	    for i in range(1, 27):
		    season3.append(i)
	
	    for i in range(1, 27):
		    season4.append(i)

	    for i in range(1, 27):
		    season5.append(i)

	    for i in range(1, 27):
		    season6.append(i)
	
	    for i in range(1, 27):
		    season7.append(i)

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
	    elif season == 4:
		    random.shuffle(season4)
		    e = season4[0]
	    elif season == 5:
		    random.shuffle(season5)
		    e = season5[0]
	    elif season == 6:
		    random.shuffle(season6)
		    e = season6[0]
	    else:
		    random.shuffle(season7)
		    e = season7[0]
    return HttpResponse("Voyager, Season: " + str(season) + ", Episode: " + str(e) )
    
    def ENT():
	    seasons = [1, 2, 3, 4]
	    season1 = []
	    season2 = []
	    season3 = []
	    season4 = []

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
		
    return HttpResponse("Enterprise, Season: " + str(season) + ", Episode: " + str(e) )

    which_series = ["The Original Series","The Animated Series", "The Next Generation","Deep Space Nine","Voyager", "Enterprise"]

    random.shuffle(which_series)
    series = which_series[0]

    if series == "The Original Series":
	    TOS()
    elif series == "The Animated Series":
	    TAS()
    elif series == "The Next Generation":
	    TNG()
    elif series == "Deep Space Nine":
	    DS9()
    elif series == "Voyager":
	    VOY()
    else:
	    ENT()
