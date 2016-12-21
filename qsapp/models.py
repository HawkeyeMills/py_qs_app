from django.db import models
from django.utils import timezone

#From DjangoGirls
#class Post(models.Model):
#    author = models.ForeignKey('auth.User')
#    title = models.CharField(max_length=200)
#    text = models.TextField()
#    created_date = models.DateTimeField(
#            default=timezone.now)
#    published_date = models.DateTimeField(
#            blank=True, null=True)

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.title

class DailyGrade(models.Model):
    grade_id = models.ForeignKey('Grade', on_delete=models.CASCADE)
    points = models.DecimalField(max_digits=4, decimal_places=2)
    possible = models.DecimalField(max_digits=4, decimal_places=2)
    grade_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

class GradeCalc(models.Model):
    GRADE_CALCS = (
            ('Standard', 'Standard'),
            ('Weight', 'Weight'),
            ('Declining', 'Declining'),
            ('DBTC', 'Don''t Break the Chain'),
            ('Time', 'Time'),
        )
    gradecalc = models.CharField(max_length=50, choices=GRADE_CALCS)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

class GradeConfig(models.Model):
    metric_config_id = models.ForeignKey('MetricConfig', on_delete=models.CASCADE)
    grade_calc_id = models.ForeignKey('GradeCalc', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=False)
    percentoftotal = models.DecimalField(max_digits=8, decimal_places=3)
    goal = models.CharField(max_length=255)
    configtype = models.CharField(max_length=255)
    note = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

class Grade(models.Model):
    GRADE_VALUES = (
            ('A+', 'A+'),
            ('A', 'A'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B', 'B'),
            ('B-', 'B-'),
            ('C+', 'C+'),
            ('C', 'C'),
            ('C-', 'C-'),
            ('D+', 'D+'),
            ('D', 'D'),
            ('D-', 'D-'),
            ('F', 'F'),
        )
    gradevalue = models.CharField(max_length=2, choices=GRADE_VALUES)
    minrange = models.IntegerField()
    maxrange = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

class MetricConfig(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    metricname = models.CharField(max_length=255)
    fitbitvalue = models.CharField(max_length=255)
    label = models.CharField(max_length = 255)
    metrictype = models.CharField(max_length=255)
    orderby = models.IntegerField()
    profiledisplay = models.BooleanField()
    updateable = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

class Metric(models.Model):
    metric_config_id = models.ForeignKey('MetricConfig', on_delete=models.CASCADE)
    metric_date = models.DateTimeField(default=timezone.now)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

class MetricGrade(models.Model):
    metric_id = models.ForeignKey('Metric', on_delete=models.CASCADE)
    grade_id = models.ForeignKey('Grade', on_delete=models.CASCADE)
    points = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=3, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

class Note(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    note = models.TextField()
    note_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
