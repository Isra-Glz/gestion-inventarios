import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <Link to="/">Dashboard</Link> |{" "}
      <Link to="/products">Productos</Link>
    </nav>
  );
}

export default Navbar;
