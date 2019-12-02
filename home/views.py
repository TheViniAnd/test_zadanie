from django.shortcuts import render
from .models import Mod
from django.utils import timezone


def pub_det(request):
    mods = Mod.objects.filter(date_added__lte=timezone.now()).order_by('-date_added')
    return render(request, 'list.html',{'mod':mods})
