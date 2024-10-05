from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Circle
from .forms import CircleForm

def home(request):
    circles = Circle.objects.all()
    return render(request, 'circles/home.html', {'circles': circles})

@login_required
def create_circle(request):
    if request.method == 'POST':
        form = CircleForm(request.POST)
        if form.is_valid():
            circle = form.save(commit=False)
            circle.creator = request.user
            circle.save()
            circle.members.add(request.user)
            return redirect('home')
    else:
        form = CircleForm()
    return render(request, 'circles/create_circle.html', {'form': form})

@login_required
def join_circle(request, circle_id):
    circle = Circle.objects.get(id=circle_id)
    circle.members.add(request.user)
    return redirect('home')

# leave circle
@login_required
def leave_circle(request, circle_id):
    circle = Circle.objects.get(id=circle_id)
    circle.members.remove(request.user)
    return redirect('home')

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'