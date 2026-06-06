
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
    }
</style>