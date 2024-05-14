document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.querySelector('form');

    formulario.addEventListener('submit', function(evento) {
        const nombre = document.getElementById('nombre').value.trim();
        const apellido = document.getElementById('apellido').value.trim();
        const email = document.getElementById('email').value.trim();
        const comentario = document.getElementById('comentario').value.trim();
        const direccion = document.getElementById('direccion').value.trim();

        if (!nombre || !apellido || !email || !comentario) {
            evento.preventDefault();
            alert('Uno o más campos requeridos no fueron completados. Complételos antes de enviar el formulario');
        }
    });
});

<script setup lang="ts">
import { ref } from "vue";
const WEB3FORMS_ACCESS_KEY = "87d1e17f-ce99-4984-bea7-c39ece2eb541";
const name = ref("")
const email = ref("")
const message = ref("")

const submitForm = async () => {
const response = await fetch("https://api.web3forms.com/submit", {
    method: "POST",
    headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
    },
    body: JSON.stringify({
    access_key: 87d1e17f-ce99-4984-bea7-c39ece2eb541,
    name: name.value,
    email: email.value,
    message: message.value,
    }),
});
const result = await response.json();
if (result.success) {
    console.log(result);
}
}
</script>
<template>
<form @submit.prevent="submitForm">
    <input type="text" name="name" v-model="name"/>
    <input type="email" name="email"  v-model="email"/> 
    <textarea name="message" v-model="message"></textarea>
    <button type="submit">Send Message</button>
</form>
</template>
