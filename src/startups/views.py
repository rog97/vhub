from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import StartupAddForm, StartupModelForm
from .models import Startup
import requests
from requests.exceptions import HTTPError
import pycrunchbase as pyc


class StartupIndex(ListView):
    model = Startup
    # template_name = "index.html"
    #
    # def get_context_data(self, **kwargs):
    #     context = super(StartupIndex, self).get_context_data(**kwargs)
    #     context["queryset"] = self.get_queryset()
    #     return context

# class StartupDelete(DeleteView):
#     model = Startup
#     success_url = reverse_lazy('startup_list', urlconf=None, args=None, kwargs=None, current_app=None)

def startup_delete(request, pk, template_name='startups/startup_confirm_delete.html'):
    startup = get_object_or_404(Startup, pk=pk)
    if request.method=='POST':
        startup.delete()
        return redirect('startup_list')
    return render(request, template_name, {'object':startup})


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
    startup_name = str(startup.name.lower())
    if " " in startup_name:
        startup_str = "-".join(startup_name.split(" "))
    else:
        startup_str = startup_name
    template = "startup_view.html"
    context = {
        "object": startup,
        "what_is_co": get_cb_co(startup_str),
        "founders": founders(startup_str),
        "funding_rounds": funding_rounds(startup_str),
        "investors": investors(startup_str),
    }

    return render(request, template, context)

# Crunchbase API calls here ----------------------------------------------------

cb = pyc.CrunchBase('f0172d1df1ca552457f0722ed6468809')

def get_cb_co(company_name):
    try:
        company = cb.organization(company_name)
    except HTTPError:
        return "Is this even incorporated?"
    what_is_co = company.description
    # context = {
    #     "what_is_co": what_is_co,
    # }
    return what_is_co

def founders(company_name):
    try:
        company = cb.organization(company_name)
    except HTTPError:
        return "Who done it?"
    founders = company.founders
    people = list()
    people2 = list()
    for dude in founders:
        people.append(dude)

    for dude in people:
        dude = str(dude)
        bracket = dude.find('(')
        dude = dude[:bracket]
        people2.append(dude)

    ceos = ""
    for person in people2:
        ceos += person
        if person != people2[len(people2)-1]:
            ceos += ", "

    return ceos

def funding_rounds(company_name):
    try:
        company = cb.organization(company_name)
    except HTTPError:
        return "Nao!"

    funding_summary = company.funding_rounds

    i = 1
    for investment_round in funding_summary:
        round_id = investment_round.uuid
        this_round = cb.funding_round(round_id)
        investment_things = this_round.investments
        b = i
        str1 = "This company is on investment round " + str(b)
        i += 1
        this_round = str(this_round)
        amount = this_round.find('$')
        unwanted = this_round.find('o')
        str2 = "Investment for this latest round was "
        dollar = this_round[amount:unwanted-1]
        if dollar != "$NA":
            dollar = str(dollar)
        else:
            return "Investment amount unavailable"
    return str1 + "  |  " + str2 + dollar

def investors(company_name):
    try:
        company = cb.organization(company_name)
    except HTTPError:
        return ":("
    funding_summary = company.funding_rounds

    for investment_round in funding_summary:
        round_id = investment_round.uuid
        this_round = cb.funding_round(round_id)
        investment_things = this_round.investments

        round_of_fun = ""
        for investors in investment_things:
            investors = str(investors)
            org = '[Organization:'
            length = len(org)
            if org in investors:
                unwanted = investors.find(org)
                investors = investors[unwanted+len(org):-1]
            round_of_fun += investors
            # if investors != investment_things[-1]:
            round_of_fun += ", "

    if round_of_fun:
        return round_of_fun[:-2]
    else:
        return "-"
