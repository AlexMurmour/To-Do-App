from django import forms 

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, widget =forms.TextInput(
        attrs= { 'class':'form-control', 'placeholder': 'Напишите задание, например Стирка', 'aria-label':'Todo', 'aria-describedby':'add-btn'}))