import API from "../api/axios";

export const getAppointments = () => {
    return API.get("appointments/");
};

export const createAppointment = (data) => {
    return API.post("appointments/", data);
};

export const updateAppointment = (id, data) => {
    return API.put(`appointments/${id}/`, data);
};

export const cancelAppointment = (id) => {
    return API.patch(`appointments/${id}/`);
};

export const deleteAppointment = (id) => {
    return API.delete(`appointments/${id}/`);
};