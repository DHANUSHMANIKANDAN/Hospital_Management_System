import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Patients from "../pages/Patients";
import PatientProfile from "../pages/PatientProfile";

function AppRoutes(){

    return(

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Login/>}
                />

                <Route
                    path="/dashboard"
                    element={<Dashboard/>}
                />

                <Route
                    path="/patients"
                    element={<Patients/>}
                />

                <Route
                    path="/patients/:id"
                    element={<PatientProfile />}
                />

            </Routes>

        </BrowserRouter>

    )

}

export default AppRoutes;