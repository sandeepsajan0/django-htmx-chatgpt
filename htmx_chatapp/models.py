from django.db import models

# Create your models here.


class ChatMessage(models.Model):
    question = models.CharField(max_length=1000, verbose_name="Question")
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def message(self):
        return {'question': self.question, 'answer': self.answer}