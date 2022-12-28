import threading
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from rest_framework.views import APIView
from rest_framework.response import Response
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
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
        message = request.data['message']
        subject = request.data['name']
        print(message)
        # configuration = sib_api_v3_sdk.Configuration()
        # configuration.api_key['api-key'] = str(os.getenv("SENDINBLUE_API_KEY"))
        # api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(configuration))
        # api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        # sender = {"name": "sender", "email": email}
        # to = [{"email": settings.EMAIL_HOST_USER, "name": "Abdul"}]
        # headers = {"Some-Custom-Name": "unique-id-1234"}
        # send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers,html_content=message, sender=sender, subject=subject)
        # try:
            # api_response = api_instance.send_transac_email(send_smtp_email)
            # api_response = api_instance.get_account()
            # pprint(api_response)
            # return Response(True)
        # except ApiException as e:
            # print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
            # return Response(False)
        
        msg = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, ['a1daromosu@gmail.com', ])
        msg.send()
        EmailThread(msg).start()
        return Response(True)
