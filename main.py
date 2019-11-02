from flask import flash, render_template, request, redirect
from flask import Flask
from data.taskDataService import TaskDataService
from uuid import uuid4

app = Flask(__name__)
app.secret_key = str(uuid4())


@app.route('/new_task')
def add_task_view():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_task():
    _name = request.form['inputName']
    _id = str(uuid4())
    if _name and request.method == 'POST':
        task_data = TaskDataService
        task_data.create(_id, _name)
        flash('Task added successfully!')
        return redirect('/')
    else:
        return 'Error while adding task'


@app.route('/')
def tasks():
    task_data = TaskDataService
    tasks = task_data.list()
    return render_template('tasks.html', tasks)


@app.route('/delete/<string:id>')
def delete_task(id):
    task_data = TaskDataService
    task_data.delete(id)
    flash('Task deleted successfully!')
    return redirect('/')


if __name__ == "__main__":
    app.run()
