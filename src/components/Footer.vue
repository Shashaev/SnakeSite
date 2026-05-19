
<template>
    <div class="footer">
        <div class="about_company">©️ 2025 Discourse Inc: все права защищены</div>
        <div class="links_site">
            <p>Ссылки:</p>
            <RouterLink to="/">Главная страница</RouterLink>
            <br>
            <RouterLink to="/game">Игра про змею</RouterLink>
            <br>
            <RouterLink to="/types_snake">Виды змей</RouterLink>
            <br>
            <RouterLink to="/feedback">Обратная связь</RouterLink>
        </div>
        <div class="contacts">
            <p>Контакты:</p>
            <a href="tel:+79290431468">+7 929 043 14 68</a>
            <br>
            <a href="mailto:shashaevkirill@gmai&body=привет?subject=вопрос">Напишите нам</a>
        </div>
    </div>
</template>

<style scoped>
    .footer {
        margin: 0px;
        padding-top: 50px;
        padding-left: 50px;
        background-color: #141A20;
        font-size: 16px;
        display: flex;
        height: 200px;
        color: aliceblue;
        justify-content:space-around;
    }
</style>
