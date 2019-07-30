import csv, io
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from blog.models import PostForms
from .forms import lessonPlan
from django.views.generic.detail import DetailView



def postform(request):
    name = User.objects.first()
    if request.method == 'POST':
        form = lessonPlan(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.name = request.user
            lesson.save()
        '''title_p = request.POST.get('title')
        name = request.user
        lt = request.POST.get('ls')
        gq = request.POST.get('question')
        presentation_p = request.POST.get('presentation')
        background_p = request.POST.get('background')
        pt = request.POST.get('perfTask')
        quiz_p = request.POST.get('quiz')
        vocab_p = request.POST.get('vocab')
        wiki_p = request.POST.get('wiki')

        p = PostForms(title=title_p, name=request.user, ls=lt, question=gq, presentation=presentation_p,
        background=background_p, perfTask=pt, quiz=quiz_p, vocab=vocab_p, wiki=wiki_p)
        p.save()'''

        return redirect('blog')
    else:
        form = lessonPlan()
        return render(request, 'blog/postform.html', {'form': form})

def posts(request, pk):
    post = PostForms.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        posts = PostForms.objects.filter(ls__icontains=query_string)
        context = {
            'query_string': query_string,
            'posts': posts
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'blog/blog.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })

def blog_download(request):

    items = PostForms.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="blog.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['title', 'name','ls', 'question', 'presentation','background',
    'perfTask','quiz', 'vocab', 'wiki'])

    for obj in items:
        writer.writerow([obj.title, obj.name, obj.ls, obj.question, obj.presentation, obj.background,
        obj.perfTask, obj.quiz, obj.vocab, obj.wiki])

    return response
