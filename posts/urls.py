from django.urls import path
from . import views
urlpatterns = [
    # path('add/', views.addPost, name='add_post'),
    path('add/', views.addPost_createView.as_view(), name='add_post'),
    # path('edit/<int:id>', views.editPost, name='edit_post'),
    path('edit/<int:id>', views.editPost_updateView.as_view(), name='edit_post'),
    # path('delete/<int:id>', views.deletePost, name='delete_post'),
    path('delete/<int:id>', views.deletePost_DeleteView.as_view(), name='delete_post'),
    path('detail/<int:id>', views.detail_view.as_view(), name='detail_post'),
]