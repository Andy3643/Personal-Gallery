from django.shortcuts import render
from .models import Image
# Create your views here.
def index(request):
    image = Image.objects.all()
    return render (request,'index.html', {'image':image})

def search_images (request):
    """
    method to display users search results
    """
    if 'images' in request.GET and request.GET['images']:
        searched_category = request.GET.get('images')
        searched_images = Image.search_image_by_category(searched_category)
        message = f'{searched_category}'
        context = {
            "searched_images":searched_images,
            "message":message
        }
        return render(request,'search.html',context)

    else:
        message = "Input a relevant search"
        return render(request,'search.html',{"message":message})