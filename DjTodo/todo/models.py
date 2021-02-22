from django.db import models

class Todo(models.Model):
    name = models.CharField('name', max_length=10, blank=True)
    todo = models.CharField('todo', max_length=50)

    def __str__(self):
        return self.todo
