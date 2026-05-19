
<script>
export default {
    mounted() {
        const script = document.createElement('script');
        script.src = '/project2.js';
        document.body.appendChild(script);
    }
}
</script>

<template>
    <div class="content">
        <div class="main_info">
            <div class="text_info">
                <h1>
                    Самая популярная игра про змей!</h1>
                <p>
                    Игра представляет собой простой способ убить 
                    время и решить сложные задачи позиционирования с элементами решения лабиринтов
                </p>
                <RouterLink class="button_add" to="/types_snake">Больше!</RouterLink>
            </div>
            <div class="block_game">
                <div class="game_background">
                    <div class="game"></div>
                </div>
            </div>
        </div>
        <div class="attention_block">
            <img src="/image/70per.png" alt="70%">
            <div class="info_attention_block">
                <h2>
                    Далеко не все осилят это
                </h2>
                <p>Только 70% добираются до конца.</p>
            </div>
        </div>
    </div>
</template>

<style>
    .base {
        background-color: rgb(190, 177, 177);
        width: 5px;
        height: 5px;
        padding: 5px;
        margin: 0px;
        display:inline-block;
    }

    .snake {
        background-color: rgb(39, 249, 6);
        width: 5px;
        height: 5px;
        padding: 5px;
        margin: 0px;
        display:inline-block;
    }

    .snake-head {
        background-color: rgb(17, 168, 17);
        width: 5px;
        height: 5px;
        padding: 5px;
        margin: 0px;
        display:inline-block;
    }

    .cheery {
        background-color: rgb(242, 30, 30);
        width: 5px;
        height: 5px;
        padding: 5px;
        margin: 0px;
        display:inline-block;
    }
</style>
<style src="../assets/css/game.css" scoped></style>
