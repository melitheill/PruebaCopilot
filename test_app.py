import unittest
from app import calcular_riesgo_calor


class TestCalcularRiesgoCalor(unittest.TestCase):
    """
    Suite de pruebas unitarias para la función calcular_riesgo_calor.
    Cubre casos normales, casos de borde y manejo de errores.
    """

    # ============================================================================
    # PRUEBAS DE CASOS NORMALES
    # ============================================================================

    def test_calor_extremo_40_grados(self):
        """
        Prueba: Temperatura extrema de 40°C
        Resultado esperado: "Alto"
        """
        resultado = calcular_riesgo_calor(40)
        self.assertEqual(resultado, "Alto", 
                        "A 40°C, el riesgo debería ser 'Alto'")

    def test_calor_extremo_45_grados(self):
        """
        Prueba: Temperatura extrema de 45°C
        Resultado esperado: "Alto"
        """
        resultado = calcular_riesgo_calor(45)
        self.assertEqual(resultado, "Alto",
                        "A 45°C, el riesgo debería ser 'Alto'")

    def test_clima_templado_22_grados(self):
        """
        Prueba: Temperatura templada de 22°C
        Resultado esperado: "Medio"
        """
        resultado = calcular_riesgo_calor(22)
        self.assertEqual(resultado, "Medio",
                        "A 22°C, el riesgo debería ser 'Medio'")

    def test_clima_templado_25_grados(self):
        """
        Prueba: Temperatura templada de 25°C
        Resultado esperado: "Medio"
        """
        resultado = calcular_riesgo_calor(25)
        self.assertEqual(resultado, "Medio",
                        "A 25°C, el riesgo debería ser 'Medio'")

    def test_clima_frio_10_grados(self):
        """
        Prueba: Temperatura fría de 10°C
        Resultado esperado: "Bajo"
        """
        resultado = calcular_riesgo_calor(10)
        self.assertEqual(resultado, "Bajo",
                        "A 10°C, el riesgo debería ser 'Bajo'")

    def test_clima_frio_negativo_5_grados(self):
        """
        Prueba: Temperatura muy fría de -5°C
        Resultado esperado: "Bajo"
        """
        resultado = calcular_riesgo_calor(-5)
        self.assertEqual(resultado, "Bajo",
                        "A -5°C, el riesgo debería ser 'Bajo'")

    # ============================================================================
    # PRUEBAS DE CASOS DE BORDE (BOUNDARY TESTING)
    # ============================================================================

    def test_borde_exacto_20_grados(self):
        """
        Prueba de borde: Temperatura exactamente en 20°C (límite inferior)
        Resultado esperado: "Bajo" (porque 20 no es > 20)
        """
        resultado = calcular_riesgo_calor(20)
        self.assertEqual(resultado, "Bajo",
                        "A exactamente 20°C, el riesgo debería ser 'Bajo' (no > 20)")

    def test_borde_justo_arriba_20_grados(self):
        """
        Prueba de borde: Temperatura justo arriba de 20°C (20.1°C)
        Resultado esperado: "Medio" (porque 20.1 > 20)
        """
        resultado = calcular_riesgo_calor(20.1)
        self.assertEqual(resultado, "Medio",
                        "A 20.1°C, el riesgo debería ser 'Medio' (> 20)")

    def test_borde_exacto_30_grados(self):
        """
        Prueba de borde: Temperatura exactamente en 30°C (límite superior)
        Resultado esperado: "Medio" (porque 30 no es > 30)
        """
        resultado = calcular_riesgo_calor(30)
        self.assertEqual(resultado, "Medio",
                        "A exactamente 30°C, el riesgo debería ser 'Medio' (no > 30)")

    def test_borde_justo_arriba_30_grados(self):
        """
        Prueba de borde: Temperatura justo arriba de 30°C (30.1°C)
        Resultado esperado: "Alto" (porque 30.1 > 30)
        """
        resultado = calcular_riesgo_calor(30.1)
        self.assertEqual(resultado, "Alto",
                        "A 30.1°C, el riesgo debería ser 'Alto' (> 30)")

    # ============================================================================
    # PRUEBAS CON CONVERSIÓN DE STRINGS
    # ============================================================================

    def test_string_temperatura_40(self):
        """
        Prueba: Recibir temperatura como string "40"
        Resultado esperado: Conversión exitosa a "Alto"
        """
        resultado = calcular_riesgo_calor("40")
        self.assertEqual(resultado, "Alto",
                        "String '40' debería convertirse y retornar 'Alto'")

    def test_string_temperatura_22(self):
        """
        Prueba: Recibir temperatura como string "22"
        Resultado esperado: Conversión exitosa a "Medio"
        """
        resultado = calcular_riesgo_calor("22")
        self.assertEqual(resultado, "Medio",
                        "String '22' debería convertirse y retornar 'Medio'")

    def test_string_temperatura_decimal(self):
        """
        Prueba: Recibir temperatura como string con decimales "25.5"
        Resultado esperado: Conversión exitosa a "Medio"
        """
        resultado = calcular_riesgo_calor("25.5")
        self.assertEqual(resultado, "Medio",
                        "String '25.5' debería convertirse y retornar 'Medio'")

    def test_float_temperatura(self):
        """
        Prueba: Recibir temperatura como float 28.7
        Resultado esperado: "Medio"
        """
        resultado = calcular_riesgo_calor(28.7)
        self.assertEqual(resultado, "Medio",
                        "Float 28.7 debería retornar 'Medio'")

    # ============================================================================
    # PRUEBAS DE MANEJO DE ERRORES
    # ============================================================================

    def test_error_string_invalido(self):
        """
        Prueba: Enviar un texto no numérico "ABC"
        Resultado esperado: Lanzar ValueError
        """
        with self.assertRaises(ValueError) as context:
            calcular_riesgo_calor("ABC")
        
        self.assertIn("No se pudo convertir", str(context.exception),
                     "Debería lanzar ValueError con mensaje descriptivo")

    def test_error_string_vacio(self):
        """
        Prueba: Enviar un string vacío ""
        Resultado esperado: Lanzar ValueError
        """
        with self.assertRaises(ValueError):
            calcular_riesgo_calor("")

    def test_error_tipo_lista(self):
        """
        Prueba: Enviar una lista [25] en lugar de número
        Resultado esperado: Lanzar TypeError
        """
        with self.assertRaises(TypeError) as context:
            calcular_riesgo_calor([25])
        
        self.assertIn("debe ser un número", str(context.exception),
                     "Debería lanzar TypeError con mensaje descriptivo")

    def test_error_tipo_diccionario(self):
        """
        Prueba: Enviar un diccionario {"temp": 25}
        Resultado esperado: Lanzar TypeError
        """
        with self.assertRaises(TypeError):
            calcular_riesgo_calor({"temp": 25})

    def test_error_tipo_none(self):
        """
        Prueba: Enviar None como temperatura
        Resultado esperado: Lanzar TypeError
        """
        with self.assertRaises(TypeError):
            calcular_riesgo_calor(None)

    def test_error_string_parcialmente_numerico(self):
        """
        Prueba: Enviar string con números y letras "25C"
        Resultado esperado: Lanzar ValueError
        """
        with self.assertRaises(ValueError):
            calcular_riesgo_calor("25C")

    # ============================================================================
    # PRUEBAS ADICIONALES DE CASOS EXTREMOS
    # ============================================================================

    def test_temperatura_cero(self):
        """
        Prueba: Temperatura de 0°C (punto de congelación del agua)
        Resultado esperado: "Bajo"
        """
        resultado = calcular_riesgo_calor(0)
        self.assertEqual(resultado, "Bajo",
                        "A 0°C, el riesgo debería ser 'Bajo'")

    def test_temperatura_muy_alta_100(self):
        """
        Prueba: Temperatura extrema de 100°C
        Resultado esperado: "Alto"
        """
        resultado = calcular_riesgo_calor(100)
        self.assertEqual(resultado, "Alto",
                        "A 100°C, el riesgo debería ser 'Alto'")

    def test_temperatura_muy_baja_negativa(self):
        """
        Prueba: Temperatura extremadamente baja de -40°C
        Resultado esperado: "Bajo"
        """
        resultado = calcular_riesgo_calor(-40)
        self.assertEqual(resultado, "Bajo",
                        "A -40°C, el riesgo debería ser 'Bajo'")

    def test_string_con_espacios(self):
        """
        Prueba: String con espacios " 25 "
        Resultado esperado: Conversión exitosa a "Medio"
        """
        resultado = calcular_riesgo_calor(" 25 ")
        self.assertEqual(resultado, "Medio",
                        "String ' 25 ' con espacios debería convertirse correctamente")


