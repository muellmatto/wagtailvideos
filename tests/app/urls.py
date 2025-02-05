from __future__ import unicode_literals

import re

from django.conf import settings
from django.conf.urls import include
from django.urls import path, re_path
from django.views.static import serve
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls

urlpatterns = [
    path('admin/', include(wagtailadmin_urls)),
    path('', include(wagtail_urls)),
    #  For media serving
    re_path(r'^%s(?P<path>.*)$' % re.escape(
        settings.MEDIA_URL.lstrip('/')), serve, kwargs={'document_root': settings.MEDIA_ROOT})
]
