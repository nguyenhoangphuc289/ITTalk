from Core.DAL import *
from django.template.loader import render_to_string


class PostBLL(object):
    @staticmethod
    def Insert(typeId, arrTopics, title, content, userId, isAnonymous):
        topics = ""
        for topic in arrTopics:
            topics = topics + topic + ","
        topics = topics[:len(topics) - 1]
        PostDAL.Insert(typeId, topics, title, content, userId, isAnonymous)

    @staticmethod
    def SelectLastQuestion(userId):
        return PostDAL.SelectQuestionByUserId(userId)[0]

    @staticmethod
    def SelectLastPost(userId):
        return PostDAL.SelectPostByUserId(userId)[0]

    @staticmethod
    def SelectAll():
        return PostDAL.SelectAll().order_by('-id', '-date_created')

    @staticmethod
    def SelectWithoutDownvotePost(userId):
        result = []
        for post in PostDAL.SelectAll():
            if (str(userId) not in post.down_votes):
                result.append(post)
        return result

    @staticmethod
    def GetAvatar(userId):
        return "http://graph.facebook.com/%s/picture?type=large" % SocialAuthUsersocialAuthDAL.SelectByUserId(
            userId).uid

    @staticmethod
    def GetFullName(userId):
        user = AuthUserDAL.GetUser(userId)
        return user.first_name + " " + user.last_name

    @staticmethod
    def SelectById(postId):
        return PostDAL.SelectByPostId(postId)

    @staticmethod
    def Delete(postId):
        PostDAL.Delete(postId)

    @staticmethod
    def IncreaseUpvote(postId, userId):
        PostDAL.IncreaseUpvote(postId, userId)

    @staticmethod
    def DecreaseUpvote(postId, userId):
        PostDAL.DecreaseUpvote(postId, userId)

    @staticmethod
    def IncreaseDownVote(postId, userId):
        PostDAL.IncreaseDownVote(postId, userId)

    @staticmethod
    def DecreaseDownvote(postId, userId):
        PostDAL.DecreaseDownvote(postId, userId)


class AuthUserBLL(object):
    @staticmethod
    def GetSubcribers(userId):
        return


class NotificationBLL(object):
    @staticmethod
    def create_notification(userId):
        subscribers = AuthUserDAL.GetSubcribers(userId)
        context = {
            'model': AuthUserDAL.GetUser(userId),
            'frontend_uri': '/app/#/posts'
        }
        notification_markup = render_to_string('home/notifications/post_notification.html', context)

        NotificationDAL.send_notifications(subscribers, notification_markup)
