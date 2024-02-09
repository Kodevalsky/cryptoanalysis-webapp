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
        # Get the uploaded file
        uploaded_file = request.FILES.get('exclusion_file')
        word_length = request.POST.get('wordLength') 
        print(type(uploaded_file))
        words_to_exclude = self.handle_uploaded_file(uploaded_file) if uploaded_file else set()
        url = request.POST.get('url')
        init_word_count = self.wordCount(url)
        word_count = [(word, count) for word, count in init_word_count if word not in words_to_exclude and len(word) >= int(word_length)]
        print(words_to_exclude)
        word_count_js = json.dumps(word_count)
        return render(request, 'bruteforce/word_count.html', {
            'word_count': word_count_js,
            'request_url': url
        })
    def handle_uploaded_file(self, f):
        words_to_exclude = [line.decode('utf-8').strip() for line in f.readlines()]
        return set(words_to_exclude) 

def word_count_json_view(request):
    url = request.GET.get('url')
    if url:
        view = bruteforceView()
        word_count = view.wordCount(url)
        response = HttpResponse(json.dumps(dict(word_count)), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="word_count.json"'
        return response
    return JsonResponse({'error': 'No URL provided'})