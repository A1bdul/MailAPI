import threading
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class EmailThread(threading.Thread):

    def __init__(self, msg):
        self.email_message = msg
        threading.Thread.__init__(self)

    def run(self):
        print("sent!!")
        self.email_message.send()


class MailAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        message = request.data['message'] + '\nfrom ' + email
        subject = request.data['name']
        msg = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, ['a1daromosu@gmail.com', ])
        # msg.send()
        print(message, settings.EMAIL_HOST_USER)
        EmailThread(msg).start()
        return Response(True)
