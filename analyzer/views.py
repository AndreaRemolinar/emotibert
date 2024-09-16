# views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .sentiment import predict_sentiment
from .translate import translate_sentiment
from .neutralize import neutralize_text, sentiment_words  # Asegúrate de tener este archivo

def sentiment_analysis(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        prediction = predict_sentiment(text)
        return render(request, 'analyzer/index.html', {'prediction': prediction, 'original_text': text})
    else:
        return render(request, 'analyzer/index.html')

def translate_view(request):
    if request.method == 'POST':
        text = request.POST['text']
        sentiment = request.POST['sentiment']
        translated_text = translate_sentiment(text, sentiment)
        return HttpResponse(translated_text)
    return render(request, 'index.html')

def neutralize_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        neutral_text = neutralize_text(text, sentiment_words)
        return JsonResponse({'neutral_text': neutral_text})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
