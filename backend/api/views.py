from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rest_framework import generics
from django.shortcuts import render

from .models import Message, MessageSerializer, Todo, TodoSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class CSRFExemptMixin(object):
   @method_decorator(csrf_exempt)
   def dispatch(self, *args, **kwargs):
       return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ListTodo(CSRFExemptMixin, generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# @csrf_exempt
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

