from django import forms
from .models import Classes
from django.forms import ModelForm, widgets

# class CreateForm(forms.Form):
#     name = forms.CharField(label='Class Title', max_length=200, )
#     faculty = forms.CharField(label='Faculty', max_length=200, )
#     url = forms.BooleanField()
#     time = forms.TimeField(label='Time',)


class MyTimeField(forms.TimeInput):
    input_type = 'time'


class CreateForm(ModelForm):
    class Meta:
        model = Classes
        exclude = ["user"]
        widgets = {"class_time": MyTimeField, }
        # fields = '__all__'


# class DayForm(ModelForm):
#     class Meta:
#         model = Classes
#         exclude = ["user", "Monday", "Tuesday", "Wednesday",
#                    "Thursday", "Friday", "Saturday", "Sunday"]
#         # fields = '__all__'


# class DayForm(ModelForm):
#     class Meta:
#         model = Day
#         exclude = ["class_name"]
#         widgets = {"class_day": forms.CheckboxSelectMultiple(),

#                    }
