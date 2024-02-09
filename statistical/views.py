from django.shortcuts import render
from django.views.generic import TemplateView
from collections import defaultdict


# Create your views here.
class statisticalView(TemplateView):
    def get(self, request):
        context = {}
        return render(request, 'statistical/insert.html', context)
    
    def post(self, request):
        original_text = request.POST.get('originalText')
        ciphertext = request.POST.get('ciphertext')
        
        # Assuming 'count_enabled' or similar functionality might be used here
        count_enabled = request.POST.get('count_enabled')
        
        keypairs = []
        keypair_count = []
        char_occurrences = defaultdict(int) # For tracking occurrences of each original text character
        
        # First, count occurrences of each character
        for char in original_text:
            char_occurrences[char] += 1
        
        # Then, populate keypairs and their counts
        for num, char in enumerate(original_text):
            if (char, ciphertext[num]) not in keypairs:
                keypairs.append((char, ciphertext[num]))
                keypair_count.append(1)
            else:
                index = keypairs.index((char, ciphertext[num]))
                keypair_count[index] += 1
        
        # Calculate probabilities
        keypair_probabilities = []
        for keypair, count in zip(keypairs, keypair_count):
            total_occurrences = char_occurrences[keypair[0]]
            probability = count / total_occurrences
            keypair_probabilities.append(probability)
        
        for num, element in enumerate(keypair_probabilities):
            keypair_probabilities[num] = element * 100
            
        # Combine data into one list
        keypair_data = zip(keypairs, keypair_count, keypair_probabilities)
        
        return render(request, 'statistical/keypairs.html', context={'keypair_data': keypair_data})