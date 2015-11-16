from django.contrib.auth.models import User
from socialgraph.models import UserLink


def get_people_user_follows(user):
    ulink = UserLink.objects.filter(from_user=user).values('to_user')
    return User.objects.filter(id__in=[i['to_user'] for i in ulink])


def get_people_following_user(user):
    ulink = UserLink.objects.filter(to_user=user).values('from_user')
    return User.objects.filter(id__in=[i['from_user'] for i in ulink])


def get_mutual_followers(user):
    follower = UserLink.objects.filter(from_user=user).values('to_user')
    following = UserLink.objects.filter(to_user=user).values('from_user')
    follows_set = set([i['to_user'] for i in follower])
    following_set = set([i['from_user'] for i in following])
    return User.objects.filter(id__in=follows_set.intersection(following_set))
