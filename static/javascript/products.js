
// JavaScript to fetch JSON data from the backend
// LISTO TODOS LOS PRODUCTOS 
fetch('/api/products/')
    .then(response => response.json())
    .then(products =>
    {
        const productList = document.getElementById('product-list');
        products.forEach(product =>
        {
            const productDiv = document.createElement('div');
            productDiv.classList.add('product-item');
            productDiv.innerHTML = `
                <div class="product-details">
                    <h2>${product.product_name}</h2>
                    <p>Description: ${product.product_desc}</p>
                    <p>Price: ${product.product_price}</p>
                    <div class="product-actions">
                        <button id="button" class="editar" onclick="editProduct(${product.product_id})">Editar</button>
                        <button id="button" class="eliminar" onclick="openModal(${product.product_id})">Eliminar</button>
                    </div>
                </div>
                <img src="${product.product_image_path}" alt="${product.product_name}" class="product-image">
            `;
            productList.appendChild(productDiv);
        });
    })
    .catch(error => console.error('Error fetching products:', error));


function editProduct(productId)
{
    // aca va la lógica para editar el producto
    console.log(`Editar producto con ID: ${productId}`);
    // Construir la URL con el ID del producto
    const url = `/api/products/edit/${productId}`;

    // Redirigir a la nueva URL
    window.location.href = url;

}

/*
// Función para eliminar un producto
function deleteProduct(productId)
{
    // aca va la lógica para eliminar el producto
    console.log(`Eliminar producto con ID: ${productId}`);

    const url = `/api/products/delete/${productId}`;

    // Redirigir a la nueva URL
    window.location.href = url;
}

*/

/******************************************************************************** */
/*                  LOGICA PARA CONFIRMAR UN DELETE                             */
/***************************************************************************** */

let productIdToDelete;

// Función para abrir la modal y establecer el ID del producto a eliminar
function openModal(productId)
{
    productIdToDelete = productId;
    document.getElementById('myModal').style.display = 'block';
}

// Función para cerrar la modal
function closeModal()
{
    document.getElementById('myModal').style.display = 'none';
}

// Función para confirmar la eliminación
function confirmDelete()
{
    closeModal();

    // Construir la URL para eliminar el producto
    const url = `/api/products/delete/${productIdToDelete}`;
    console.log(url)
    // Redirigir a la nueva URL
    window.location.href = url;

}