import React from "react";
import { Link } from "react-router-dom";

function Sidebar() {
  const links = [
    { name: "Dashboard", path: "/dashboard" },
    { name: "Patients", path: "/patients" },
    { name: "Doctors", path: "/doctors" },
    { name: "Appointments", path: "/appointments" },
  ];

  return (
    <aside className="w-64 min-h-screen bg-gray-900 text-white flex flex-col">
      <div className="px-6 py-5 text-lg font-bold border-b border-gray-700">
        HMS
      </div>
      <ul className="flex-1 px-3 py-4 space-y-1">
        {links.map((link) => (
          <li key={link.path}>
            <Link
              to={link.path}
              className="block px-3 py-2 rounded-md text-gray-300 hover:bg-gray-800 hover:text-white transition-colors"
            >
              {link.name}
            </Link>
          </li>
        ))}
      </ul>
    </aside>
  );
}

export default Sidebar;