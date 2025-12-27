import { useState, ChangeEvent, FormEvent } from "react";
import { crearProducto } from "../services/api";

interface ProductoFormData {
  nombre: string;
  descripcion: string;
  id_categoria: string;
  stock: string;
  precio: string;
}

export default function ProductoForm() {
  const [form, setForm] = useState<ProductoFormData>({
    nombre: "",
    descripcion: "",
    id_categoria: "",
    stock: "",
    precio: "",
  });

  const [mensaje, setMensaje] = useState<string>("");

  function handleChange(e: ChangeEvent<HTMLInputElement>) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    try {
      await crearProducto({
        nombre: form.nombre,
        descripcion: form.descripcion,
        id_categoria: Number(form.id_categoria),
        stock: Number(form.stock),
        precio: Number(form.precio),
      });

      setMensaje("Producto creado correctamente ✅");
      setForm({
        nombre: "",
        descripcion: "",
        id_categoria: "",
        stock: "",
        precio: "",
      });
    } catch (error: any) {
      setMensaje(error.message);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Alta de Producto</h2>

      <input name="nombre" placeholder="Nombre" value={form.nombre} onChange={handleChange} required />
      <input name="descripcion" placeholder="Descripción" value={form.descripcion} onChange={handleChange} required />
      <input name="id_categoria" placeholder="ID Categoría" value={form.id_categoria} onChange={handleChange} required />
      <input name="stock" placeholder="Stock" value={form.stock} onChange={handleChange} required />
      <input name="precio" placeholder="Precio" value={form.precio} onChange={handleChange} required />

      <button type="submit">Guardar</button>

      {mensaje && <p>{mensaje}</p>}
    </form>
  );
}
