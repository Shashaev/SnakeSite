
<script>
    let vueInstance = null;

    export default {
        data() {
            return {
                statusGame: 'GAME',
                isAuthenticated: (
                    document.cookie
                    .split(';')
                    .some(cookie => cookie.trim().startsWith('session_id='))
                ),
            }
        },
        mounted() {
            vueInstance = this;  // Crutch
            main();
        },
    }

    // Settings

    const width = 15;  // Change is not supported
    const height = 10;  // Change is not supported

    const timeOut = 300;  // Frame render -> timeOut -> Frame render ...

    let dx = 0;  // Initial movement
    let dy = 0;

    // Location functions: Down -> Up

    document.addEventListener('keydown', function(event) {
        if (['ArrowUp', 'ArrowDown', 'PageUp', 'PageDown'].includes(event.code)) {
            event.preventDefault();
        }
    });

    document.onkeydown = (enter) => {
        const key = enter.key
        // Very-hard level
        // if (key == 'd' || key == 'ArrowRight') dx = 1;
        // if (key == 'a' || key == 'ArrowLeft') dx = -1;
        // if (key == 'w' || key == 'ArrowUp') dy = -1;
        // if (key == 's' || key == 'ArrowDown') dy = 1;

        // Easy level
        if (key == 'd' || key == 'ArrowRight') { dy = 0;  dx = 1;  }
        if (key == 'a' || key == 'ArrowLeft')  { dy = 0;  dx = -1; }
        if (key == 'w' || key == 'ArrowUp')    { dy = -1; dx = 0;  }
        if (key == 's' || key == 'ArrowDown')  { dy = 1;  dx = 0;  }
    }

    function moveHead(positionHeadOld) {
        return [positionHeadOld[0] + dy, positionHeadOld[1] + dx];
    }

    let pole = [];  // To be filled in after. Initial pole = [
                    //                                          [0, ..., 0], 
                    //                                              ...,
                    //                                          [0, ..., 0],
                    //                                       ]
                    // Value in pole:
                    //   0 -> empty
                    //   1 -> body snake
                    //   2 -> head snake
                    //   3 -> cherry

    function checkDeadSnake(positionHead) {
        let y = positionHead[0];
        let x = positionHead[1];

        if (y === -1 || y === height || x === -1 || x === width) return true;
        if (dx === 0 && dy === 0) return false;

        return pole[y][x] === 1
    }

    function getCherry() {
        let count = 0;
        while (true) {
            let y = Math.trunc(Math.random() * height);
            let x = Math.trunc(Math.random() * width);
            if (y == height) y--;
            if (x == width) x--;

            if (pole[y][x] == 0) {
                return [y, x];
            }

            count++;

            if (count == 10 ** 8) {  // Crutch
                return false;
            }
        }
    }

    let snake = [];
    let positionCherry = [];

    function step() {
        pole[snake[snake.length - 1][0]][snake[snake.length - 1][1]] = 1;
        let newPositionHead = moveHead(snake[snake.length - 1]);

        if (checkDeadSnake(newPositionHead)) return 'LOSE';

        if ((newPositionHead[0] == positionCherry[0]) && (newPositionHead[1] == positionCherry[1])) {
            pole[positionCherry[0]][positionCherry[1]] = 2;
            positionCherry = getCherry();
            if (positionCherry) {
                pole[positionCherry[0]][positionCherry[1]] = 3;
            } else {
                return 'WIN';
            }
        } else {
            const removeEl = snake.shift();
            pole[removeEl[0]][removeEl[1]] = 0;
        }

        pole[newPositionHead[0]][newPositionHead[1]] = 2;
        snake.push(newPositionHead);
    }

    function pushScore(score) {
        const BASE = import.meta.env.VITE_API_BASE_URL;
        const formData = new FormData();
        formData.append('score', score);

        fetch(`${BASE}/v1/game/add`, {
            method: 'POST',
            credentials: 'include',
            body: formData
        }).catch(err => console.error('Ошибка при отправке счёта:', err));
    }

    let livePole = [];  // Precalculate
    for (let i = 0; i < height; i++) {
        livePole[i] = [];
        for (let j = 0; j < width; j++) {
            const idCell = `${i}_${j}`;
            livePole[i][j] = idCell;
            // livePole[i][j] = document.getElementById(idCell);
        }
    }

    let indToClassCell = ['base', 'snake', 'snake-head', 'cheery']

    function renderArrayElement(array) {
        for (let i = 0; i < height; i++) {
            for (let j = 0; j < width; j++) {
                const cell = document.getElementById(livePole[i][j]);
                let className = indToClassCell[array[i][j]];
                if (cell && cell.className !== className) cell.className = className;
            }
        }
    }

    function mainLoop() {
        const exit = step();
        if (exit) {
            vueInstance.statusGame = exit;
            if (vueInstance.isAuthenticated) pushScore(snake.length);
            snake = [];
            return;
        }

        renderArrayElement(pole);
        setTimeout(mainLoop, timeOut);
    }

    function createArrayInArray(width, height) {
        let array = [];
        for (let i = 0; i < height; i++) {
            array[i] = [];
            for (let j = 0; j < width; j++) {
                array[i][j] = 0;
            }
        }
        return array;
    }

    function main() {
        if (snake.length) return;
        vueInstance.statusGame = 'GAME';
        pole = createArrayInArray(width, height);
        snake = [[5, 7]];
        positionCherry = getCherry();
        pole[snake[0][0]][snake[0][1]] = 2;
        pole[positionCherry[0]][positionCherry[1]] = 3;
        dx = 0;
        dy = 0;
        mainLoop();
    }
    
    document.onclick = () => main();
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
                    <div class="game">
                        <div v-if="statusGame === 'WIN'">
                            <p>ТЫ ВЫГРАЛ!!!</p>
                            <p>ПОЗДРОВЛЯЮ!!!</p>
                            <br>
                            <div class=cheery></div>
                            <span>    </span>
                            <!-- <per>    </per> -->
                            <div class=snake></div>
                        </div>
                        <div v-if="statusGame === 'LOSE'">
                            <p>ТЫ ПРОИГРАЛ!</p>
                            <p>ТЕБЕ ПРОСТО НЕПОВЕЗЛО!!!</p>
                            <p>для продолжения нажми на экран</p>
                            <br>
                            <div class=cheery></div>
                            <span>    </span>
                            <!-- <per>    </per> -->
                            <div class=snake></div>
                        </div>
                        <div class="grid" v-if="statusGame === 'GAME'">
                            <div class="base" id="0_0"></div>
                            <div class="base" id="0_1"></div>
                            <div class="base" id="0_2"></div>
                            <div class="base" id="0_3"></div>
                            <div class="base" id="0_4"></div>
                            <div class="base" id="0_5"></div>
                            <div class="base" id="0_6"></div>
                            <div class="base" id="0_7"></div>
                            <div class="base" id="0_8"></div>
                            <div class="base" id="0_9"></div>
                            <div class="base" id="0_10"></div>
                            <div class="base" id="0_11"></div>
                            <div class="base" id="0_12"></div>
                            <div class="base" id="0_13"></div>
                            <div class="base" id="0_14"></div>
                            <br>
                            <div class="base" id="1_0"></div>
                            <div class="base" id="1_1"></div>
                            <div class="base" id="1_2"></div>
                            <div class="base" id="1_3"></div>
                            <div class="base" id="1_4"></div>
                            <div class="base" id="1_5"></div>
                            <div class="base" id="1_6"></div>
                            <div class="base" id="1_7"></div>
                            <div class="base" id="1_8"></div>
                            <div class="base" id="1_9"></div>
                            <div class="base" id="1_10"></div>
                            <div class="base" id="1_11"></div>
                            <div class="base" id="1_12"></div>
                            <div class="base" id="1_13"></div>
                            <div class="base" id="1_14"></div>
                            <br>
                            <div class="base" id="2_0"></div>
                            <div class="base" id="2_1"></div>
                            <div class="base" id="2_2"></div>
                            <div class="base" id="2_3"></div>
                            <div class="base" id="2_4"></div>
                            <div class="base" id="2_5"></div>
                            <div class="base" id="2_6"></div>
                            <div class="base" id="2_7"></div>
                            <div class="base" id="2_8"></div>
                            <div class="base" id="2_9"></div>
                            <div class="base" id="2_10"></div>
                            <div class="base" id="2_11"></div>
                            <div class="base" id="2_12"></div>
                            <div class="base" id="2_13"></div>
                            <div class="base" id="2_14"></div>
                            <br>
                            <div class="base" id="3_0"></div>
                            <div class="base" id="3_1"></div>
                            <div class="base" id="3_2"></div>
                            <div class="base" id="3_3"></div>
                            <div class="base" id="3_4"></div>
                            <div class="base" id="3_5"></div>
                            <div class="base" id="3_6"></div>
                            <div class="base" id="3_7"></div>
                            <div class="base" id="3_8"></div>
                            <div class="base" id="3_9"></div>
                            <div class="base" id="3_10"></div>
                            <div class="base" id="3_11"></div>
                            <div class="base" id="3_12"></div>
                            <div class="base" id="3_13"></div>
                            <div class="base" id="3_14"></div>
                            <br>
                            <div class="base" id="4_0"></div>
                            <div class="base" id="4_1"></div>
                            <div class="base" id="4_2"></div>
                            <div class="base" id="4_3"></div>
                            <div class="base" id="4_4"></div>
                            <div class="base" id="4_5"></div>
                            <div class="base" id="4_6"></div>
                            <div class="base" id="4_7"></div>
                            <div class="base" id="4_8"></div>
                            <div class="base" id="4_9"></div>
                            <div class="base" id="4_10"></div>
                            <div class="base" id="4_11"></div>
                            <div class="base" id="4_12"></div>
                            <div class="base" id="4_13"></div>
                            <div class="base" id="4_14"></div>
                            <br>
                            <div class="base" id="5_0"></div>
                            <div class="base" id="5_1"></div>
                            <div class="base" id="5_2"></div>
                            <div class="base" id="5_3"></div>
                            <div class="base" id="5_4"></div>
                            <div class="base" id="5_5"></div>
                            <div class="base" id="5_6"></div>
                            <div class="base" id="5_7"></div>
                            <div class="base" id="5_8"></div>
                            <div class="base" id="5_9"></div>
                            <div class="base" id="5_10"></div>
                            <div class="base" id="5_11"></div>
                            <div class="base" id="5_12"></div>
                            <div class="base" id="5_13"></div>
                            <div class="base" id="5_14"></div>
                            <br>
                            <div class="base" id="6_0"></div>
                            <div class="base" id="6_1"></div>
                            <div class="base" id="6_2"></div>
                            <div class="base" id="6_3"></div>
                            <div class="base" id="6_4"></div>
                            <div class="base" id="6_5"></div>
                            <div class="base" id="6_6"></div>
                            <div class="base" id="6_7"></div>
                            <div class="base" id="6_8"></div>
                            <div class="base" id="6_9"></div>
                            <div class="base" id="6_10"></div>
                            <div class="base" id="6_11"></div>
                            <div class="base" id="6_12"></div>
                            <div class="base" id="6_13"></div>
                            <div class="base" id="6_14"></div>
                            <br>
                            <div class="base" id="7_0"></div>
                            <div class="base" id="7_1"></div>
                            <div class="base" id="7_2"></div>
                            <div class="base" id="7_3"></div>
                            <div class="base" id="7_4"></div>
                            <div class="base" id="7_5"></div>
                            <div class="base" id="7_6"></div>
                            <div class="base" id="7_7"></div>
                            <div class="base" id="7_8"></div>
                            <div class="base" id="7_9"></div>
                            <div class="base" id="7_10"></div>
                            <div class="base" id="7_11"></div>
                            <div class="base" id="7_12"></div>
                            <div class="base" id="7_13"></div>
                            <div class="base" id="7_14"></div>
                            <br>
                            <div class="base" id="8_0"></div>
                            <div class="base" id="8_1"></div>
                            <div class="base" id="8_2"></div>
                            <div class="base" id="8_3"></div>
                            <div class="base" id="8_4"></div>
                            <div class="base" id="8_5"></div>
                            <div class="base" id="8_6"></div>
                            <div class="base" id="8_7"></div>
                            <div class="base" id="8_8"></div>
                            <div class="base" id="8_9"></div>
                            <div class="base" id="8_10"></div>
                            <div class="base" id="8_11"></div>
                            <div class="base" id="8_12"></div>
                            <div class="base" id="8_13"></div>
                            <div class="base" id="8_14"></div>
                            <br>
                            <div class="base" id="9_0"></div>
                            <div class="base" id="9_1"></div>
                            <div class="base" id="9_2"></div>
                            <div class="base" id="9_3"></div>
                            <div class="base" id="9_4"></div>
                            <div class="base" id="9_5"></div>
                            <div class="base" id="9_6"></div>
                            <div class="base" id="9_7"></div>
                            <div class="base" id="9_8"></div>
                            <div class="base" id="9_9"></div>
                            <div class="base" id="9_10"></div>
                            <div class="base" id="9_11"></div>
                            <div class="base" id="9_12"></div>
                            <div class="base" id="9_13"></div>
                            <div class="base" id="9_14"></div>
                            <br>
                        </div>
                    </div>  
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
