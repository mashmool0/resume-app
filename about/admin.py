from django.contrib import admin
from .models import HeaderInfo,AboutMe,WhatToDo,Comments
# Register your models here.
admin.site.register(HeaderInfo)
admin.site.register(AboutMe)
admin.site.register(WhatToDo)
admin.site.register(Comments)