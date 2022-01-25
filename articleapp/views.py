from django.shortcuts import render

from django.views import generic

# Create your views here.

class customHandler404(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, "404.html")