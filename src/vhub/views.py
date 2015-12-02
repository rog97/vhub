from django.shortcuts import render


# def index(request):
#     return render(request, "index.html", {})

def news(request):
    return render(request, "news.html", {})

def analytics(request):
    return render(request, "analytics.html", {})
