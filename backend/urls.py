from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from audit_engine.views import dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🌟 YEH WALI LINE MISSING THI: Main website ka link template se jor diya
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    
    # API Link Connection
    path('api/v1/scan/', scan_document),
]