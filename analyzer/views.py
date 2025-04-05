import math
import re
from collections import Counter
from django.shortcuts import render, redirect
from .forms import DocumentForm


def calculate_tf_idf(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    total_words = len(words)

    if not total_words:
        return []

    word_counts = Counter(words)

    # Рассчитываем TF и IDF
    results = []
    for word, count in word_counts.items():
        tf = count / total_words
        idf = math.log(total_words / count)
        results.append({
            'word': word,
            'tf': round(tf, 4),
            'idf': round(idf, 4)
        })

    # Сортируем по IDF (убывание) и берём топ-50
    results.sort(key=lambda x: (-x['idf'], x['word']))
    return results[:50]


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()

            file_content = document.file.read().decode('utf-8')

            analysis_results = calculate_tf_idf(file_content)

            return render(request, 'analyzer/results.html', {
                'results': analysis_results
            })
    else:
        form = DocumentForm()
    return render(request, 'analyzer/upload.html', {'form': form})
