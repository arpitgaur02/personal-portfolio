from django.shortcuts import render


def home(httprequest):
    print(httprequest.method)
    return render(httprequest, "pages/home.html", {})
