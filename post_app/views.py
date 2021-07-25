from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from .serializers import UserSerializer, PostSerializer, TagSerializer

from .models import User, Post, Tag

import jwt, datetime


@api_view(['GET', 'POST'])
def index(request):
    response = {
        '/api/': 'this page.',
        '/api/login/': 'Takes username and password as '
                       'parameters, logs in the user and '
                       'returns an authorization token. '
                       'If the user is not registered, '
                       'returns 404 response and shows an appropriate message',
        '/api/register/': 'Takes username, email and password as parameters, '
                          'and registers the user after validation. '
                          'In case of failed validation (username already in use, etc.),'
                          'responds with an appropriate message.',
        '/api/post_create': '',
        '/api/post_update': '',
        '/api/post_delete': '',
    }
    return Response(response)


@api_view(['POST'])
def login(request):
    """
    Takes username and password as
    parameters, logs in the user and
    returns an authorization token.
    If the user is not registered,
    returns 404 response and shows an appropriate message

    :param request:
    :return:
    """
    email = request.data['email']
    password = request.data['password']
    user = User.objects.get(email=email)

    if not user.check_password(password):
        raise AuthenticationFailed('Password is incorrect!')

    token = jwt.encode(
        {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=3),
            'iat': datetime.datetime.utcnow()
        },
        'secret',
        algorithm='HS256'
    )
    response = Response({'jwt': token})
    response.set_cookie(key='jwt', value=token, httponly=True)

    return response


@api_view(['POST'])
def register(request):
    """
    Takes username, email and password as parameters,
    and registers the user after validation.
    In case of failed validation (username already in use, etc.)
    responds with an appropriate message.

    :param request:
    :return:
    """
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def logout(request):
    """
    Logs out the user
    :param request:
    :return:
    """
    response = Response({'message': 'success'})
    response.delete_cookie('jwt')

    return response


@api_view(['GET'])
def get_user(request):
    """
    Returns the basic info about the logged user
    :param request:
    :return:
    """
    user = check_auth(request)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def get_posts(request):
    """
    Returns an array of the post created by the logged user (Posts which editor is the logged user)
    :param request:
    :return:
    """
    user = check_auth(request)

    posts = user.posts
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


def check_auth(request):
    """
    checks whether the is authorized or not and
    in case of a successful validation returns
    the user object of the current session
    ! IS NOT AN API VIEW
    :param request:
    :return: User object
    """
    token = request.COOKIES.get('jwt')  # get the jwt token from the request cookies

    if not token:
        raise NotAuthenticated('Unauthorized!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])     # get decode the token to get the user id
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token Expired!')

    user = User.objects.get(id=payload['id'])   # fetch the user object from id

    return user


@api_view(['POST'])
def post_create(request):
    """
    Creates a post with given parameters. The editor by default is the logged user.
    :param request: must contain a title, content of the post and an array of tags
    :return: Response object with created post
    """
    # TODO implement post_create function

    user = check_auth(request)

    title = request.data['title']
    content = request.data['content']
    tags = request.data['tags']

    post = Post(title=title, content=content, editor=user)

    post.save()

    for tag in tags:
        tag_object = Tag.objects.filter(title=tag).first()
        if not tag_object:
            tag_object = Tag(title=tag)
            tag_object.save()

        post.tags.add(tag_object)

    post.save()

    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])
def post_update(request):
    """
    checks if the user can edit the post and updates it.
    can take any of the following parameters:
        title: str
        content: str
        tags: array
    and has one required parameter:
        id: int -> id of the requested post
    :param request:
    :return:
    """
    user = check_auth(request)
    post = Post.objects.get(id=request.data['id'])

    if user.id != post.editor_id:
        raise AuthenticationFailed('Cannot access the requested post.')

    if request.data['title']:
        post.title = request.data['title']
    if request.data['content']:
        post.content = request.data['content']
    if request.data['tags']:
        # post.tags.remove(post.tags.all())
        for tag in post.tags.all():
            post.tags.remove(tag)

        tags = request.data['tags']

        for tag in tags:
            tag_object = Tag.objects.filter(title=tag).first()
            if not tag_object:
                tag_object = Tag(title=tag)
                tag_object.save()

            post.tags.add(tag_object)

    post.save()

    return Response(PostSerializer(post).data)


@api_view(['POST', 'DELETE'])
def post_delete(request):
    # TODO implement post_delete function

    user = check_auth(request)
    post = Post.objects.get(id=request.data['id'])

    if user.id != post.editor_id:
        raise AuthenticationFailed('Cannot access the requested post.')

    serializer = PostSerializer(post)
    response = Response({f"Post with id {post.id} successfully deleted": serializer.data})

    post.delete()
    return response

