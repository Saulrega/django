from tkinter.messagebox import QUESTION
from django.contrib import admin
from .models import Question

admin.site.register(Question)
