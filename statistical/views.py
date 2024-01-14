from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class statisticalView(TemplateView):
    def get(self, request):
        context = {}
        return render(request, 'statistical/insert.html', context)