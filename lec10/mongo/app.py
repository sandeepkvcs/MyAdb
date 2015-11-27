from bottle import default_app, run, route
from bottle import get, put, post, request, template
from bottle import static_file

from items import *

@get('/')
@get('/list')
@get('/list/<status:int>')
def get_list(status=-1):
    items = get_items(status)
    result = []
    for item in items:
        result.append((item['id'],item['task'],item['status']))
    return template('list_view', rows=result)

@get('/new') 
def get_new():
    return '''
        <p>Enter a new item...</p><br/>
        <form action="/new" method="post">
            To be done: <input name="task" type="text" />
            <input value="Save" type="submit" />
        </form>
    '''
    
@post('/new')
def post_new():
    task = request.forms.get('task', '').strip()
    new_item(task,1)
    return get_list()

@get('/edit/<id:int>')
def get_edit(id):
    item = get_item(id)
    return template('edit_view', id=id, task=item['task'], status=item['status'])

@post('/edit/<id:int>')
def post_edit(id):
    task = request.forms.get('task', '').strip()
    status = request.GET.get('status','').strip()
    if status == 'open':
        status = 1
    else:
        status = 0
    item = get_item(id)
    item['task'] = task
    item['status'] = status
    save_item(item)
    return get_list()
        
@get('/delete/<id:int>')
def confirm_delete_item(id):
    item = get_item(id=id)
    return template('delete_view', id=id, task=item['task'], status=item['status'])

@post('/delete/<id:int>')
def delete_item(id):
    discard_item(id)
    return get_list()
              
@get('/static/<filename>')
def server_static(filename):
    print(filename)
    return static_file(filename, root='static')

if __name__ == "__main__":
    run(reloader = True, host="0.0.0.0")
else:
    application = default_app()

