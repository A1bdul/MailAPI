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
    
    def __init__(self, subject, msg, email):
        self.subject = subject
        self.msg = msg
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        print("sent!!")
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = str(os.getenv('SENDINBLUE_API_KEY'))
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        # Define the campaign settings\
        email_campaigns = sib_api_v3_sdk.SendSmtpEmail(
        subject= self.subject,
        sender= { "name": "Israel", "email": self.email},
        to = [{'email': DEFAULT_TO_EMAIL, "name":"Abdul"}],
        # Content that will be sent\
        html_content= self.msg,
        )
        # Make the call to the client\
        try:
            api_response = api_instance.send_transac_email(email_campaigns)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)# ------------------
        # Include the Sendinblue library\



class MailAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        message = request.data['message']
        subject = request.data['name']
        print(message+ 'from\n' +email)
        EmailThread(subject, message, email).start()
        return Response(True)
