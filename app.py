from flask import Flask, request, jsonify, render_template
from hillClimbingIterative import hill_climbing_iterativo, obtener_ciudades

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', ciudades=obtener_ciudades())

@app.route('/resolver', methods=['POST'])
def resolver():
    ciudad_inicio = request.form.get('ciudad')
    if ciudad_inicio not in obtener_ciudades():
        return jsonify({'error': 'Ciudad no válida'}), 400

    ruta, distancia_total = hill_climbing_iterativo(ciudad_inicio, max_iteraciones=10)
    return jsonify({'ruta': ruta, 'distancia': round(distancia_total, 2)})

if __name__ == '__main__':
    app.run(debug=True)
