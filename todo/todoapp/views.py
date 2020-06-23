from django.shortcuts import render
from .models import goals
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):
    todo_items=goals.objects.all().order_by('-date_posted')
    context={
    'posts':todo_items
    }
    return render(request,'todoapp/home.html',context)

@csrf_exempt
def create(request):
    print(request.POST)
    date=timezone.now()
    title=request.POST['title']

    goals.objects.create(goal=title,date_posted=date)
    return HttpResponseRedirect('/')






def delete_post(request,goals_id=None):

    post_to_delete=goals.objects.get(id=goals_id)
    post_to_delete.delete()
    return HttpResponseRedirect("/")


