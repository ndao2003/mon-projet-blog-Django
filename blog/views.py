from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article
# Liste des articles
class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"
# Détail d'un article

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"
# Créer un nouvel article
class ArticleCreateView(CreateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ["titre", "contenu", "auteur", "image"]
    success_url = reverse_lazy("article_list")

# Modifier un article
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ["titre", "contenu", "auteur", "image"]
    success_url = reverse_lazy("article_list")

# Supprimer un article
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("article_list")



