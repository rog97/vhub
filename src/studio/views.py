from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
import requests
from requests.exceptions import HTTPError
import random
import soundcloud

# Create your views here.
def podcast(request):
    client=soundcloud.Client(client_id='82e2e587553e349d06053f4a676657f4')
    random_number = random.randint(1,20)
    if random_number == 1:
        track_url = 'https://soundcloud.com/a16z/ipos-public-private-valuations'
    elif random_number == 2:
        track_url = 'http://soundcloud.com/akharris/startup-school-radio-ep-24-sam-altman-and-aarjav-trivedi'
    elif random_number == 3:
        track_url = 'https://soundcloud.com/a16z/lean-startups'
    elif random_number == 4:
        track_url = 'https://soundcloud.com/a16z/scaling-ideas-and-startups-in-the-uk-and-europe'
    elif random_number == 5:
        track_url = 'https://soundcloud.com/a16z/the-power-of-open-source-systems-software'
    elif random_number == 6:
        track_url = 'https://soundcloud.com/a16z/a16z-podcast-when-cars-and-technology-collide'
    elif random_number == 7:
        track_url = 'https://soundcloud.com/bothsidestv/matt-mazzeo'
    elif random_number == 8:
        track_url = 'https://soundcloud.com/akharris/startup-school-radio-ep-4-plangrid-campus-job'
    elif random_number == 9:
        track_url = 'https://soundcloud.com/a16z/a16z-podcast-taking-the-pulse-of-vc-and-tech-dan-primack-interviews-marc-andreessen'
    elif random_number == 10:
        track_url = 'https://soundcloud.com/a16z/a16z-podcast-the-rise-of-the-quasi-ipo'
    elif random_number == 11:
        track_url = 'https://soundcloud.com/a16z/a16z-podcast-the-marketplace-rules'
    elif random_number == 12:
        track_url = 'https://soundcloud.com/akharris/startup-school-radio-ep-1-alexis-ohanian-kaz-nejatian'
    elif random_number == 13:
        track_url = 'https://soundcloud.com/bothsidestv/ryan-hoover'
    elif random_number == 14:
        track_url = 'https://soundcloud.com/akharris/startup-school-radio-ep-15-ryan-hoover-harry-zhang'
    elif random_number == 15:
        track_url = 'https://soundcloud.com/akharris/startup-school-ep-6-marco-zappacosta-sanjay-dastoor'
    elif random_number == 16:
        track_url = 'https://soundcloud.com/bothsidestv/fred-wilson'
    elif random_number == 17:
        track_url = 'https://soundcloud.com/bothsidestv/sam-rosen-ceo-of-makespace-bothsides-tv-ep-7-with-mark-suster'
    elif random_number == 18:
        track_url = 'https://soundcloud.com/bothsidestv/jeff-clavier'
    elif random_number == 19:
        track_url = 'https://soundcloud.com/venture-studio/ep-02-ben-lerer-thrillist-lerer-ventures'
    else:
        track_url = 'https://soundcloud.com/venture-studio/ep-11-stephanie-palmeri-softtechvc'
    embed_info = client.get('/oembed', url=track_url)
    da_src = embed_info.html
    da_src = da_src[71:234].strip()

    context = {
        'embed': embed_info,
        'da_code': da_src,
        }
    return render(request, 'studio.html', context )
