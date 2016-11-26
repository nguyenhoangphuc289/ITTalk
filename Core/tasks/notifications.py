from django.conf import settings
from firebase import firebase

from django.template.loader import render_to_string

FIREBASE_URL = settings.FIREBASE_URL


def send_notifications(subscribers, notification_markup):
    context = {'markup': notification_markup}
    fb = firebase.FirebaseApplication(FIREBASE_URL, None)

    for user in subscribers:
        url = '/users/%s/notification' % user.pk

        try:
            result = fb.post(url, context)

        except Exception as e:
            print e
            print 'Firebase Notification not sent'


def create_notification(sender, created, **kwargs):
    if created:
        model = kwargs['instance']
        subscribers = model.get_subscribers()
        context = {
            'model': model,
            'frontend_uri': '/app/#/posts',
            'SITE_URL': settings.SITE_URL
        }
        notification_markup = render_to_string('home/notifications/post_notification.html', context)

        send_notifications(subscribers, notification_markup)
