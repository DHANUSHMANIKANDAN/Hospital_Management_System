import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../services/authService";

function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");


const handleLogin = async (e) => {
    e.preventDefault();

    setError("");

    if (!email || !password) {
        setError("Please fill all fields");
        return;
    }

    try {

        setLoading(true);

        const data = await login(email, password);

        localStorage.setItem(
            "access_token",
            data.access
        );

        localStorage.setItem(
            "refresh_token",
            data.refresh
        );

        localStorage.setItem(
            "username",
            data.username
        );

        navigate("/dashboard");

    } catch (error) {

        setError(
            error.response?.data?.message ||
            "Invalid email or password"
        );

    } finally {

        setLoading(false);

    }
};


    return (

        <div className="min-h-screen bg-gray-100 flex items-center justify-center">

            <div className="bg-white w-full max-w-md rounded-xl shadow-lg p-8">

                <h1 className="text-3xl font-bold text-center text-blue-600 mb-8">

                    Hospital Management System

                </h1>

                <form
                    onSubmit={handleLogin}
                    className="space-y-5"
                >

                    <div>

                        <label className="block mb-2 font-medium">

                            Email

                        </label>

                        <input

                            type="email"

                            value={email}

                            onChange={(e)=>setEmail(e.target.value)}

                            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"

                            placeholder="Enter email"

                        />

                    </div>


                    <div>

                        <label className="block mb-2 font-medium">

                            Password

                        </label>

                        <input

                            type="password"

                            value={password}

                            onChange={(e)=>setPassword(e.target.value)}

                            className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"

                            placeholder="Enter password"

                        />

                    </div>


                    {

                        error &&

                        <p className="text-red-500 text-sm">

                            {error}

                        </p>

                    }


                    <button

                        type="submit"

                        disabled={loading}

                        className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg font-semibold transition"

                    >

                        {

                            loading ?

                            "Logging in..."

                            :

                            "Login"

                        }

                    </button>


                </form>

            </div>

        </div>

    )

}

export default Login;