
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
                        <button onclick="editProduct(${product.product_id})">Editar</button>
                        <button onclick="deleteProduct(${product.product_id})">Eliminar</button>
                    </div>
                </div>
                <img src="${product.product_image_path}" alt="${product.product_name}" class="product-image">
            `;
            productList.appendChild(productDiv);
        });
    })
    .catch(error => console.error('Error fetching products:', error));

// falta implementar la edicion y eliminacion 
function editProduct(productId)
{
    // aca va la lógica para editar el producto
    console.log(`Editar producto con ID: ${productId}`);
}

// Función para eliminar un producto
function deleteProduct(productId)
{
    // aca va la lógica para eliminar el producto
    console.log(`Eliminar producto con ID: ${productId}`);
}
