from flask import Flask
from flask import Flask, jsonify
from flask import request
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


    # Definir el endpoint de GET

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos) # Convertir los datos de todos a JSON
    return json_text # Devolver los datos JSON


    # Definir el endpoint de POST

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True) # convierte el cuerpo de la solicitud en un diccionario
    todos.append(request_body) # agrega el diccionario a la lista de todos
    return jsonify(todos) # devuelve la lista actualizada de todos al front end

    # Definir el endpoint de DELETE
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]  # Eliminar la tarea de la lista de todos
    return jsonify(todos)  # Devolver la lista actualizada de todos al front end



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)


  # pipenv run python src/app.py