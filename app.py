from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# ACTIVIDAD 1: Refactorice una función con errores
# Esta función ahora maneja errores de tipado correctamente
def calcular_riesgo_calor(temperatura):
    """
    Calcula el nivel de riesgo según la temperatura.
    
    Args:
        temperatura: Valor numérico de temperatura en Celsius
        
    Returns:
        str: Nivel de riesgo ('Alto', 'Medio', 'Bajo')
        
    Raises:
        TypeError: Si la temperatura no es un número válido
    """
    try:
        # Convertir a número si es string
        if isinstance(temperatura, str):
            temperatura = float(temperatura)
        elif not isinstance(temperatura, (int, float)):
            raise TypeError(f"La temperatura debe ser un número, recibido: {type(temperatura).__name__}")
        
        # Lógica corregida con comparaciones numéricas
        if temperatura > 30:
            return "Alto"
        elif temperatura > 20:
            return "Medio"
        else:
            return "Bajo"
            
    except ValueError as e:
        raise ValueError(f"No se pudo convertir '{temperatura}' a número válido: {str(e)}")


# Ruta principal que sirve el HTML
@app.route('/')
def index():
    """Sirve la página principal de la aplicación"""
    return render_template('index.html')


# ACTIVIDAD 4: Endpoint REST completo
@app.route('/api/clima', methods=['GET'])
def get_clima():
    """
    Endpoint GET que recibe una ciudad y devuelve temperatura y nivel de riesgo
    
    Query parameters:
        ciudad (str): Nombre de la ciudad a consultar
        
    Returns:
        JSON con: {
            "ciudad": str,
            "temperatura": float,
            "riesgo": str
        }
    """
    ciudad = request.args.get('ciudad')
    
    if not ciudad:
        return jsonify({
            "error": "Parámetro 'ciudad' es requerido"
        }), 400
    
    try:
        # Generar temperatura aleatoria entre -5 y 45°C
        temperatura = round(random.uniform(-5, 45), 1)
        
        # Calcular riesgo usando la función refactorizada
        riesgo = calcular_riesgo_calor(temperatura)
        
        return jsonify({
            "ciudad": ciudad.strip().title(),
            "temperatura": temperatura,
            "riesgo": riesgo
        }), 200
        
    except (TypeError, ValueError) as e:
        return jsonify({
            "error": f"Error al procesar la temperatura: {str(e)}"
        }), 500


# Ruta de prueba para calcular riesgo manualmente
@app.route('/api/riesgo', methods=['POST'])
def post_riesgo():
    """
    Endpoint POST para calcular riesgo con temperatura proporcionada
    
    Body JSON:
        {
            "temperatura": número
        }
        
    Returns:
        JSON con el nivel de riesgo o error
    """
    try:
        datos = request.get_json()
        
        if not datos or 'temperatura' not in datos:
            return jsonify({
                "error": "Body JSON debe contener 'temperatura'"
            }), 400
        
        temperatura = datos['temperatura']
        riesgo = calcular_riesgo_calor(temperatura)
        
        return jsonify({
            "temperatura": temperatura,
            "riesgo": riesgo
        }), 200
        
    except (TypeError, ValueError) as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
