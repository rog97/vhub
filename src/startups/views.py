from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .forms import StartupAddForm, StartupModelForm
from .models import Startup
import pycrunchbase as pyc

class StartupIndex(ListView):
    model = Startup
    # template_name = "index.html"
    #
    # def get_context_data(self, **kwargs):
    #     context = super(StartupIndex, self).get_context_data(**kwargs)
    #     context["queryset"] = self.get_queryset()
    #     return context

    def get_queryset(self, *args, **kwargs):
        query = super(StartupIndex, self).get_queryset(**kwargs)
        # query = query.filter(name__icontains="Startup")
        return query

def index(request):
    queryset = Startup.objects.all()
    template = "index.html"
    context = {
    "queryset": queryset,
    }
    return render(request, template, context)

def get_cb_co(company_name):
    cb = pyc.CrunchBase('f0172d1df1ca552457f0722ed6468809')
    company = cb.organization(company_name)
    what_is_co = company.description
    context = {
        "what_is_co": what_is_co,
    }
    return what_is_co


def create_view(request):
    form = StartupModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    template = "form.html"
    context = {
        "form": form,
        "submit_btn": "Add Startup",
    }
    return render(request, template, context)

def update_view(request, object_id=None):
    startup = get_object_or_404(Startup, id=object_id)
    form = StartupModelForm(request.POST or None, instance=startup)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    template = "form.html"
    context = {
        "object": startup,
        "form": form,
        "submit_btn": "Update Startup",
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
    print('----')
    startup_str = str(startup.name.lower())
    template = "startup_view.html"
    context = {
        "object": startup,
        "what_is_co": get_cb_co(startup_str),
    }

    return render(request, template, context)
