// Obtén el botón y la sección de perfil por su ID
const toggleButton = document.getElementById('toggleProfileSection');
const profileSection = document.getElementById('profileSection');

// Agrega un controlador de eventos al botón
toggleButton.addEventListener('click', () => {
    // Cambia la visibilidad de la sección de perfil
    if (profileSection.style.display === 'none' || profileSection.style.display === '') {
        profileSection.style.display = 'block'; // Mostrar la sección
    } else {
        profileSection.style.display = 'none'; // Ocultar la sección
    }
});