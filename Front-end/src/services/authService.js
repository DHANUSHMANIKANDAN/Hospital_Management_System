import API from "../api/axios";

export const login = async (email, password) => {
    const response = await API.post("accounts/login/", {
        email,
        password,
    });

    return response.data;
};

export const logout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("username");
};

export const isAuthenticated = () => {
    return !!localStorage.getItem("access_token");
};