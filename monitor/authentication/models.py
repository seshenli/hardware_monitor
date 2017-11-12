from django.db import models


# Create your models here.
class WebUser(models.Model):
    username = models.CharField(max_length=40, db_column='user_name')
    password = models.CharField(max_length=1024, db_column='passwd')
    email = models.CharField(max_length=200, db_column='email')
    nickname = models.CharField(max_length=100, db_column='nick_name')

    class Meta:
        db_table = 'web_user'
        # verbose_name = u'网站用户'
        # verbose_name_plural = u'网站用户'
