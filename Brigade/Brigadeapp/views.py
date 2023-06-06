import mimetypes
import os
from django.shortcuts import render, redirect

from django.http.response import HttpResponse
# from .forms import LocationForm
from .models import know_your_locality,walkthrough,amenities,enquire_now,overview,locality_map,gallery, Logo


def registration(request):
    if request.method=="POST":
        post=enquire_now()
        post.first_name=request.POST['first_name']
        post.Last_name=request.POST['last_name']
        post.Mobile_number=request.POST['mobile_number']
        post.email=request.POST['email']
        post.enquiry_type = request.POST['form_type']
        
        post.save()
        return redirect("index")
    else:
        return redirect("index")


def index(request):
    pc_overview=overview.objects.first()
    lc_map=locality_map.objects.first()
    logos = Logo.objects.first()
    gallery_objects = gallery.objects.all()
    # img=gallery.objects.all()
    locality = know_your_locality.objects.all()
    video = walkthrough.objects.first()
    source=amenities.objects.all()
    print("GAllery: ", gallery_objects)
    return render(request, "index.html", {"sources":source,"galleries": gallery_objects, "localities": locality,
                                          "video": video.video,"overview":pc_overview,"lc_map":lc_map.location,
                                          "logos": logos})







def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'test.txt'
    filepath = BASE_DIR + '/Brigadeapp/Files/' + filename
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    
    