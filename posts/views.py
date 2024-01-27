from typing import Any
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator

# Create your views here.
# add
@login_required
def addPost (request):
    if request.method == 'POST':
        post_form = forms.add_post(request.POST)
        if post_form.is_valid:
            messages.success(request, "post added")
            post_form.instance.author = request.user
            post_form.save()
            return redirect('homePage')
    else:
        post_form = forms.add_post()
    return render (request, 'add_post.html', {'form':post_form})

# edit
@login_required
def editPost (request, id):
    post = Post.objects.get(pk=id)
    post_form = forms.add_post(instance=post)
    if request.method == 'POST':
        post_form = forms.add_post(request.POST, instance=post)
        if post_form.is_valid:
            messages.success(request, "Post updated")
            post_form.save()
            return redirect('homePage')
    return render (request, 'edit_post.html', {'form':post_form})

# delete
@login_required
def deletePost(request, id):
    post = Post.objects.get(pk = id)
    messages.warning(request, f"{post.title} delete success")
    post.delete()
    return redirect('profile')


# ---------------------------------------------- class based views ------------------------------------------------------ #
# add
@method_decorator(login_required, name='dispatch')
class addPost_createView(CreateView):
    model = Post
    form_class = forms.add_post
    template_name = 'add_post.html'
    success_url = reverse_lazy('homePage')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# edit
@method_decorator(login_required, name='dispatch')
class editPost_updateView(UpdateView):
    model = Post
    form_class = forms.add_post
    template_name = 'add_post.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

# delete
@method_decorator(login_required, name='dispatch')
class deletePost_DeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

# detail
class detail_view(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'detail_post.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comment.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


