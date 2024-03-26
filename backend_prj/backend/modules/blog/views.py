from django.views.generic import ListView, DetailView

from .models import Article

from django.shortcuts import render
from django.core.paginator import Paginator

def articles_list(request, page):
    articles = Article.objects.all()
    paginator = Paginator(articles, per_page=2)
    page_object = paginator.get_page(page)
    context = {'page_obj': page_object}
    return render(request, 'blog/articles_func_list.html', context)

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/articles_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    qs = Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/articles_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context