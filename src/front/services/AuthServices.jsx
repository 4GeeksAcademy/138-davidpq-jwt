const backendUrl = import.meta.env.VITE_BACKEND_URL;

export const loginService = async ({ email, password }) => {
    try {
        const response = await fetch(backendUrl + "/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password }),
        });

        if (!response.ok) {
            return [null, "Error al iniciar sesion"];
        }

        const data = await response.json();
        return [data, null];
    } catch (err) {
        return [null, err.message];
    }
};

export const getProfile = async (token) => {
    try {
        const response = await fetch(backendUrl + "/api/profile", {
            headers: { "Authorization": "Bearer " + token },
        });

        if (!response.ok) {
            return [null, "Token invalido"];
        }

        const data = await response.json();
        return [data, null];
    } catch (err) {
        return [null, err.message];
    }
};

export const signupService = async ({ email, username, password }) => {
    try {
        const response = await fetch(backendUrl + "/api/signup", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, username, password }),
        });

        if (!response.ok) {
            return [null, "Error al registrarse"];
        }

        const data = await response.json();
        return [data, null];
    } catch (err) {
        return [null, err.message];
    }
};