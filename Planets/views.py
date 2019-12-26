from django.shortcuts import render
from .forms import PlanetForm
from django.http import HttpResponse
from django.views import View
from .models import Planet
from fuzzywuzzy import fuzz
import requests

def home(request):
    form=PlanetForm(request.POST)
    if(form.is_valid()):
        if(request.method == 'POST'):                                        #checking whether request was a POST request
            planet_name=form.cleaned_data['planet_name']                     #extract planet name submitted
        if(Planet.objects.filter(planet_name=planet_name).exists()):
            print(Planet.objects.filter(planet_name=planet_name).exists())
            planet_object=Planet.objects.get(planet_name=planet_name)          #If planet name exits in local store extract the object from 'Planet' database
            planet_details_dict={'name':planet_object.planet_name,'rotation_period':planet_object.rotation_period,'orbital_period':planet_object.orbital_period,'gravity':planet_object.gravity,'films':planet_object.films,'Result':'Exact Match'} #data to be rendered to template
            return render(request,'Planets/results.html',planet_details_dict)

        else:
            api_url_part='?search='+planet_name
            url='https://swapi.co/api/planets/'+api_url_part                  #If planet name does not exists in the local store extract the object
            swapi_reponse=requests.get(url)
            swapi_reponse_json=swapi_reponse.json()                           #JSON response from swapi
            if(swapi_reponse_json['results']!=[]):
                if(planet_name==swapi_reponse_json['results'][0]['name']):
                    planet_name=swapi_reponse_json['results'][0]['name']         #update planet_name to the planet name in the swap_response_json data
                    if(swapi_reponse_json['results'][0]['films']!=[]):
                        swapi_reponse_films_urls=swapi_reponse_json['results'][0]['films']   #if films key is not empty traverse through the urls, to extract film names
                        films=""
                        for film_url in swapi_reponse_films_urls:
                            swapi_reponse_film_url=requests.get(film_url)
                            film=swapi_reponse_film_url.json()['title']
                            films+=film+', '
                    else:
                        films='Not Known'
                    planet_details_dict={'name':swapi_reponse_json['results'][0]['name'],'rotation_period':swapi_reponse_json['results'][0]['rotation_period'],'orbital_period':swapi_reponse_json['results'][0]['orbital_period'],'gravity':swapi_reponse_json['results'][0]['gravity'],'films':films,'Result':'Exact Match'}             #data to be rendered to template
                    return render(request,'Planets/results.html',planet_details_dict)
                else:
                    planet_name=swapi_reponse_json['results'][0]['name']         #update planet_name to the planet name in the swap_response_json data
                    if(swapi_reponse_json['results'][0]['films']!=[]):
                        swapi_reponse_films_urls=swapi_reponse_json['results'][0]['films']   #if films key is not empty traverse through the urls, to extract film names
                        films=""
                        for film_url in swapi_reponse_films_urls:
                            swapi_reponse_film_url=requests.get(film_url)
                            film=swapi_reponse_film_url.json()['title']
                            films+=film+', '
                    else:
                        films='Not Known'
                                                                               #if film key is empty
                    planet_details_dict={'name':swapi_reponse_json['results'][0]['name'],'rotation_period':swapi_reponse_json['results'][0]['rotation_period'],'orbital_period':swapi_reponse_json['results'][0]['orbital_period'],'gravity':swapi_reponse_json['results'][0]['gravity'],'films':films,'Result':'Fuzzy Match'}             #data to be rendered to template
                    return render(request,'Planets/results.html',planet_details_dict)
            else:                                                                       #if planet name is not there either in local store or swapiTests
                final_match_value=0                                                     #holds the ratio of string match with planets in local store
                received_planet_name=planet_name
                if(Planet.objects.all().exists()):                                      #Planet name received from form
                    for planet in Planet.objects.all():
                        match_value=fuzz.token_sort_ratio(planet_name,planet.planet_name)   #Computes the match ration between the planet names
                        if(match_value>final_match_value):                                  #update the planet name and the ratio
                            final_match_value=match_value
                            received_planet_name=planet.planet_name
                    planet_object=Planet.objects.get(planet_name=received_planet_name)
                    planet_details_dict={'name':planet_object.planet_name,'rotation_period':planet_object.rotation_period,'orbital_period':planet_object.orbital_period,'gravity':planet_object.gravity,'films':planet_object.films,'Result':'Fuzzy match'}                    #holds the data renderd to template
                    return render(request,'Planets/results.html',planet_details_dict)             #data rendered to template to be displayed
                else:
                    return HttpResponse("<h1>Not Found</h1>")


    else:
        form = PlanetForm()
        return render(request,'Planets/home.html',{'form':form})                          #reload the form if data is invalid

def database_addition(request):                                                           #if data to be added to database through a button click
    gravity=request.POST.get('gravity')
    films=request.POST.get('films')
    rotation_period=request.POST.get('rotation_period')
    orbital_period=request.POST.get('orbital_period')
    name=request.POST.get('name')
    if(Planet.objects.filter(planet_name=name).exists()):
        return HttpResponse("<h1>Already Added to Database</h1>")                          #if data in already in database return the response
    else:
        p=Planet(planet_name=name,rotation_period=rotation_period,orbital_period=orbital_period,gravity=gravity,films=films)  #data to be added to Planet database
        p.save()                      #save the changes                                                       

        return HttpResponse("<h1>Added to database</h1>")                               #return the response once data added to database

def local_store(request):
    all_planets=Planet.objects.all()                                                      #extract all the data from Planet database
    all_planets_info={'all_planets':all_planets}                                          #data to be rendered to template
    return render(request,'Planets/store.html',all_planets_info)
