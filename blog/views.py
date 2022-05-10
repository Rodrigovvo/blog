from datetime import datetime
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View, generic

from blog.forms import CommentCreateForm
from .models import Post, Comment


class PostList(generic.ListView):
    """
    Return all published posts.
    """
    queryset = Post.objects.filter(
        publication_date__lte=datetime.now(), 
        active=True
    ).order_by('-publication_date')
    template_name = 'index.html'
    paginate_by = 5


class PostDetail(generic.DetailView):
    """
    Return a detail for a post.
    """
    model = Post
    template_name = 'post_detail.html'
    commnet_form = CommentCreateForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        initial_data = {
            'post': self.object, 
            'comment_author':'Your name', 
            'content':'Your Comment'
        }

        context['comments'] = Comment.objects.filter(post=self.object, active=True).order_by('-like')
        context['form'] = kwargs.get('form') if kwargs.get('form') else self.commnet_form(initial=initial_data)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.commnet_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=self.get_object().slug)
            
        else:
            kwargs['form'] = form
        return self.get(request, *args, **kwargs)


class LikeView(View):
    """
    Like a comment
    """
    def post(self, request, *args, **kwargs):
        comment_id = json.loads(request.body).get('comment_id')
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.like_comment()
        return JsonResponse({"like": comment.like}, status=200)


class DislikeView(View):
    """
    Dislike a comment
    """
    def post(self, request, *args, **kwargs):
        comment_id = json.loads(request.body).get('comment_id')
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.dislike_comment()
        return JsonResponse({"dislike": comment.dislike}, status=200)
