const API_URL = "http://127.0.0.1:8000";

interface ProductoCreate {
  nombre: string;
  descripcion: string;
  id_categoria: number;
  stock: number;
  precio: number;
}

export async function crearProducto(producto: ProductoCreate) {
  const response = await fetch(`${API_URL}/productos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(producto),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Error al crear producto");
  }

  return response.json();
}
