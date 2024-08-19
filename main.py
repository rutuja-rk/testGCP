import functions_framework

@functions_framework.http
def hello_http(request):

    request_json = request.get_json(silent=True)
    request_args = request.args
    print("test here")

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(name)
