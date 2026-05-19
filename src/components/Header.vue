
<template>
    <header>
        <RouterLink to="/">Главная страница</RouterLink>
        <RouterLink to="/game">Игра про змею</RouterLink>
        <RouterLink to="/types_snake">Виды змей</RouterLink>
        <RouterLink to="/feedback">Обратная связь</RouterLink>
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