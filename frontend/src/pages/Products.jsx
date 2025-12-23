import { useEffect, useState } from "react";
import axios from "axios";

function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/inventario")
      .then((res) => {
        console.log("DATA BACKEND:", res.data);
        setProducts(res.data);
      })
      .catch((err) => {
        console.error("Error cargando inventario:", err);
      });
  }, []);

  return (
    <div>
      <h1>Productos</h1>

      {products.length === 0 && <p>No hay productos</p>}

      <ul>
        {products.map((p) => (
          <li key={p.id}>
            {p.name} — {p.quantity}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Products;
