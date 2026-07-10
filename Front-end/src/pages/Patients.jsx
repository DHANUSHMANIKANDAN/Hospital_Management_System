import React, { useEffect, useState } from "react";
import {
  getPatients,
  addPatient,
  updatePatient,
  deletePatient,
} from "../services/patientService";
import PatientTable from "../components/PatientTable";
import PatientFormModal from "../components/PatientFormModal";
import ConfirmDeleteModal from "../components/ConfirmDeleteModal";
import Pagination from "../components/Pagination";

const PAGE_SIZE = 5;

function Patients() {
  const [patients, setPatients] = useState([]);
  const [search, setSearch] = useState("");
  const [currentPage, setCurrentPage] = useState(1);

  const [isFormOpen, setIsFormOpen] = useState(false);
  const [editingPatient, setEditingPatient] = useState(null);

  const [isDeleteOpen, setIsDeleteOpen] = useState(false);
  const [deletingPatient, setDeletingPatient] = useState(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchPatients = async () => {
    try {
      setLoading(true);
      const res = await getPatients();
      setPatients(res.data);
    } catch (err) {
      setError("Failed to load patients.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPatients();
  }, []);

  const filtered = patients.filter((p) =>
    p.name?.toLowerCase().includes(search.toLowerCase())
  );

  const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
  const paginated = filtered.slice(
    (currentPage - 1) * PAGE_SIZE,
    currentPage * PAGE_SIZE
  );

  const openAddModal = () => {
    setEditingPatient(null);
    setIsFormOpen(true);
  };

  const openEditModal = (patient) => {
    setEditingPatient(patient);
    setIsFormOpen(true);
  };

  const handleSave = async (formData) => {
    try {
      if (editingPatient) {
        await updatePatient(editingPatient.id, formData);
      } else {
        await addPatient(formData);
      }
      setIsFormOpen(false);
      fetchPatients();
    } catch (err) {
      alert("Failed to save patient.");
    }
  };

  const openDeleteModal = (patient) => {
    setDeletingPatient(patient);
    setIsDeleteOpen(true);
  };

  const handleDeleteConfirm = async () => {
    try {
      await deletePatient(deletingPatient.id);
      setIsDeleteOpen(false);
      fetchPatients();
    } catch (err) {
      alert("Failed to delete patient.");
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
        <h1 className="text-2xl font-semibold text-gray-800">Patients</h1>
        <div className="flex gap-3">
          <input
            type="text"
            placeholder="Search by name..."
            value={search}
            onChange={(e) => {
              setSearch(e.target.value);
              setCurrentPage(1);
            }}
            className="border rounded-md px-3 py-2 text-sm w-56 focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <button
            onClick={openAddModal}
            className="bg-blue-500 text-white px-4 py-2 rounded-md text-sm hover:bg-blue-600"
          >
            + Add Patient
          </button>
        </div>
      </div>

      {loading && <p className="text-gray-500">Loading patients...</p>}
      {error && <p className="text-red-500">{error}</p>}

      {!loading && !error && (
        <>
          <PatientTable
            patients={paginated}
            onEdit={openEditModal}
            onDelete={openDeleteModal}
          />
          <Pagination
            currentPage={currentPage}
            totalPages={totalPages}
            onPageChange={setCurrentPage}
          />
        </>
      )}

      <PatientFormModal
        isOpen={isFormOpen}
        onClose={() => setIsFormOpen(false)}
        onSave={handleSave}
        patient={editingPatient}
      />

      <ConfirmDeleteModal
        isOpen={isDeleteOpen}
        onClose={() => setIsDeleteOpen(false)}
        onConfirm={handleDeleteConfirm}
        patientName={deletingPatient?.name}
      />
    </div>
  );
}

export default Patients;