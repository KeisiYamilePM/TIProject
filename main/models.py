from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    TODO = '1'
    DOING = '2'
    DONE = '3'

    STATUS_CHOICES = (
        (TODO, 'To do'),
        (DOING, 'Doing'),
        (DONE, 'Done')
    )

    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=TODO,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_tags_display(self):
        tags = ['#{}'.format(tag.name) for tag in self.tags.all()]

        return ', '.join(tags)



from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=ToDo)
def my_todo_signal(sender, **kwargs):
    print('una nueva tarea ha sido creada')
