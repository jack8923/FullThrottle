from django.db import models
# Create your models here.


class Members(models.Model):
    real_name = models.CharField(
        unique=True,
        max_length=256,
        verbose_name="real_name"
    )

    tz = models.CharField(
        unique=True,
        max_length=256,
        verbose_name="tz"
    )

    def __str__(self):
        return self.real_name

    class Meta:
        db_table = "Members"
        verbose_name = "members"


class Activity_Periods(models.Model):
    member = models.ForeignKey(
        Members,
        on_delete=models.CASCADE,
        related_name="activity_periods"
    )

    start_time = models.DateTimeField(
        # auto_now=True,
        verbose_name="start_time"
    )

    end_time = models.DateTimeField(
        # auto_now=True,
        verbose_name="end_time"
    )

    # def __str__(self):
    #     return "{user}: {start_time}, {end_time}".format(
    #         member=str(self.user), attribute=str(self.start_time), value=self.end_time
    #     )

    class Meta:
        db_table = "Activity Periods"
        verbose_name = "activity_periods"
