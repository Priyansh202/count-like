

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Count

def index(request):
   
   context= Count.objects.all()
    
   return render(request, 'index.html', {'context':context})

@csrf_exempt
def update_count(request):
    post = Count.objects.first()
    if request.method == 'POST':
        if request.POST['action'] == 'like':
            post.likes += 1
            post.save()
        elif request.POST['action'] == 'dislike':
            post.dislikes += 1
            post.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
