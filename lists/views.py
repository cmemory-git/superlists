from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from lists.models import Item, List
from lists.forms import ItemForm

KEY_ENTER = b'\xEE\x80\x87'.decode()
# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'].rstrip(KEY_ENTER), list=list_)
            return redirect(list_)

    return render(request, 'list.html', {'list': list_, 'form': form})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        trimmedInput = request.POST['text'].rstrip(KEY_ENTER)
        item = Item.objects.create(text=trimmedInput, list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})