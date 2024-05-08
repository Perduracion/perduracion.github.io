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



const form = document.getElementById('form');
const result = document.getElementById('result');

form.addEventListener('submit', function(e) {
e.preventDefault();
const formData = new FormData(form);
const object = Object.fromEntries(formData);
const json = JSON.stringify(object);
result.innerHTML = "Por favor espere..."

    fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: json
        })
        .then(async (response) => {
            let json = await response.json();
            if (response.status == 200) {
                result.innerHTML = json.message;
            } else {
                console.log(response);
                result.innerHTML = json.message;
            }
        })
        .catch(error => {
            console.log(error);
            result.innerHTML = "Algo salio mal!";
        })
        .then(function() {
            form.reset();
            setTimeout(() => {
                result.style.display = "none";
            }, 3000);
        });
});