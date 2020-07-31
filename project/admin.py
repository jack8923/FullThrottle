from django.contrib import admin
from django.db import models

from .models import (Members, Activity_Periods)


class Activity_periodAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateTimeField: {'input_formats': ('%m/%d/%Y',)},
    }


admin.site.register(
    (
        Members,
        Activity_Periods,
    )
)
