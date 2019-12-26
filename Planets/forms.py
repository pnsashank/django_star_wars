from django import forms

class PlanetForm(forms.Form):
    planet_name = forms.CharField(max_length=50)                  #defining the maximum characters the form field can accept

    def clean(self):                                                #To access and validate the fields in the form
        cleaned_data = super(PlanetForm, self).clean()
        planet_name = cleaned_data.get('planet_name')
        if(not planet_name):
            raise forms.ValidationError('You have to write something!')    #Exception when form is not filled
