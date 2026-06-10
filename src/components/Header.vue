
<script>
    export default {
        data() {
            return {
                isAuthenticated: (
                    document.cookie
                    .split(';')
                    .some(cookie => cookie.trim().startsWith('session_id='))
                ),
            }
        },
    }
</script>

<template>
    <header>
        <RouterLink to="/">Главная страница</RouterLink>
        <RouterLink to="/game">Игра про змею</RouterLink>
        <RouterLink to="/leaderboard">Лидерборд</RouterLink>
        <RouterLink to="/types_snake">Виды змей</RouterLink>
        <RouterLink to="/auth" v-if="!isAuthenticated">Авторизация</RouterLink>
    </header>
</template>

<style scoped>
    header {
        width: 100%;
        margin: 0px;
        height: 60px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        background-color: #141A20;
        border-bottom-left-radius: 50px;
        border-bottom-right-radius: 50px;
        position: fixed;
        z-index: 1000;
    }

    a {
        color: #FEFAE0;
        text-decoration: none;
        padding: 15px 18px;
        border-radius: 20px;
        transition: background-color 0.2s;
    }

    a:hover {
        background-color: #2a3540;
    }

    a.router-link-active {
        background-color: #D4A373;
        color: #141A20;
    }
</style>
