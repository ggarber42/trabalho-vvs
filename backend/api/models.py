from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class Todo(models.Model):
    name = models.CharField(max_length=200)
    completed =  models.BooleanField(default=False)

    def __str__(self):
        return self.name

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id','name','completed')