from django.shortcuts import render

bears = [
  {'name': 'British Collectors 1907 Replica', 'material': 'brown mohair', 'description': '23.6in tall and fully jointed', 'year': 1993, 'price': '$750'},
  {'name': 'Steamboat Willie Mickey Mouse', 'material': 'Trevira velvet', 'description': '13.8in tall with white buttons and matching hat', 'year': 2019, 'price': '$380'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bears_index(request):
    return render(request, 'bears/index.html', {
        'bears': bears
    })