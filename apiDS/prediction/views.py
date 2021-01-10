from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import valeursForm
from django.urls import reverse
from django.shortcuts import redirect
from .modelPickle import modelDecisionTree, modelRandomForest


def Pred(request):

    if request.method == 'POST':
        form = valeursForm(request.POST)
        if form.is_valid():
            #date=form.cleaned_data['date']
            #rentCount=form.cleaned_data['rentCount']
            hour=form.cleaned_data['hour']
            temperature=form.cleaned_data['temperature']
            humidity=form.cleaned_data['humidity']
            windSpeed=form.cleaned_data['windSpeed']
            visibility=form.cleaned_data['visibility']
            dewPointTemp=form.cleaned_data['dewPointTemp']
            solarRadiation=form.cleaned_data['solarRadiation']
            rainfall=form.cleaned_data['rainfall']
            snowfall=form.cleaned_data['snowfall']
            seasons=form.cleaned_data['seasons']
            holiday=form.cleaned_data['holiday']
            functDay=form.cleaned_data['functDay']

            if holiday == True:
                holiday = 1

            else:
                holiday = 0
                
            if functDay == True:
                functDay = 1
            else:
                functDay = 0

            if seasons == "Winter":
                seasons = 0
            elif seasons == "Spring":
                seasons = 1
            elif seasons == "Summer":
                seasons = 2
            else:
                seasons = 3
                
            line = [[hour,temperature,humidity,windSpeed,visibility,dewPointTemp,solarRadiation,rainfall,snowfall,seasons,holiday,functDay]]
            print(line)
            predicted = modelDecisionTree.predict(line)
            print(predicted)
            request.session['predTree'] = predicted[0]

            predictedForest = modelRandomForest.predict(line)
            request.session['predForest'] = predictedForest[0]


            return redirect('http://127.0.0.1:8000/result')
        else:
            print("form non valide")

    form = valeursForm()
    return render(request, 'index.html', {'form': form})

def Result(request):
    context = {'predictedTree' : request.session['predTree'],
                'predictedForest' : request.session['predForest']}
    return render(request, 'result.html', context) 