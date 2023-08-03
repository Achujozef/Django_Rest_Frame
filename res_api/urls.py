

from django.urls import path
from .views import PostView,Post_Details,PostAPIView,DetailsAPIView,genericApiView

urlpatterns = [
    # path('posts/',PostView),
    # path('details/<int:pk>',Post_Details)

    #path('postsAPIView/',PostAPIView.as_view()),
    #path('detailsAPIView/<int:pk>',DetailsAPIView.as_view())
    path('genericsApiView/',genericApiView.as_view()),
    path('genericsApiView/<int:id>/',genericApiView.as_view())
]
