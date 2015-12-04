from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError

from .models import DBSession, User, Post, Counter


@view_config(route_name='home', renderer='json')
def home(request):
    result = []
    try:
        for post, user, views in DBSession.query(
                Post, User.name, Counter.views).join(User).outerjoin(Counter).all():
            result.append([post.text, user])
            if views is None:
                DBSession.add(Counter(post_id=post.id, views=1))
            else:
                DBSession.query(Counter).filter_by(post_id=post.id).update({'views': views + 1})
    except DBAPIError:
        return Response('Database Error', content_type='text/plain', status_int=500)
    return result
