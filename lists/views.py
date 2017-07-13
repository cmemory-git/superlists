from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List
from django.core.exceptions import ValidationError

KEY_ENTER = b'\xEE\x80\x87'.decode()
# Create your views here.
def home_page(request):
    print("loading home\n")
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'].rstrip(KEY_ENTER), list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    trimmedInput = request.POST['item_text'].rstrip(KEY_ENTER)
    item = Item.objects.create(text=trimmedInput, list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})
    return redirect(list_)