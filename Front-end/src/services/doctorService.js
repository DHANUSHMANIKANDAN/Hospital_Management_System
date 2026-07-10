import API from "../api/axios";

export const getDoctors = () => {
    return API.get("doctors/");
};

export const getDoctor = (id) => {
    return API.get(`doctors/${id}/`);
};

export const createDoctor = (data) => {
    return API.post("doctors/", data);
};

export const updateDoctor = (id, data) => {
    return API.put(`doctors/${id}/`, data);
};

export const deleteDoctor = (id) => {
    return API.delete(`doctors/${id}/`);
};

export const searchDoctor = (name) => {
    return API.get(`doctors/?search=${name}`);
};