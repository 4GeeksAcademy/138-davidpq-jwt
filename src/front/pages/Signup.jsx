import React, { useState } from "react";
import useGlobalReducer from "../hooks/useGlobalReducer";
import { useNavigate } from "react-router-dom";
import { loginService, signupService } from "../services/AuthServices";

export default function Signup() {
    const { dispatch } = useGlobalReducer();
    const navigate = useNavigate();
    const [form, setForm] = useState({ email: "", username: "", password: "" });

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const [data, error] = await signupService(form);

        if (error) {
            alert(error);
            return;
        }
        dispatch({ type: "login", payload: { token: data.token, user: data.user } });
        navigate("/demo");
    };

    return (
        <div className="container d-flex justify-content-center align-items-center vh-100 bg-light">
            <div
                className="card shadow p-4"
                style={{ maxWidth: "380px", width: "100%" }}
            >
                <h3 className="text-center mb-4">Crear cuenta</h3>

                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label className="form-label">Correo electrónico</label>
                        <input type="email" className="form-control" name="email" placeholder="tuemail@ejemplo.com" required onChange={handleChange}/>
                    </div>

                    <div className="mb-3">
                        <label className="form-label">Usuario</label>
                        <input type="text" className="form-control" name="username" placeholder="Nombre de usuario" required onChange={handleChange}/>
                    </div>

                    <div className="mb-3">
                        <label className="form-label">Contraseña</label>
                        <input type="password" className="form-control" name="password" placeholder="••••••••" required onChange={handleChange}/>
                    </div>

                    <button type="submit" className="btn btn-success w-100">
                        Registrarse
                    </button>

                    <div className="text-center mt-3">
                        <a href="#" className="text-decoration-none">
                            ¿Ya tienes cuenta? Inicia sesión
                        </a>
                    </div>
                </form>
            </div>
        </div>
    );
}
