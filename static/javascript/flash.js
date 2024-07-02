
/********************************   */
/* funcion flash para mensajes      */
/********************************* */

document.addEventListener('DOMContentLoaded', function ()
{
    var form = document.querySelector('form[action^="/api/products/"]');
    if (form)
    {
        form.addEventListener('submit', function (event)
        {
            event.preventDefault(); // Evitar el envío del formulario por defecto

            // Mostrar el mensaje flash y esperar 5 segundos
            var alert = document.querySelector('.alert');
            if (alert)
            {
                alert.style.display = 'block'; // Mostrar el mensaje flash

                setTimeout(function ()
                {
                    alert.style.display = 'none'; // Ocultar el mensaje flash después de 5 segundos
                    form.submit(); // Enviar el formulario después de ocultar el mensaje
                }, 5000); // 5000 milisegundos = 5 segundos
            }
        });
    }
});