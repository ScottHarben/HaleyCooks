from django.conf.urls import url
from subscribe import views

app_name = 'subscribe'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^form/', views.form, name="form"),
    url(r'^meals/', views.meals, name="meals"),
    url(r'^smoothies/', views.smoothies, name="smoothies"),
    url(r'^cocktails/', views.cocktails, name="cocktails"),
    url(r'^pan/', views.pan, name="pan"),
    url(r'^peachcobbler/', views.peachcobbler, name="peachcobbler"),
    url(r'^berrypie/', views.berrypie, name="berrypie"),
    url(r'^bananaberry/', views.bananaberry, name="bananaberry"),
    url(r'^cocostrawberry/', views.cocostrawberry, name="cocostrawberry"),
    url(r'^fruitstand/', views.fruitstand, name="fruitstand"),
    url(r'^margarita/', views.margarita, name="margarita"),
    url(r'^lemonsoda/', views.lemonsoda, name="lemonsoda"),
    url(r'^toothpick/', views.toothpick, name="toothpick"),
    url(r'^about/', views.about, name="about"),
]
