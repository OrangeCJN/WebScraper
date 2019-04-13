
from flask import Flask, jsonify, request, abort

from load_graph import load_graph

from  part1 import filter_pred

from flask import make_response

graph = load_graph("data.json")

app = Flask(__name__)

def check_name_match(q, name):

    return  q.lower() in name.lower()


# reference: this function from tutorial
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


def get_actors_or_movies(isMovie):

    res = {}

    isOrOp = False

    for k in request.args:

        v = request.args[k]

        v = v.replace("_", " ")

        v = v.replace('"', "")

        v = v.strip()

        if '|' in v:
            arr = v.split('|')

            res[k] = arr[0].strip()

            for m in arr[1:]:
                spl = m.split('=')

                res[spl[0].strip()] = spl[1].strip()

            isOrOp = True

            break

        res[k] = v

    if "total gross" in res:
        res['total_gross'] = res["total gross"]

        del res["total gross"]

    if "box office" in res:
        res['box_office'] = res["box office"]

        del res["box office"]

    if isMovie:
        attrs = ['name', 'box_office', 'year']

    else:
        attrs = ['name', 'age', 'total_gross']


    for k in res:
        # if k == "total gross":
        #     k = "total_gross"

        if k not in attrs:

            return jsonify({'error': 'invalid attribute ' + k}), 400

        if k != 'name':
            try:
                res[k] = int(res[k])

            except Exception:
                return jsonify({'error': 'invalid ' + k}), 400

    def pred(data):

        if isMovie:
            if data['json_class'] != "Movie":

                return False

        else:

            if data['json_class'] != "Actor":

                return False

        for k in res:

            if k == 'name':

                matched = check_name_match(res[k], data['name'])

            else:

                matched = (res[k] == data[k])

            if isOrOp and matched:

                return True

            elif not isOrOp and not matched:
                return False

        if isOrOp:
            return False

        else:
            return True


    print("result")

    result = filter_pred(graph, pred)

    if isMovie:
        name = "movies"

    else:
        name = "actors"


    # return jsonify(result), 200

    return jsonify({name: result}), 200




@app.route('/actors', methods=['GET'])
def get_actors():

    return get_actors_or_movies(False)


@app.route('/movies', methods=['GET'])
def get_movies():
    return get_actors_or_movies(True)


def find_data(isMovie, name):

    name = name.replace("_", " ")

    def pred(data):

        if isMovie:
            if data['json_class'] != "Movie":

                return False

        else:

            if data['json_class'] != "Actor":

                return False

        return check_name_match(name, data['name'])

    arr = filter_pred(graph, pred)

    return arr

def get_movie_or_actor(isMovie, name):

    # name = name.replace("_", " ")
    #
    # def pred(data):
    #
    #     if isMovie:
    #         if data['json_class'] != "Movie":
    #
    #             return False
    #
    #     else:
    #
    #         if data['json_class'] != "Actor":
    #
    #             return False
    #
    #     return check_name_match(name, data['name'])

    arr = find_data(isMovie, name)

    if len(arr) == 0:

        return jsonify({'error': 'Not found'}), 404

    else:
        # if isMovie:
        #     name = "movie"
        #
        # else:
        #     name = "actor"

        return jsonify(arr[0])


def put_movie_or_actor(isMovie, name, data):


    if not data:

        abort(400)

    for k in data:
        if k in ['age', 'total_gross', 'box_office']:
            try:
                data[k] = int(data[k])
            except Exception:
                abort(400)

    arr = find_data(isMovie, name)

    if len(arr) == 0:

        return jsonify({'error': 'Not found'}), 404

    else:

        target = arr[0]
        for k in data:


            target[k] = data[k]

        return jsonify(target), 404




@app.route('/actors/<name>', methods=['GET'])
def get_actor(name):
    return get_movie_or_actor(False, name)

@app.route('/movies/<name>', methods=['GET'])
def get_movie(name):
    return get_movie_or_actor(True, name)


@app.route('/actors/<name>', methods=['PUT'])
def put_actor(name):

    return put_movie_or_actor(False, name, request.json)

@app.route('/movies/<name>', methods=['PUT'])
def put_movie(name):

    return put_movie_or_actor(True, name, request.json)

def post_actor_or_movie(isMovie, data):

    if not data:
        abort(400)

    if 'name' not in data:
        return jsonify({'error': 'must have name attribute'}), 400


    if isMovie:
        data['json_class'] = 'Movie'

    else:
        data['json_class'] = 'Actor'

    if data['name'] in graph.get_nodes():

        return jsonify({'error': 'already have ' + data['name']}), 400

    else:

        graph.add_node(data['name'], data)

        return jsonify(data), 201


@app.route('/actors', methods=['POST'])
def post_actor():

    return  post_actor_or_movie(False, request.json)

@app.route('/movies', methods=['POST'])
def post_movie():

    return  post_actor_or_movie(True, request.json)


def delete_movie_or_actor(isMovie, name):

    # if name not in graph.get_nodes():
    #     abort(404)
    #
    # if graph['json_class'] != ('Movie' if isMovie else "Actor"):
    #     abort(404)

    arr = find_data(isMovie, name)

    if len(arr) == 0:

        return jsonify({'error': 'Not found'}), 404


    print(graph.get_nodes()[arr[0]['name']])

    del graph.get_nodes()[arr[0]['name']]

    return jsonify(arr[0])

@app.route('/actors/<name>', methods=['DELETE'])
def delete_actor(name):

    return delete_movie_or_actor(False, name)

@app.route('/movies/<name>', methods=['DELETE'])
def delete_movie(name):

    return delete_movie_or_actor(True, name)

if __name__ == '__main__':

    app.run(debug=True)


