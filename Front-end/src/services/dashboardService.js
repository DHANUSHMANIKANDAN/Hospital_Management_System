import API from "../api/axios";

export const getDashboard = async () => {
    const response = await API.get("dashboard/");
    return response.data;
};

export const globalSearch = async (query) => {
    const response = await API.get(`dashboard/search/?q=${query}`);
    return response.data;
};