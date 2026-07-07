import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
  const [dashboard, setDashboard] = useState({
    total_products: 0,
    total_customers: 0,
    total_sales: 0,
    total_credit: 0,
    low_stock_products: 0,
  });

  useEffect(() => {
    api.get("/dashboard")
      .then((response) => {
        setDashboard(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">
        Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-gray-500">Products</h2>
          <p className="text-3xl font-bold mt-2">
            {dashboard.total_products}
          </p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-gray-500">Customers</h2>
          <p className="text-3xl font-bold mt-2">
            {dashboard.total_customers}
          </p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-gray-500">Sales</h2>
          <p className="text-3xl font-bold mt-2">
            {dashboard.total_sales}
          </p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-gray-500">Credit</h2>
          <p className="text-3xl font-bold mt-2">
            ₹{dashboard.total_credit}
          </p>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-gray-500">Low Stock</h2>
          <p className="text-3xl font-bold mt-2">
            {dashboard.low_stock_products}
          </p>
        </div>

      </div>
    </div>
  );
}

export default Dashboard;