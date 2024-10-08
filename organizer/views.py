from django.shortcuts import render

from django.http.response import HttpResponse
from .models import Tag
from django.template import Context, loader


def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = {'tag_list': tag_list}
    output = template.render(context)
    return HttpResponse(output)


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact = slug)
    template = loader.get_template('organizer/tag_detail.html')
    context = {'tag': tag}
    output = template.render(context)
    return HttpResponse(output)