class TestCalcularRiesgoCalorIntegration(unittest.TestCase):
    """
    Pruebas de integración para verificar el comportamiento general
    y las transiciones entre rangos de riesgo.
    """

    def test_transicion_bajo_a_medio(self):
        """
        Prueba: Verificar transición correcta de "Bajo" a "Medio"
        """
        self.assertEqual(calcular_riesgo_calor(20), "Bajo")
        self.assertEqual(calcular_riesgo_calor(20.1), "Medio")

    def test_transicion_medio_a_alto(self):
        """
        Prueba: Verificar transición correcta de "Medio" a "Alto"
        """
        self.assertEqual(calcular_riesgo_calor(30), "Medio")
        self.assertEqual(calcular_riesgo_calor(30.1), "Alto")

    def test_rango_bajo_completo(self):
        """
        Prueba: Verificar que todo el rango bajo retorna "Bajo"
        """
        temperaturas_bajas = [-50, -10, 0, 5, 10, 15, 20]
        for temp in temperaturas_bajas:
            resultado = calcular_riesgo_calor(temp)
            self.assertEqual(resultado, "Bajo",
                           f"Temperatura {temp}°C debería ser 'Bajo'")

    def test_rango_medio_completo(self):
        """
        Prueba: Verificar que todo el rango medio retorna "Medio"
        """
        temperaturas_medias = [20.1, 22, 25, 28, 29.9, 30]
        for temp in temperaturas_medias:
            resultado = calcular_riesgo_calor(temp)
            self.assertEqual(resultado, "Medio",
                           f"Temperatura {temp}°C debería ser 'Medio'")

    def test_rango_alto_completo(self):
        """
        Prueba: Verificar que todo el rango alto retorna "Alto"
        """
        temperaturas_altas = [30.1, 35, 40, 50, 100]
        for temp in temperaturas_altas:
            resultado = calcular_riesgo_calor(temp)
            self.assertEqual(resultado, "Alto",
                           f"Temperatura {temp}°C debería ser 'Alto'")


if __name__ == '__main__':
    # Ejecutar pruebas con nivel de verbosidad 2
    unittest.main(verbosity=2)
