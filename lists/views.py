from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item

KEY_ENTER = b'\xEE\x80\x87'.decode()
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        trimmedInput = request.POST['item_text'].rstrip(KEY_ENTER)
        Item.objects.create(text = trimmedInput)
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})