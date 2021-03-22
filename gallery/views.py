from django.shortcuts import render
from .models import Image
import datetime as dt

# Create your views here.

def index (request):
     title = 'Welcome to the gallery'
     date = dt.date.today()
     pgallery = Image.objects.all()

     return render(request,'index.html',{"gallery":gallery})

def image(request, image_id):
      try:
            image = Image.objects.get(id = image_id)
      except Gallery.DoesNotExist:
            raise Http404()

      return render(request,"image.html", {"image":image})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term=request.GET.get("category")
        searched_categories=Category.search_by_name(search_term) 
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"categories":searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message}) 

