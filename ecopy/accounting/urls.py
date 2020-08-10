from accounting import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [url(r"^$", views.StartView.as_view(), name="home")] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
