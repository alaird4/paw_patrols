from django.db import models

# Create your models here.

class Post(models.Model):
# Default behaviour - Django creates primary keys for you
    """
    Model representing a blog post.

    Attributes:
        id (AutoField): The primary key for the post.
        title (CharField): The title of the post (maximum length: 140 characters).
        body (TextField): The body/content of the post.
        date (DateTimeField): The date and time of the post.
    """


    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
def __str__(self):
    

    """
        Returns a string representation of the Post object.

        Returns:
            str: The title of the post.
        """

    return self.title