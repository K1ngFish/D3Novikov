from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from datetime import datetime
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm

from django.utils import timezone
import pytz


class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.now()
        context['open_vacancies'] = None
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.context_data['timezones'] = pytz.common_timezones
        response.context_data['current_time'] = timezone.now()
        return response

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('posts_list')

    # def get_queryset(self):
    #    queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return self.filterset.qs

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['filterset'] = self.filterset
    #    return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsApp.add_post')
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsApp.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('NewsApp.delete_post')
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')


class SearchResultsView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search_list'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_posts_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.category).order_by('-dateCreation')
        return queryset

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
       context['category'] = self.category
       return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'subscribe.html', {'category': category, 'message': message})

