import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getPatientById } from "../services/patientService";

function PatientProfile() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [patient, setPatient] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPatient = async () => {
      try {
        const res = await getPatientById(id);
        setPatient(res.data);
      } catch (err) {
        setError("Failed to load patient profile.");
      } finally {
        setLoading(false);
      }
    };
    fetchPatient();
  }, [id]);

  if (loading) return <p className="text-gray-500">Loading...</p>;
  if (error) return <p className="text-red-500">{error}</p>;
  if (!patient) return <p className="text-gray-500">Patient not found.</p>;

  return (
    <div className="max-w-2xl">
      <button
        onClick={() => navigate("/patients")}
        className="text-sm text-blue-500 hover:underline mb-4"
      >
        ← Back to Patients
      </button>

      <div className="bg-white rounded-lg shadow p-6 space-y-4">
        <div className="flex items-center gap-4">
          <div className="w-16 h-16 rounded-full bg-blue-500 text-white flex items-center justify-center text-xl font-semibold">
            {patient.name?.charAt(0)}
          </div>
          <div>
            <h2 className="text-xl font-semibold text-gray-800">{patient.name}</h2>
            <p className="text-sm text-gray-500">{patient.gender}, {patient.age} yrs</p>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4 pt-4 border-t">
          <div>
            <p className="text-xs text-gray-400 uppercase">Phone</p>
            <p className="text-gray-700">{patient.phone}</p>
          </div>
          <div>
            <p className="text-xs text-gray-400 uppercase">Address</p>
            <p className="text-gray-700">{patient.address}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default PatientProfile;