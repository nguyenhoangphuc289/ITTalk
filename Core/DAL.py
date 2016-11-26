from Core.models import *
from django.db.models import *
from django.db.models.functions import *
from django.db.models.query import *
from datetime import datetime
from firebase import firebase
from django.conf import settings


# FIREBASE_URL = settings.FIREBASE_URL


class PostDAL(object):
    @staticmethod
    def SelectAll():
        return Post.objects.all()

    @staticmethod
    def SelectByPostId(postId):
        return Post.objects.get(pk=postId)

    @staticmethod
    def SelectByTypeId(typeId):
        return Post.objects.filter(type_id=typeId)

    @staticmethod
    def SelectByTopic(topicId):
        return Post.objects.filter(topics__contains=topicId)

    @staticmethod
    def SelectQuestionByUserId(userId):
        return Post.objects.filter(user_id=userId).filter(type_id=1).order_by('-id')

    @staticmethod
    def SelectPostByUserId(userId):
        return Post.objects.filter(user_id=userId).filter(type_id=2).order_by('-id')

    @staticmethod
    def IncreaseUpvote(postId, userId):
        p = Post.objects.get(pk=postId)
        p.up_votes += userId + ","
        p.up_votes = p.up_votes[:-1]
        p.save()

    @staticmethod
    def DecreaseUpvote(postId, userId):
        p = Post.objects.get(pk=postId)
        arr = p.up_votes.split(',')
        p.up_votes = ""
        arr.remove(userId)
        for str in arr:
            p.up_votes += str + ','
        p.up_votes = p.up_votes[:-1]
        p.save()

    @staticmethod
    def IncreaseDownVote(postId, userId):
        p = Post.objects.get(pk=postId)
        p.down_votes += str(userId) + ","
        p.down_votes = p.down_votes[:-1]
        p.save()

    @staticmethod
    def DecreaseDownvote(postId, userId):
        p = Post.objects.get(pk=postId)
        if ("," not in p.down_votes and p.down_votes != ""):
            p.down_votes = ""
        else:
            arr = p.down_votes.split(',')
            p.down_votes = ""
            arr.remove(userId)
            for str in arr:
                p.down_votes += str
            p.down_votes = p.down_votes[:-1]
        p.save()

    @staticmethod
    def IncreaseView(postId):
        p = Post.objects.get(pk=postId)
        p.view_count += 1
        p.save()

    @staticmethod
    def Insert(typeId, topics, title, content, userId, isAnonymous):
        p = Post(type_id=typeId, topics=topics, title=title, content=content, user_id=userId, view_count=0, up_votes=0,
                 down_votes=0, date_created=datetime.now(), is_anonymous=isAnonymous)
        p.save()

    @staticmethod
    def Update(postId, content):
        p = Post.objects.get(pk=postId)
        p.content = content
        p.save()

    @staticmethod
    def Delete(postId):
        p = Post.objects.get(pk=postId)
        p.delete()


class PostTypeDAL(object):
    @staticmethod
    def SelectAll():
        return PostType.objects.all()

    @staticmethod
    def SelectById(typeId):
        return PostType.objects.get(pk=typeId)


class SocialAuthUsersocialAuthDAL(object):
    @staticmethod
    def SelectByUserId(userId):
        return SocialAuthUsersocialauth.objects.get(user_id=userId)


class AuthUserDAL(object):
    @staticmethod
    def GetUser(userId):
        return AuthUser.objects.get(id=userId)

    @staticmethod
    def GetSubcribers(userId):
        return UserFollower.objects.all().exclude(followed_user_id=userId)


class NotificationDAL(object):
    @staticmethod
    def send_notifications(subscribers, notification_markup):
        context = {'markup': notification_markup}
        fb = firebase.FirebaseApplication(FIREBASE_URL, None)

        for user in subscribers:
            url = '/' + user.id + '/'

            try:
                fb.post(url, context)

            except Exception as e:
                print e
                print 'Firebase Notification not sent'
