document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.querySelector('form');

    formulario.addEventListener('submit', function(evento) {
        const nombre = document.getElementById('nombre').value.trim();
        const apellido = document.getElementById('apellido').value.trim();
        const email = document.getElementById('email').value.trim();

        if (!nombre || !apellido || !email) {
            evento.preventDefault(); // Evita que el formulario se envíe
            alert('Por favor, completa los campos de nombre, apellido y correo electrónico.');
        }
    });
});
