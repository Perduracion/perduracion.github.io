
/********************************   */
/* funcion flash para mensajes      */
/********************************* */

var alert = document.querySelector('.alert');
if (alert)
    alert.style.display = 'block'; // Mostrar el mensaje flash

setTimeout(function ()
{
    alert.style.display = 'none'; // Ocultar el mensaje flash después de 5 segundos
    form.submit(); // Enviar el formulario después de ocultar el mensaje
}, 3000); // 5000 milisegundos = 3 segundos