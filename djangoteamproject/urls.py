from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

# as_view()를 써야 cbv 방식을 fbv 처럼 쓸 수 있따.
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
    path('mypage/', include('my_page.urls')),
    path('board/', include('boards.urls')),
    path('comment/', include('comments.urls')),
    path('bookmark/', include('bookmarks.urls')),
    # path('messages/', include('django.contrib.messages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media 경로
