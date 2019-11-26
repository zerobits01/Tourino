from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.dispatch import receiver, Signal
from django.core.signals import request_finished
from rimaleusers.models import RimaleUser
mail_post = Signal(providing_args=["post"])

# TODO : Emailing with asyncio or adding this to signals and using it
#       in overloaded saved method of post model 

@receiver(mail_post)
def my_callback(sender, **kwargs):
    post = kwargs['post']

    basepath = 'localhost/blog'
    link = basepath + '/' + post.id

    subject, from_email = post.name, 'from@example.com'

    to = RimaleUser.objects.filter(news__exact=True).values('email')

    text_content = post.text
    html_content = '<a>%s</a>' % (link)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


signer = Signer()
# Create your models here.
# checking everything in here with try catch and if statements
# i know that i can use init i wanna use static method
