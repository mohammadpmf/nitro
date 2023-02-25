from django.shortcuts import render

def show_homepage(request):
    return render(request, 'home_page.html')

def show_amir(request):
    context = { 'name': "Amir A'layi" }
    return render(request, 'amir.html', context)

def show_ali(request):
    context = { 'mylist': [10,20,30,40,50,60]}
    return render(request, 'ali.html', context)

def show_abbas(request):
    context = {
        'teachers': ('Fallah', 'Motamed', 'Hajipour', 'Bakhshandeh', 'Ramezanzadeh', 'Pourghadiri', 'Pourghalam bor', 'Babayi'),
        'students': ['Alavi', 'Niazi', 'Shekari', 'Ahmadi'],
        'objects': [
            {'name': 'Mohsen', 'family': 'Ebrahimzadeh'},
            {'name': 'Mohammad', 'family': 'Esfahani'},
            {'name': 'Behnam', 'family': 'Bani'},
            ],
    }
    return render(request, 'abbas.html', context)
