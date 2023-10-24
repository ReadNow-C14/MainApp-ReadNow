from django.shortcuts import render

# Create your views here.
def show_main(request):

    context = {
        'aplikasi': 'ReadNow',
        'class': 'PBP C',
    }

    return render(request, "main.html", context)