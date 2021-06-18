from django.shortcuts import render
from app.models import *
from django.db.models import Q
from django.views.generic import ListView


class SearchResultsView(ListView):
    model = Image
    template_name = 'search_results.html'
    

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = Image.objects.filter(
            Q(title__icontains=query)
        )
        return object_list

def category(request, id):
    context = {}
    a = Category.objects.get(id=id)
    context["images"] = a.images.order_by("id")

    return render(request, "category.html", context)


def index(request):
    context = {}
    context["images"] = Image.objects.all().order_by('-id')

    return render(request, "index.html", context)

def image_detail(request, id):
    context = {}
    context["image"] = Image.objects.get(id=id)

    return render(request, "image_detail.html", context)
