from django.contrib import admin
from django.db.models.base import ModelBase
from django.conf import settings

from . import models

# register all models when debugging
if settings.DEBUG:
    for model_name in dir(models):
        model = getattr(models, model_name)
        if isinstance(model, ModelBase):
            admin.site.register(model)
