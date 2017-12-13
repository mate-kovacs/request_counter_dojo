from flask import Flask, redirect, request, render_template
import data_manager

app = Flask(__name__)


@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def request_counter():
    count = data_manager.read_file()
    if request.method == 'GET':
        count['GET'] += 1
    elif request.method == 'POST':
        count['POST'] += 1
    elif request.method == 'PUT':
        count['PUT'] += 1
    else:
        count['DELETE'] += 1
    data_manager.write_file(count)
    return redirect('/')


@app.route('/statistics')
def present_statistics():
    count = data_manager.read_file()
    return render_template('statistics.html', count=count)


@app.route('/')
def frontend():
    return render_template('mainform.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=5200,
            debug=True)
