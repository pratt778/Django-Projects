from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "this will print hi there!"
    def handle(self,*args,**kwargs):
        print('Hi there!! how are you doing??')