from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.dispatch import receiver, Signal
from django.core.signals import request_finished
from TourinoUser.model import TourinoUser 
mail_post = Signal(providing_args=["post"])
# import smtplib
# from email.message import EmailMessage
        

@receiver(mail_post)
def my_callback(sender, **kwargs):
    try :

        post = kwargs['post']

        basepath = 'localhost/blog'
        link = basepath + '/' + str(post.id)
        subject, from_email = post.title, 'from@example.com'

        to = TourinoUser.objects.filter(news__exact=True).values('email')
        text_content = post.text
        html_content = '<a>%s</a>' % (link)
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        print(to)
        print("trying to send")
        msg.send()
        print("sent!!!")

    
    except Exception as e :
        print(e)



'''
        post = kwargs['post']
        basepath = 'localhost/blog'
        link = basepath + '/' + str(post.id)

        subject, from_email = post.title, 'from@example.com'

        to = ['zerobits01@yahoo.com']# TourinoUser.objects.filter(news__exact=True).values('email')

        text_content = post.text
        html_content = '<a>%s</a>' % (link)
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        print("** \t trying to sent")
        msg.send()
        print("** \t sent")
        post = kwargs['post']
        basepath = 'localhost/blog'
        link = basepath + '/' + str(post.id)

        subject, from_email = post.title, 'from@example.com'
        to = TourinoUser.objects.filter(news__exact=True).values('email')
        text_content = post.text
        
        gmail_user = 'pgr0101mm@gmail.com'
        gmail_password = 'yimuwczssawcqrmm'

        body = 'Hey, whats up?\n\n- You'

        email_text = '<a>%s</a>' % (link)
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        print("[+] try to sent")
        server.sendmail(gmail_user, to, email_text)
        server.close()

        print('Email sent!')
'''
