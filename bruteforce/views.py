from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class bruteforceView(TemplateView):
    def get(self, request):
        context = {}
        return render(request, 'bruteforce/insert.html', context)