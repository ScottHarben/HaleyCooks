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

def bananaberry(request):
    return render(request,'subscribe/bananaberry.html')

def cocostrawberry(request):
    return render(request,'subscribe/cocostrawberry.html')

def fruitstand(request):
    return render(request,'subscribe/fruitstand.html')

def margarita(request):
    return render(request,'subscribe/margarita.html')

def lemonsoda(request):
    return render(request,'subscribe/lemonsoda.html')

def toothpick(request):
    return render(request,'subscribe/toothpick.html')

def about(request):
    return render(request,'subscribe/about.html')

def form(request):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'subscribe/form.html',{'chicken':form})
