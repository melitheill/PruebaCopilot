from flask import Flask, jsonify, request

app = Flask(__name__)

# ACTIVIDAD 1: Refactorice una función con errores
# Esta función tiene errores de lógica y tipado. 
# Pide al Copilot: "Refactoriza esta función para que maneje errores y sea más limpia"
def calcular_riesgo_calor(temperatura):
    if temperatura > "30": # Error: comparando string con int
        res = "Alto"
    elif temperatura > 20:
        res = "Medio"
    else:
        res = "Bajo"
    return res

# ACTIVIDAD 4: Cree un endpoint REST completo desde comentarios
# Escribe este comentario y deja que Copilot haga el resto:
# // Crear un endpoint GET en '/api/clima' que reciba una ciudad 
# // y devuelva un JSON con temperatura aleatoria y el nivel de riesgo

if __name__ == '__main__':
    app.run(debug=True)
