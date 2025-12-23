import axios from "axios";

export const getInventory = async () => {
  const response = await axios.get("http://localhost:8000/inventario");
  return response.data;
};
