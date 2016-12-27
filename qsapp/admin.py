from django.contrib import admin

from .models import DailyGrade
admin.site.register(DailyGrade)

from .models import GradeCalc
admin.site.register(GradeCalc)

from .models import GradeConfig
admin.site.register(GradeConfig)

from .models import Grade
admin.site.register(Grade)

from .models import MetricConfig
admin.site.register(MetricConfig)

from .models import MetricGrade
admin.site.register(MetricGrade)

from .models import Metric
admin.site.register(Metric)

from .models import Note
admin.site.register(Note)

from .models import MetricType
admin.site.register(MetricType)