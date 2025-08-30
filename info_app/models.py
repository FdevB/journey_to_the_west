from django.db import models

# Create your models here.
class MessageModel(models.Model):
    """
    Model definition for MessageModel.

    This class defines the MessageModel database schema and its related behaviors.

    Attributes:
        name (CharField): The name of the message sender.
        email (EmailField): The email address of the sender.
        subject (CharField): The subject ot title of the message.
        message (TextField): The message.
        sent_at (DateTimeField): Timestamp of when the message was sent.
        is_read (BooleanField): Indicates whether the message has been read.
    """
    name = models.CharField(max_length=20)
    email = models.EmailField()
    
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    is_read = models.BooleanField(default=False)

    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message'

    def __str__(self):
        return self.subject
