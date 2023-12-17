from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    """
    Model representing a question.

    Attributes:
        question_text (CharField): The text of the question (maximum length: 200 characters).
        pub_date (DateTimeField): The date and time the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def __str__(self):
        """
        Returns a string representation of the Question object.

        Returns:
            str: The text of the question.
        """
        return self.question_text
    
    def was_published_recently(self):
        """
        Checks if the question was published recently.

        Returns:
            bool: True if the question was published within the last day, False otherwise.
            """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    """
    Model representing a choice for a question.

    Attributes:
        question (ForeignKey): The associated question for the choice.
        choice_text (CharField): The text of the choice (maximum length: 200 characters).
        votes (IntegerField): The number of votes for the choice (default: 0).
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of the Choice object.

        Returns:
            str: The text of the choice.
        """
        return self.choice_text