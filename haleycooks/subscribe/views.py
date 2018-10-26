from django.shortcuts import render
from subscribe.forms import EmailForm

# Create your views here.
def index(request):
    return render(request,'subscribe/index.html')

def meals(request):
    return render(request,'subscribe/meals.html')

def smoothies(request):
    return render(request,'subscribe/smoothies.html')

def cocktails(request):
    return render(request,'subscribe/cocktails.html')

def pan(request):
    return render(request,'subscribe/pan.html')

def peachcobbler(request):
    return render(request,'subscribe/peachcobbler.html')

def berrypie(request):
    return render(request,'subscribe/berrypie.html')

def form(request):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'subscribe/form.html',{'chicken':form})
