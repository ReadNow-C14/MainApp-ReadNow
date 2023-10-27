from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from review_buku.forms import ReviewForm
from review_buku.models import Review
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse
from book.models import Book
import datetime

def show_review(request):
    review_data = Review.objects.all()
    review_form = ReviewForm()
    user = request.user

    context = {
        'list_of_review': review_data,
        'review_form': review_form,
        'user_loggedin': user.username,
    }
    
    return render(request, 'review_buku.html', context)

def review_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@login_required(login_url='/login/')
@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        book_rev = Book.objects.get(pk=request.POST.get("id"))
        user = request.user
        date = datetime.date.today()
        new_review = Review(user=user, book=book_rev, comment=comment, date=date)
        new_review.save()
        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()
