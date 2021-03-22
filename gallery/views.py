from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def mygallery(request):
    date = dt.date.today()
    photos = Image.get_all()
    return render(request, 'all-pics/home.html', {"date": date, "photos":photos})
