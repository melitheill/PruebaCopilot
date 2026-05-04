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
        // Llamada al endpoint que crearás con Copilot en el backend
        const response = await fetch(`/api/clima?ciudad=${ciudad}`);
        
        // ACTIVIDAD 3: Solicite explicación de una excepción
        // Si la respuesta no es ok, lanzamos un error para que Copilot nos explique
        if (!response.ok) {
            throw new Error("API_OFFLINE: El servidor no responde o el endpoint no existe");
        }

        const data = await response.json();
        
        // Mostramos el resultado
        divResultado.innerHTML = `
            <p>Ciudad: <strong>${data.ciudad}</strong></p>
            <p>Temperatura: ${data.temperatura}°C</p>
            <p>Riesgo: ${data.riesgo}</p>
        `;

    } catch (error) {
        console.error("Error detectado:", error);
        divResultado.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
        // TIP: Aquí puedes sombrear 'error.message' y preguntarle a Copilot: 
        // "¿Por qué este fetch me está dando este error?"
    }
});
