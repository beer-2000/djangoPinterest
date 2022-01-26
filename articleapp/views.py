from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views import generic

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super(). form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'







#class customHandler404(generic.View):
#    def get(self, request, *args, **kwargs):
#        return render(request, "404.html")

