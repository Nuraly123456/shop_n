from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
                  path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
                  path('secureadmin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('store/', include('store.urls')),
                  path('cart/', include('carts.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('orders/', include('orders.urls')),

                  # Добавьте эти новые пути для политик
                  path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
                  path('terms-of-use/', views.terms_of_use, name='terms_of_use'),
                  path('shipping-payment/', views.shipping_payment, name='shipping_payment'),
                  path('returns/', views.returns, name='returns'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)