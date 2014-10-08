from cowpy import cow
from flask import Flask, request, abort, make_response, Response


app = Flask(__name__)


@app.route('/cowsay/')
def cowsay():
    if not 't' in request.args and not 'text' in request.args:
        abort(make_response("Pass text with -t, otherwise I don't know what to say", 422))
    text = request.args.get('t', request.args.get('text'))
    return  Response(cow.get_cow()().milk(msg=text), mimetype='text/plain')


if __name__ == '__main__':
    app.run()

