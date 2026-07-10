import { useEffect, useState } from "react";
import MainLayout from "../layouts/MainLayout";
import SummaryCard from "../components/SummaryCard";
import { getDashboard } from "../services/dashboardService";

function Dashboard() {

    const [dashboard, setDashboard] = useState({
        patients: 0,
        doctors: 0,
        today_appointments: 0,
        upcoming_appointments: 0,
    });

    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadDashboard();
    }, []);

    const loadDashboard = async () => {
        try {
            const data = await getDashboard();
            setDashboard(data);
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <MainLayout>
            <h1 className="text-3xl font-bold mb-8">
                Dashboard
            </h1>

            {loading ? (
                <h2>Loading...</h2>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

                    <SummaryCard
                        title="Patients"
                        value={dashboard.patients}
                        color="bg-blue-600"
                    />

                    <SummaryCard
                        title="Doctors"
                        value={dashboard.doctors}
                        color="bg-green-600"
                    />

                    <SummaryCard
                        title="Today's Appointments"
                        value={dashboard.today_appointments}
                        color="bg-orange-500"
                    />

                    <SummaryCard
                        title="Upcoming Appointments"
                        value={dashboard.upcoming_appointments}
                        color="bg-purple-600"
                    />

                </div>
            )}
        </MainLayout>
    );
}

export default Dashboard;