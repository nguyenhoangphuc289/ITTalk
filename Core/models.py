# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class AdminAccount(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    role_id = models.IntegerField(blank=True, null=True)
    username = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    password = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_date = models.DateTimeField(blank=True, null=True)
    is_active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ittalk_admin_account'


class Article(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    article_name = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    article_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_article'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    post_id = models.IntegerField(blank=True, null=True)
    parent_comment_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    up_votes = models.IntegerField(blank=True, null=True)
    down_votes = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    public_date = models.DateTimeField(blank=True, null=True)
    status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ittalk_comment'


class Event(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    event_detail = models.TextField(blank=True, null=True)
    event_name = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ittalk_event'


class Image(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    image_name = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    image_size = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ittalk_image'


class Notification(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    notification_type_id = models.IntegerField(blank=True, null=True)
    send_user_id = models.IntegerField(blank=True, null=True)
    post_id = models.IntegerField(blank=True, null=True)
    recieve_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_notification'


class NotificationType(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    notification_type_name = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_notification_type'


class Post(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    type_id = models.IntegerField(blank=True, null=True)
    topics = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    up_votes = models.TextField(blank=True, null=True)
    down_votes = models.TextField(blank=True, null=True)
    subcribers = models.TextField(blank=True, null=True)
    is_anonymous = models.BooleanField()

    def get_subscribers(self):
        users = User.objects.all()
        users = users.exclude(pk=self.user_id)
        return users

    class Meta:
        managed = False
        db_table = 'ittalk_post'


class PostType(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    post_type_name = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_post_type'


class Report(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    report_type_id = models.IntegerField(blank=True, null=True)
    object_reported_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_report'


class ReportType(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    report_type_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_report_type'


class Role(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    role_name = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_role'


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    time_line_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_schedule'


class TimeLine(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    week_id = models.IntegerField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ittalk_time_line'


class Topic(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    topic_name = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_topic'


class TopicFollower(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    user_id = models.IntegerField(blank=True, null=True)
    post_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_topic_follower'


class UserFollower(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    followed_user_id = models.IntegerField(blank=True, null=True)
    follow_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ittalk_user_follower'


class Week(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    week_name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ittalk_week'


class SocialAuthAssociation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthUsersocialauth(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)
