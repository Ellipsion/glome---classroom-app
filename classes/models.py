import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Classes(models.Model):
    user = models.ForeignKey(User, related_name='classes',
                             on_delete=CASCADE, null=True,)  # editable=False)
    class_name = models.CharField(max_length=200)
    class_faculty = models.CharField(max_length=200, null=True, blank=True)
    class_url = models.URLField(blank=True, null=True)
    class_time = models.TimeField(blank=True, null=True)
    class_pub_date = models.DateField(
        'Date published', auto_now_add=True, editable=False)
    class_pub_datetime = models.DateTimeField('Date published',
                                              auto_now_add=True, editable=False,)

    Monday = models.BooleanField(blank=True, default=False)
    Tuesday = models.BooleanField(blank=True, default=False)
    Wednesday = models.BooleanField(blank=True, default=False)
    Thursday = models.BooleanField(blank=True, default=False)
    Friday = models.BooleanField(blank=True, default=False)
    Saturday = models.BooleanField(blank=True, default=False)
    Sunday = models.BooleanField(blank=True, default=False)
    Alldays = models.BooleanField(blank=True, default=False)

    def id(self):
        return self.id

    def create_time(self, hours, minutes):
        return timezone.now().replace(hour=0, minute=0, second=0) + \
            datetime.timedelta(hours=hours, minutes=minutes)

    def is_active(self):
        if self.class_time is not None:
            hours = self.class_time.hour
            minutes = self.class_time.minute
            fifty_minutes = minutes+50
            time = self.create_time(hours=hours, minutes=minutes)
            duration = self.create_time(hours=hours, minutes=fifty_minutes)
            # return time, duration
            return duration >= timezone.now() and timezone.now() >= time
        else:
            return None

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.class_name
