

<script>
    const BASE = import.meta.env.VITE_API_BASE_URL;
    export default {
        data() {
            return {
                mode: 'login',
                form: {
                    username: '',
                    password: '',
                    passwordConfirm: ''
                },
                error: '',
                loading: false
            }
        },
        methods: {
            switchMode(m) {
                this.mode = m;
                this.error = '';
                this.form = { username: '', password: '', passwordConfirm: '' };
            },
            validate() {
                if (!this.form.username.trim() || !this.form.password.trim()) {
                    this.error = 'Заполните все поля';
                    return false;
                }
                if (this.form.password.length < 30) {
                    this.error = 'Пароль должен быть не менее 30 символов';
                    return false;
                }
                if (this.mode === 'register' && this.form.password !== this.form.passwordConfirm) {
                    this.error = 'Пароли не совпадают';
                    return false;
                }
                return true;
            },
            async submit() {
                this.error = '';
                if (!this.validate()) return;

                this.loading = true;
                try {
                    const url = this.mode === 'login'
                        ? `${BASE}/v1/user/authentication`
                        : `${BASE}/v1/user/registration`;

                    const res = await fetch(url, {
                        method: 'POST',
                        credentials: 'include',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            username: this.form.username,
                            password: this.form.password
                        })
                    });

                    if (!res.ok) {
                        const data = await res.json().catch(() => ({}));
                        this.error = data.detail || 'Ошибка, попробуйте снова';
                        return;
                    }

                    if (this.mode === 'register') {
                        this.switchMode('login');
                        this.error = '';
                        this._success = 'Аккаунт создан! Войдите.';
                    } else {
                        window.location.href = '/';
                    }
                } catch (e) {
                    this.error = 'Ошибка соединения с сервером';
                } finally {
                    this.loading = false;
                }
            }
        }
    }
</script>

<template>
    <div class="auth-page">
        <div class="auth-card">

            <div class="auth-header">
                <span class="auth-logo">🐍</span>
                <h1>SnakeSite</h1>
            </div>

            <div class="auth-tabs">
                <button
                    :class="['tab-btn', { active: mode === 'login' }]"
                    @click="switchMode('login')"
                >Вход</button>
                <button
                    :class="['tab-btn', { active: mode === 'register' }]"
                    @click="switchMode('register')"
                >Регистрация</button>
            </div>

            <div class="auth-form">

                <div class="field">
                    <label>Имя пользователя</label>
                    <input
                        v-model="form.username"
                        type="text"
                        placeholder="username"
                        autocomplete="username"
                        @keyup.enter="submit"
                    >
                </div>

                <div class="field">
                    <label>Пароль</label>
                    <input
                        v-model="form.password"
                        type="password"
                        placeholder="Минимум 30 символов"
                        autocomplete="current-password"
                        @keyup.enter="submit"
                    >
                    <span class="field-hint" :class="{ ok: form.password.length >= 30 }">
                        {{ form.password.length }} / 30
                    </span>
                </div>

                <div class="field" v-if="mode === 'register'">
                    <label>Повторите пароль</label>
                    <input
                        v-model="form.passwordConfirm"
                        type="password"
                        placeholder="••••••••"
                        autocomplete="new-password"
                        @keyup.enter="submit"
                    >
                </div>

                <p class="msg error-msg" v-if="error">{{ error }}</p>
                <p class="msg success-msg" v-if="_success && !error">{{ _success }}</p>

                <button
                    class="submit-btn"
                    @click="submit"
                    :disabled="loading"
                >
                    <span v-if="loading" class="spinner">◌</span>
                    <span v-else>{{ mode === 'login' ? 'Войти' : 'Создать аккаунт' }}</span>
                </button>

            </div>
        </div>
    </div>
</template>

<style scoped>
    .auth-page {
        min-height: 100vh;
        background-color: #FEFAE0;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'MyFont', sans-serif;
    }

    .auth-card {
        width: 100%;
        max-width: 420px;
        background-color: #FAEDCD;
        border: 1px solid #D4A373;
        border-radius: 30px;
        padding: 44px 40px;
        margin: 20px;
    }

    /* Header */
    .auth-header {
        text-align: center;
        margin-bottom: 32px;
    }

    .auth-logo {
        font-size: 2.4rem;
        display: block;
        margin-bottom: 6px;
    }

    .auth-header h1 {
        font-weight: normal;
        font-size: 1.8rem;
        margin: 0;
        color: #000;
    }

    /* Tabs */
    .auth-tabs {
        display: flex;
        border-bottom: 1px solid #D4A373;
        margin-bottom: 28px;
    }

    .tab-btn {
        flex: 1;
        padding: 10px;
        background: none;
        border: none;
        font-family: 'MyFont', sans-serif;
        font-size: 1rem;
        cursor: pointer;
        color: #999;
        border-bottom: 2px solid transparent;
        margin-bottom: -1px;
        transition: color 0.2s, border-color 0.2s;
    }

    .tab-btn.active {
        color: #000;
        border-bottom-color: #D4A373;
    }

    /* Form */
    .auth-form {
        display: flex;
        flex-direction: column;
        gap: 16px;
    }

    .field {
        display: flex;
        flex-direction: column;
        gap: 5px;
    }

    .field label {
        font-size: 0.82rem;
        color: #666;
        letter-spacing: 0.02em;
    }

    .field input {
        padding: 11px 16px;
        font-family: 'MyFont', sans-serif;
        font-size: 1rem;
        border: 1px solid #D4A373;
        border-radius: 16px;
        background-color: #FEFAE0;
        color: #000;
        transition: border-color 0.2s, box-shadow 0.2s;
    }

    .field input:focus {
        outline: none;
        border-color: #b88b5a;
        box-shadow: 0 0 6px rgba(212, 163, 115, 0.45);
    }

    .field-hint {
        font-size: 0.78rem;
        color: #aaa;
        text-align: right;
        transition: color 0.2s;
    }

    .field-hint.ok {
        color: #6aab6a;
    }

    /* Messages */
    .msg {
        margin: 0;
        font-size: 0.88rem;
        text-align: center;
        padding: 8px 12px;
        border-radius: 12px;
    }

    .error-msg {
        color: #a33;
        background-color: rgba(180, 60, 60, 0.08);
    }

    .success-msg {
        color: #3a7a3a;
        background-color: rgba(60, 140, 60, 0.08);
    }

    /* Button */
    .submit-btn {
        padding: 13px;
        background-color: #CCD5AE;
        border: 1px solid #D4A373;
        border-radius: 40px;
        font-family: 'MyFont', sans-serif;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.2s, color 0.2s;
        margin-top: 4px;
    }

    .submit-btn:hover:not(:disabled) {
        background-color: #D4A373;
        color: white;
    }

    .submit-btn:disabled {
        opacity: 0.55;
        cursor: default;
    }

    .spinner {
        display: inline-block;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    @media (max-width: 480px) {
        .auth-card {
            padding: 28px 20px;
            border-radius: 20px;
        }
    }
</style>
