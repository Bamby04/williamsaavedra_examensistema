from flask import Flask, jsonify
import os

app = Flask(__name__)

STUDENT = os.environ.get('STUDENT_NAME', 'NombreEstudiante')
PORT = int(os.environ.get('PORT', 5000))

@app.route('/')
def index():
    return jsonify({
        'message': 'Hola desde Flask en Docker',
        'student': STUDENT
    })

@app.route('/salud')
def salud():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # Para que Flask escuche en 0.0.0.0 dentro del contenedor
    app.run(host='0.0.0.0', port=PORT)
