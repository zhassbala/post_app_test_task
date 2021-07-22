from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    TODO implement login function
    Takes username and password as
    parameters, logs in the user and
    returns an authorization token.
    If the user is not registered,
    returns 404 response and shows an appropriate message

    :param request:
    :return:
    """
    return Response('this is a login endpoint')


@api_view(['POST'])
def register(request):
    """
    TODO implement register function
    Takes username, email and password as parameters,
    and registers the user after validation.
    In case of failed validation (username already in use, etc.)
    responds with an appropriate message.

    :param request:
    :return:
    """
    return Response('this is a register endpoint')


@api_view(['POST'])
def post_create(request):
    # TODO implement post_create function
    return Response('this is a post_create endpoint')


@api_view(['POST'])
def post_update(request):
    # TODO implement post_update function
    return Response('this is a post_update endpoint')


@api_view(['POST'])
def post_delete(request):
    # TODO implement post_delete function
    return Response('this is a post_delete endpoint')
