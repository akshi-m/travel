
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SinglePage/cat=<str:cat>', views.SinglePage.as_view()),
    path('index', views.Index.as_view()),
    path('', views.SignIn.as_view()),
    path('AboutView', views.AboutView.as_view()),
    path('feedback', views.FeedbackView.as_view()),
    path('traveldesk', views.TraveldeskView.as_view()),
    path('owner', views.Owner.as_view()),
    path('signup/', views.SignUp.as_view()),
    path('activate/<uid64>/<token>', views.activate, name='activate'),
    path('login/', views.SignIn.as_view()),
    path('approve/id=<int:id>', views.Approve.as_view()),

    path('signout/', views.SignOut.as_view()),
    path('message', views.MessageView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
