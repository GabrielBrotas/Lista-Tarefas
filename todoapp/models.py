from django.db import models


class ToDo(models.Model):
    # data_adicionada = models.DateTimeField()
    text = models.TextField(max_length=200)
