from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from socialgraph.util import get_people_user_follows, get_people_following_user
from socialgraph.util import get_mutual_followers
from django.template import RequestContext

friend_function_map = {
    'followers': get_people_user_follows,
    'following': get_people_following_user,
    'mutual': get_mutual_followers,
}


def friend_list(request, list_type, username):
    user = get_object_or_404(User, username=username)
    context = {
        'list_type': list_type,
        'friends': friend_function_map[list_type](user),
    }
    return render_to_response(
        'friend_list.html',
        context,
        context_instance=RequestContext(request),
    )
