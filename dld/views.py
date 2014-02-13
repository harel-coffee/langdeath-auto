from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import RequestContext, loader

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic

from dld.models import Language
from dld.forms import LanguageSearchForm


class LanguageListView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'languages'
    
    def get_queryset(self):
        return Language.objects.order_by('-last_updated')


class NewsView(generic.ListView):
    template_name = 'news.html'
    context_object_name = 'latest_updated_langs'
    
    def get_queryset(self):
        return Language.objects.order_by('-last_updated')


class LanguageDetailsView(generic.DetailView):
    template_name = 'detail.html'
    model = Language
    

class AboutUsView(generic.TemplateView):
    template_name = 'about.html'


class SearchResultsView(generic.ListView):
    template_name = 'index.html'
    model = Language


def index(request):
    context = {'languages': Language.objects.order_by('-last_updated')}
    return render(request, 'index.html', context)

def search(request):
    #if request.method == 'POST':
        #form = LanguageSearchForm(request.POST)
        #if form.is_valid():
            #langs = form.get_results()
    #try:
        #name = request.POST['name']
    #except:
        #return render(request, 'search.html', {
        #})
    #else:
        #langs = Language.objects.filter(name__startswith=name)
        #context = {'languages': langs}
        #return render(request, 'index.html', context)
#
    if request.method == 'POST':
        form = LanguageSearchForm(request.POST)
        if form.is_valid():
            langs = form.get_languages()
            #t = loader.get_template('index.html')
            #c = RequestContext(request, {'languages': langs})
            context = {'languages': langs}
            return render(request, 'index.html', context)
            return HttpResponseRedirect(t.render(c), content_type="application/xhtml+xml")
    else:
        form = LanguageSearchForm()
    return render(request, 'search.html', {'form': form})


