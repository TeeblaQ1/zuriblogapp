from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'index.html'

# class BlogDetailView(DetailView):

def postDetailView(request, pk):
    # model = Post
    # template_name = 'detail.html'
    # form_class = CommentForm
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)

    new_comment = None
    # def add_comment(self, request):
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'detail.html', {'post': post, 'comments': comments,
                                                'new_comment': new_comment, 'comment_form': comment_form})

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'body']

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

