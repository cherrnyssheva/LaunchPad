from django.shortcuts import render

from django.http.response import HttpResponse, Http404
from .models import Tag, Startup
from django.template import Context, loader
from django.shortcuts import get_object_or_404


def homepage(request):
    """tag_list = get_object_or_404(Tag.objects.all())
    template = loader.get_template('organizer/tag_list.html')
    context = {'tag_list': tag_list}
    output = template.render(context)
    return HttpResponse(output)"""
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    """try:
        tag = Tag.objects.get(slug__iexact = slug)
    except Tag.DoesNotExist:
        raise Http404
    template = loader.get_template('organizer/tag_detail.html')
    context = {'tag': tag}
    return HttpResponse(template.render(context))"""
    tag = get_object_or_404(Tag, slug__iexact = slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})


def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact = slug)
    return render(request, 'organizer/startup_detail.html', {'startup_detail': startup})