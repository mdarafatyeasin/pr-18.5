from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_categories(request):
    if request.method == "POST":
        category_form = forms.addCategories(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form = forms.addCategories()
    return render(request, 'add_categories.html', {'form':category_form})