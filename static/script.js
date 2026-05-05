// Selección de elementos del DOM
const btnConsultar = document.getElementById('btnConsultar');
const inputCiudad = document.getElementById('ciudad');
const divResultado = document.getElementById('resultado');

// Evento para el botón
btnConsultar.addEventListener('click', async () => {
    const ciudad = inputCiudad.value;
    
    if (!ciudad) {
        alert("Por favor, escribe una ciudad");
        return;
    }

    try {
        // Mostrar estado de carga
        divResultado.innerHTML = '<p>⏳ Cargando...</p>';
        divResultado.classList.add('visible');
        
        // Llamada al endpoint /api/clima con la ciudad como parámetro
        const response = await fetch(`/api/clima?ciudad=${encodeURIComponent(ciudad)}`);
        
        // Si la respuesta no es ok, lanzamos un error
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || `Error ${response.status}: El servidor no responde correctamente`);
        }

        const data = await response.json();
        
        // Mostramos el resultado con mejor formato
        const temperaturaColor = data.temperatura > 30 ? '#d32f2f' : (data.temperatura > 20 ? '#f57f17' : '#1976d2');
        const riesgoEmoji = data.riesgo === 'Alto' ? '🔴' : (data.riesgo === 'Medio' ? '🟡' : '🟢');
        
        divResultado.innerHTML = `
            <p><strong>📍 Ciudad:</strong> ${data.ciudad}</p>
            <p><strong>🌡️ Temperatura:</strong> <span style="color: ${temperaturaColor}; font-weight: bold;">${data.temperatura}°C</span></p>
            <p><strong>⚠️ Nivel de Riesgo:</strong> <span style="font-weight: bold;">${riesgoEmoji} ${data.riesgo}</span></p>
        `;

    } catch (error) {
        console.error("Error detectado:", error);
        divResultado.innerHTML = `<p class="error">❌ Error: ${error.message}</p>`;
        divResultado.classList.add('visible');
    }
});
