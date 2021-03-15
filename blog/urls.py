from django.urls import path
from .views import (BlogList,
                    BlogDetail,
                    CreateBlog,
                    UpdateBlog,
                    DeleteBlog,
)


app_name = 'blog'


urlpatterns = [
    path('', BlogList.as_view(), name='list'),
    path('<slug>', BlogDetail.as_view(), name='detail'),
    path('<slug>/delete/', CreateBlog.as_view(), name='delete'),
    path('<slug>/update/', UpdateBlog.as_view(), name='update'),
    path('create/', DeleteBlog.as_view(), name='create'),
]

