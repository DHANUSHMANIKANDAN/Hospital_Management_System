import React from "react";

function Navbar() {
  return (
    <nav className="flex items-center justify-between bg-white shadow px-6 py-4">
      <div>
        <h2 className="text-xl font-semibold text-gray-800">
          Hospital Management System
        </h2>
      </div>
      <div className="flex items-center gap-3">
        <span className="text-gray-600">Welcome, User</span>
        <div className="w-9 h-9 rounded-full bg-blue-500 flex items-center justify-center text-white font-medium">
          U
        </div>
      </div>
    </nav>
  );
}

export default Navbar;