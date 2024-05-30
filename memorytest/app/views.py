# from django.shortcuts import render
# from .models import Test
# from django.db.models import Count
# import random

# def index(request):
#     return render(request, "index.html")

# def display(request):
#     items = Test.objects.order_by('?')
#     if items:
#         request.session['idnumberr']=items
#     return render(request, "display.html", {'items': items})

# def item(request):
#     count = Test.objects.aggregate(count=Count('id'))['count']
#     random_index = random.randint(0, count - 1)
#     item = Test.objects.all()[random_index]
#     return render(request, "item.html", {'item': item})

# def hidden(request):
#     items = Test.objects.order_by('?')
#     idnumber=request.session.get('idnumber')
#     print(idnumber)
#     return render(request, "hidden.html", {'items': items, 'idnumber': idnumber})
from django.shortcuts import render,redirect
from .models import Test
from django.db.models import Count
import random

def index(request):
    return render(request, "index.html")

def display(request):
    items = list(Test.objects.order_by('?'))
    if items:
        # Store item IDs and their corresponding count numbers in the session
        request.session['items'] = [item.id for item in items]
        request.session['item_numbers'] = list(range(1, len(items) + 1))
    return render(request, "display.html", {'items': items})

def item(request):
    count = Test.objects.aggregate(count=Count('id'))['count']
    random_index = random.randint(0, count - 1)
    item = Test.objects.all()[random_index]
    if item:
        request.session['num']=item.id
    return render(request, "item.html", {'item': item})

# def hidden(request):
#     item_ids = request.session.get('items', [])
#     item_numbers = request.session.get('item_numbers', [])

#     if not item_ids or not item_numbers:
#         return render(request, "hidden.html", {'items_with_numbers': []})

#     # Ensure items are fetched in the same order as stored in the session
#     items = [Test.objects.get(id=item_id) for item_id in item_ids]
#     items_with_numbers = zip(items, item_numbers)
#     # Shuffle items_with_numbers to randomize their order
#     random.shuffle(items_with_numbers)
#     return render(request, "hidden.html", {'items_with_numbers': items_with_numbers})
def hidden(request):
    item_ids = request.session.get('items', [])
    item_numbers = request.session.get('item_numbers', [])

    if not item_ids or not item_numbers:
        return render(request, "hidden.html", {'items_with_numbers': []})

    # Ensure items are fetched in the same order as stored in the session
    items = [Test.objects.get(id=item_id) for item_id in item_ids]
    items_with_numbers = list(zip(items, item_numbers))
    
    # Shuffle items_with_numbers to randomize their order
    random.shuffle(items_with_numbers)
    
    return render(request, "hidden.html", {'items_with_numbers': items_with_numbers})
def check(request, id):
    num = request.session.get('num')
    if str(num) == str(id):
        return redirect('win') # Replace with the actual view to redirect to
    else:
        return redirect('lose')

def win(request):
    return render(request,"win.html")

def lose(request):
    return render(request,"lose.html")