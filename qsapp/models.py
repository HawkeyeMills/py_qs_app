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
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)
    points = models.DecimalField(max_digits=4, decimal_places=2)
    possible = models.DecimalField(max_digits=4, decimal_places=2)
    grade_date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.grade

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

    def __str__(self):
        return self.gradecalc

class GradeConfig(models.Model):
    metric_config = models.ForeignKey('MetricConfig', on_delete=models.CASCADE)
    grade_calc = models.ForeignKey('GradeCalc', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=False)
    percentoftotal = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    goal = models.CharField(max_length=255)
    configtype = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
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

    def __str__(self):
        return self.gradevalue

class MetricConfig(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    metricname = models.CharField(max_length=255)
    fitbitvalue = models.CharField(max_length=255, blank=True)
    label = models.CharField(max_length = 255)
    metrictype = models.ForeignKey('MetricType', on_delete=models.CASCADE)
    orderby = models.IntegerField()
    profiledisplay = models.BooleanField()
    active = models.BooleanField(default=True)
    updateable = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.metricname

class MetricType(models.Model):
    metrictype = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.metrictype

class Metric(models.Model):
    metric_config = models.ForeignKey('MetricConfig', on_delete=models.CASCADE)
    metric_date = models.DateField(default=timezone.now)
    value = models.DecimalField(max_digits=10, decimal_places=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.metric_config.metricname

class MetricGrade(models.Model):
    metric = models.ForeignKey('Metric', on_delete=models.CASCADE)
    grade = models.ForeignKey('Grade', on_delete=models.CASCADE)
    points = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=3, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.metric

class Note(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    note = models.TextField()
    note_date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)