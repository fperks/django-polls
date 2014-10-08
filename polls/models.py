import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    """
        Model representation of a question, has a 1 to many relationship with Choice
    """
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(verbose_name='date published')

    def was_published_recently(self):
        """
        Determines if the question was published in the last day

        :returns: bool value indicating if it was published in the last day
        :rtype: bool
        """
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    """
        Model representation of a choice for a question
    """
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

