from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Aphorism


class AphorismMixin():
    model = Aphorism
    fields = '__all__'

    def get_success_url(self):
        auth_user_id = self.request.user.id
        return reverse_lazy('aphorisms:user_aphorism_list', kwargs={'user_id': auth_user_id})


class AphorismListView(ListView):
    user_id = 0
    tag_id = 0
    paginate_by = 10
    model = Aphorism

    # order by 'id' DESC
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.user_id
        context['tag_id'] = self.tag_id

        return context

    def get_queryset(self):
        query = super().get_queryset()

        if 'user_id' in self.request.resolver_match.kwargs:

            self.user_id = self.request.resolver_match.kwargs['user_id']
            query = query.filter(author_id=self.user_id)

        if 'user_id' in self.request.GET:
            query = query.filter(author_id=self.request.GET['user_id'])

        if 'tag_id' in self.request.GET:
            self.tag_id = self.request.GET['tag_id']
            query = query.filter(tags__id=self.tag_id)

        return query


class AphorismCreateView(AphorismMixin, CreateView):
    fields = ('text', 'tags')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AphorismUpdateView(AphorismMixin, UpdateView):
    fields = ('text', 'tags')

    def get_queryset(self):
        return Aphorism.objects.filter(author_id=self.request.user.pk)


class AphorismDeleteView(AphorismMixin, DeleteView):
    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(author_id=self.request.user.pk)
        return query
