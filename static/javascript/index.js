document.addEventListener('DOMContentLoaded', function ()
{
    const formulario = document.querySelector('form');

    formulario.addEventListener('submit', function (evento)
    {
        const nombre = document.getElementById('nombre').value.trim();
        const apellido = document.getElementById('apellido').value.trim();
        const email = document.getElementById('email').value.trim();
        const comentario = document.getElementById('comentario').value.trim();
        const direccion = document.getElementById('direccion').value.trim();

        if (!nombre || !apellido || !email || !comentario)
        {
            evento.preventDefault();
            alert('Uno o más campos requeridos no fueron completados. Complételos antes de enviar el formulario');
        }
    });
});



/** js para menu responsive al usar la web en celulares */

let showMenu = false;

function toggleMenu()
{
    if (showMenu)
    {
        document.getElementById("nav").classList = "";
        showMenu = false;
    } else
    {
        document.getElementById("nav").classList = "responsive";
        showMenu = true;
    }
}


function closeMenu()
{
    document.getElementById("nav").classList = "";
    showMenu = false;
}
