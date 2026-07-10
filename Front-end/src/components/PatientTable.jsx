import React from "react";
import { useNavigate } from "react-router-dom";

function PatientTable({ patients, onEdit, onDelete }) {
  const navigate = useNavigate();

  return (
    <div className="overflow-x-auto bg-white rounded-lg shadow">
      <table className="min-w-full text-sm text-left">
        <thead className="bg-gray-100 text-gray-600 uppercase text-xs">
          <tr>
            <th className="px-4 py-3">Name</th>
            <th className="px-4 py-3">Age</th>
            <th className="px-4 py-3">Gender</th>
            <th className="px-4 py-3">Phone</th>
            <th className="px-4 py-3 text-right">Actions</th>
          </tr>
        </thead>
        <tbody className="divide-y">
          {patients.length === 0 && (
            <tr>
              <td colSpan={5} className="px-4 py-6 text-center text-gray-400">
                No patients found.
              </td>
            </tr>
          )}
          {patients.map((patient) => (
            <tr key={patient.id} className="hover:bg-gray-50">
              <td
                className="px-4 py-3 font-medium text-blue-600 cursor-pointer hover:underline"
                onClick={() => navigate(`/patients/${patient.id}`)}
              >
                {patient.name}
              </td>
              <td className="px-4 py-3">{patient.age}</td>
              <td className="px-4 py-3">{patient.gender}</td>
              <td className="px-4 py-3">{patient.phone}</td>
              <td className="px-4 py-3">
                <div className="flex justify-end gap-3">
                  <button
                    onClick={() => navigate(`/patients/${patient.id}`)}
                    className="text-gray-500 hover:text-blue-600 text-xs"
                  >
                    View
                  </button>
                  <button
                    onClick={() => onEdit(patient)}
                    className="text-gray-500 hover:text-green-600 text-xs"
                  >
                    Edit
                  </button>
                  <button
                    onClick={() => onDelete(patient)}
                    className="text-gray-500 hover:text-red-600 text-xs"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default PatientTable;