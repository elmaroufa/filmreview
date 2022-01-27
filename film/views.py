from django.shortcuts import render
from .models import Film, Review
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .forms import ReviewForm

# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchFilm') 
    if searchTerm:
        films = Film.objects.filter(title__icontains=searchTerm)
    else:
        films = Film.objects.all()
    return render(request, 'home.html', {'name': 'ABBO', 'searchTerm': searchTerm, 'films': films})


def about(request):
    return render(request,'about.html')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    reviews = Review.objects.filter(film=film)
    return render(request,'detail.html',{'film':film, 'reviews':reviews})

def createreview(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method == 'GET':
        return render(request, 'createreview.html',
          {'form': ReviewForm(), 'film' : film})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.film = film
            newReview.save()
            return redirect('detail', newReview.film.id)
        except ValueError:
            return render(request, 'createreview.html',
            {'form' : form, 'error' : 'bad data passed in' })


def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method =='GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html',
                      {'review': review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.film.id)            
        except ValueError:
            return render(request, 'updatereview.html',
             {'review': review,'form':form,'error':'Bad data in form'})

def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.film.id)   

