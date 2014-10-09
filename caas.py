from cowpy import cow
from flask import Flask, request, abort, make_response, Response


app = Flask(__name__)


@app.route('/cowsay/')
def cowsay():
    helpmsg = '''

        Welcom to cow-as-as-service. We support following commands:

            help
                display help info

            say TEXT
                draw a cow saying TEXT

    '''
    if not 'command' in request.args or request.args['command'] not in ('help', 'say'):
        abort(make_response("Command missing or invalid. Cow-as-a-service supportos only following commands: help, say", 422))
    command = request.args['command']
    arguments = request.args.getlist('arg')
    if command == 'help':
        return Response(helpmsg, mimetype='text/plain')
    elif command == 'say':
        if not arguments or len(arguments) > 1:
            return Response(helpmsg, mimetype='text/plain')
        else:
            return  Response(cow.get_cow()().milk(msg=arguments[0]), mimetype='text/plain')


if __name__ == '__main__':
    app.run()
