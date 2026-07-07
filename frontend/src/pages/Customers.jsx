import { useEffect, useState } from "react";
import api from "../services/api";

function Customers() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    loadCustomers();
  }, []);

  const loadCustomers = () => {
    api
      .get("/customers")
      .then((res) => {
        setCustomers(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Customers</h1>

      <table className="w-full bg-white shadow rounded-xl">
        <thead>
          <tr className="border-b">
            <th className="p-3 text-left">ID</th>
            <th className="p-3 text-left">Name</th>
            <th className="p-3 text-left">Mobile</th>
            <th className="p-3 text-left">Balance</th>
          </tr>
        </thead>

        <tbody>
          {customers.map((customer) => (
            <tr key={customer.id} className="border-b">
              <td className="p-3">{customer.id}</td>
              <td className="p-3">{customer.name}</td>
              <td className="p-3">{customer.mobile}</td>
              <td className="p-3">₹{customer.balance}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Customers;