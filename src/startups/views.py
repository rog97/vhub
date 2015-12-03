from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .forms import StartupAddForm
from .models import Startup


# Create your views here.

def index(request):
    queryset = Startup.objects.all()
    template = "index.html"
    context = {
    "queryset": queryset,
    }
    return render(request, template, context)

def create_view(request):
    form = StartupAddForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        name = data.get("name")
        latest_funding = data.get("latest_funding")
        description = data.get("description")
        # Instantiate the startup
        new_startup = Startup()
        new_startup.name = name
        new_startup.latest_funding = latest_funding
        new_startup.description = description
        # Sticking it into the db
        new_startup.save()
    template = "create_view.html"
    context = {
        "form": form,
    }
    return render(request, template, context)

def startup_slug_view(request, slug=None):
    startup = Startup.objects.get(slug=slug)
    try:
        startup = get_object_or_404(Startup, slug=slug)
    except Startup.MultipleObjectsReturned:
        startup = Startup.objects.filter(slug=slug).order_by("-name").first()
    template = "startup_view.html"
    context = {
        "object": startup,
    }
    return render(request, template, context)

def startup_view(request, object_id=None):
    startup = get_object_or_404(Startup, id=object_id)
    template = "startup_view.html"
    context = {
        "object": startup,
    }
    return render(request, template, context)
