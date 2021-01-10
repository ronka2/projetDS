from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class valeursForm(forms.Form):
    #date=forms.CharField(max_length=12,required=False, label="Date (dd/mm/yyyy):")
    #rentCount=forms.FloatField(required=False)
    hour=forms.FloatField(required=False, label="Hour of the day(0-24):")
    temperature=forms.FloatField(required=False, label="Temperature(°C):")
    humidity=forms.FloatField(required=False, label="Humidity(%):")
    windSpeed=forms.FloatField(required=False, label="Wind speed(m/s):")
    visibility=forms.FloatField(required=False, label="Visibility(m):")
    dewPointTemp=forms.FloatField(required=False, label="Dew point temperature(°C):")
    solarRadiation=forms.FloatField(required=False, label="Solar Radiation(MJ/m2):")
    rainfall=forms.FloatField(required=False, label="Rainfall(mm):")
    snowfall=forms.FloatField(required=False, label="Snowfall(cm):")
    seasons=forms.ChoiceField(choices=[('Winter','Winter'),('Summer','Summer'),('Spring','Spring'),('Automn','Automn')],required=False, label="Seasons:")
    holiday=forms.BooleanField(required=False)
    functDay=forms.BooleanField(required=False, label="Function day")

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.helper = FormHelper
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            'hour',
            'temperature',
            'humidity',
            'windSpeed',
            'visibility',
            'dewPointTemp',
            'solarRadiation',
            'rainfall',
            'snowfall',
            'seasons',
            'holiday',
            'functDay',
            Submit('submit', 'Submit', css_class='btn-succes')
        )