from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from collections import Counter
import requests
from bs4 import BeautifulSoup
import re
from django.http import HttpResponse
import json

# Create your views here.
class bruteforceView(TemplateView):
    def get(self, request):
        context = {}
        return render(request, 'bruteforce/insert.html', context)

    def wordCount(self, url):
        # Fetch the content from the URL
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Extract text and split into words
        words = re.findall(r'\b\w{3,}\b', soup.get_text().lower())
        count = Counter(words)
        return count.most_common()

    def post(self, request):
        url = request.POST.get('url')
        word_count = self.wordCount(url)
        # Convert word_count to a format suitable for JavaScript
        word_count_js = json.dumps(word_count)
        return render(request, 'bruteforce/word_count.html', {
            'word_count': word_count_js,
            'request_url': url
        })

def word_count_json_view(request):
    url = request.GET.get('url')
    if url:
        view = bruteforceView()
        word_count = view.wordCount(url)
        response = HttpResponse(json.dumps(dict(word_count)), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="word_count.json"'
        return response
    return JsonResponse({'error': 'No URL provided'})