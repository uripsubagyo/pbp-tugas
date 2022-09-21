from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'list_watch' : data_watchlist,
        'nama': 'I Made Urip Subagyo',
    }
    return render(request, "mywatchlist.html", context)

def show_html_mywatchlist(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'list_watch' : data_watchlist,
    }
    return render(request, "mylist.html", context)    

def show_html_id_mywatchlist(request, id):
    data_watchlist = MyWatchList.objects.filter(pk=id)
    context = {
        'list_watch' : data_watchlist,
    }
    return render(request, "mylist.html", context)    

def show_json_mywatchlist(request):
    data_watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def show_json_id_mywatchlist(request, id):
    data_watchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def show_xml_mywatchlist(request):
    data_watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_xml_id_mywatchlist(request, id):
    data_watchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")




