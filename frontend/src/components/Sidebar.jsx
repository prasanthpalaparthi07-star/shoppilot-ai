import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div className="w-64 h-screen bg-slate-900 text-white p-6">
      <h1 className="text-2xl font-bold mb-8">
        🏪 ShopPilot AI
      </h1>

      <ul className="space-y-4">

        <li className="hover:text-blue-400">
          <Link to="/">📊 Dashboard</Link>
        </li>

        <li className="hover:text-blue-400">
          <Link to="/products">📦 Products</Link>
        </li>

        <li className="hover:text-blue-400">
          <Link to="/inventory">📈 Inventory</Link>
        </li>

        <li className="hover:text-blue-400">
          <Link to="/billing">🧾 Billing</Link>
        </li>

        <li className="hover:text-blue-400">
          <Link to="/customers">👥 Customers</Link>
        </li>

        <li className="hover:text-blue-400">
          <Link to="/settings">⚙️ Settings</Link>
        </li>

      </ul>
    </div>
  );
}

export default Sidebar;