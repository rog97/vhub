from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
import requests
from requests.exceptions import HTTPError
import soundcloud

# Create your views here.
def podcast(request):
    client=soundcloud.Client(client_id='82e2e587553e349d06053f4a676657f4')
    track_url = 'http://soundcloud.com/akharris/startup-school-radio-ep-24-sam-altman-and-aarjav-trivedi'
    embed_info = client.get('/oembed', url=track_url)
    da_src = embed_info.html
    da_src = da_src[71:234].strip()
    context = {
        'embed': embed_info,
        'da_code': da_src,
        }
    return render(request, 'studio.html', context )

    # def make_it_html(html_str):
