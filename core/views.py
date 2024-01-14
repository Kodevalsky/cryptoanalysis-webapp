from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class homeView(TemplateView):
    def get(self, request):
        context = {}
        return render(request, 'core/home.html', context)