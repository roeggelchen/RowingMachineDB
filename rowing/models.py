from django.db import models
from django.urls import reverse
from django.contrib import admin

# Create your models here.
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published', auto_now_add=True)


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)



class RowingSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    com_port = models.CharField(max_length=50)
    c = models.CharField(max_length=5)
    t = models.CharField(max_length=5)
    version = models.CharField(max_length=50)
    max_level = models.IntegerField(default=0)
    h = models.CharField(max_length=5)
    start_time = models.DateTimeField('start_time')#, auto_now_add=True)
    end_time = models.DateTimeField('end_time')#, auto_now_add=True)
    
    def __str__(self):
        return self.start_time

    class Meta:
        pass

    def __str__(self):
        return str(self.start_time)

    def get_absolute_url(self):
        return reverse("rowing_session_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("rowing_session_update", args=(self.pk,))

    @admin.display(description='Stroke at Distance')
    def score(self):
        return (str(self.start_time))

class RowingStroke(models.Model):
    id = models.BigAutoField(primary_key=True)
    rowing_session = models.ForeignKey(RowingSession, on_delete=models.CASCADE)
    t = models.CharField(max_length=5)
    distance = models.FloatField(default=0)
    one = models.IntegerField(default=1)
    speed = models.TimeField()
    strokes_per_minute = models.IntegerField(default=0)
    watts = models.IntegerField(default=0)
    colories_per_hour = models.IntegerField(default=0)
    zero = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    message = models.CharField(max_length=200)
    time_stamp = models.DateTimeField('time_stamp')#, auto_now_add=True)
    
    # def __str__(self):
    #     return self.time_stamp
    
    class Meta:
        pass

    def __str__(self):
        return str(self.start_time)

    def get_absolute_url(self):
        return reverse("rowing_stroke_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("rowing_stroke_update", args=(self.pk,))

    @admin.display(description='Stroke at Distance')
    def score(self):
        return ("%d m (%d Watt)" % (self.distance, self.watts))
