from django.shortcuts import render, redirect
from .models import Review
import datetime

# Create your views here.
def index(request):
    data = Review.objects.all()
    return render(request, "reviews/index.html", {"data": data})


def detail(request, _id):
    data = Review.objects.get(id=_id)

    return render(request, "reviews/detail.html", {"data": data})


def write(request):
    _title = request.GET.get("title")
    _content = request.GET.get("content")

    Review.objects.create(title=_title, content=_content)

    return redirect("reviews:index")


def update(request, _id):
    target = Review.objects.get(id=_id)

    target.title = request.GET.get("title")
    target.content = request.GET.get("content")
    target.updated_at = datetime.date.today()

    target.save()

    return redirect("reviews:detail", _id)


def delete(request, _id):
    Review.objects.get(id=_id).delete()

    return redirect("reviews:index")
