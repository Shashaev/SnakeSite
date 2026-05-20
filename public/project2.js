
document.addEventListener('keydown', function(event) {
    if (['ArrowUp', 'ArrowDown', 'PageUp', 'PageDown'].includes(event.code)) {
      event.preventDefault();
    }
  });


const width = 15
const height = 10

let pole = []
let snake = []
let positionCherry = []
const timeOut = 300

let changePosition = null

function main () {
    pole = createArrayInArray(width, height)
    snake = [[5, 5]]
    positionCherry = [0, 0]
    pole[5][5] = 2
    pole[0][0] = 3
    changePosition = null
    mainLoop()
}

main()

document.onclick = () => main()

document.onkeydown = (enter) => {
    const key = enter.key
    if (key == 'd' || key == 'ArrowRight') changePosition = 0
    if (key == 'a' || key == 'ArrowLeft') changePosition = 1
    if (key == 'w' || key == 'ArrowUp') changePosition = 2
    if (key == 's' || key == 'ArrowDown') changePosition = 3
}

function createArrayInArray (width, height) {
    array = []
    for (let i = 0; i < height; i++) {
        array[i] = []
        for (let j = 0; j < width; j++) {
            array[i][j] = 0
        }
    }
    return array
}

function getCherry () {
    let count = 0
    while (true) {
        y = Math.trunc(Math.random() * height)
        x = Math.trunc(Math.random() * width)
        if (y == height) y--
        if (x == width) x--
        
        if (pole[y][x] == 0) {
            position = [y, x]
            return position
        }

        count++

        if (count == 10 ** 8) {
            return false
        }
    }
}

function moveHead (positionHeadOld) {
    if (changePosition == null) {
        return [positionHeadOld[0], positionHeadOld[1]]
    }
    
    switch (changePosition) {
        case 0:
            return [positionHeadOld[0], positionHeadOld[1] + 1]
        case 1:
            return [positionHeadOld[0], positionHeadOld[1] - 1]
        case 2:
            return [positionHeadOld[0] - 1, positionHeadOld[1]]
        case 3:
            return [positionHeadOld[0] + 1, positionHeadOld[1]]
    }
}

function checkDeadSnake(positionHead) {
    let y = positionHead[0]
    let x = positionHead[1]
    
    if (y == height || x == width) {
        return true
    }

    if (y == -1 || x == -1) {
        return true
    }

    if (changePosition != null) {
        if (pole[y][x] == 1) {
            return true
        }
    }

    return false
}

function renderArrayElement (array) {
    let res = ''
    for (let els of array) {
        for (let el of els) {
            if (el == 0) res += '<div class="base"></div>'
            if (el == 1) res += '<div class="snake"></div>'
            if (el == 2) res += '<div class="snake-head"></div>'
            if (el == 3) res += '<div class="cheery"></div>'
            res += ' '
        }
        res += '<br>'
    }
    return res
}

function stap () {
    pole[snake[snake.length - 1][0]][snake[snake.length - 1][1]] = 1
    newPositionHead = moveHead(snake[snake.length - 1])

    if (checkDeadSnake(newPositionHead)) {
        return 'LOSE'
    }

    if ((newPositionHead[0] == positionCherry[0]) && (newPositionHead[1] == positionCherry[1])) {
        pole[positionCherry[0]][positionCherry[1]] = 0
        positionCherry = getCherry()
        if (positionCherry) {
            pole[positionCherry[0]][positionCherry[1]] = 3
        } else {
            return 'WIN'
        }
    } else {
        const removeEl = snake.shift()
        pole[removeEl[0]][removeEl[1]] = 0
    }

    pole[newPositionHead[0]][newPositionHead[1]] = 2
    snake.push(newPositionHead)
}

function mainLoop () {
    const exit = stap()
    const game_pol = document.body.getElementsByClassName('game')[0]

    if (exit) {
        if (exit == 'WIN') game_pol.innerHTML = rendersWindowWin
        else game_pol.innerHTML = rendersWindowLose
        return
    }

    const rendersPole = renderArrayElement(pole)
    game_pol.innerHTML = rendersPole

    setTimeout(mainLoop, timeOut)
}

const rendersWindowWin = `
<p>ТЫ ВЫГРАЛ!!!</p>
<p>ПОЗДРОВЛЯЮ!!!</p>
<br>
<div class=cheery></div><per>    </per><div class=snake></div>
`

const rendersWindowLose = `
<p>ТЫ ПРОИГРАЛ!</p>
<p>ТЕБЕ ПРОСТО НЕПОВЕЗЛО!!!</p>
<p>для продолжения нажми на экран</p>
<br>
<div class=cheery></div><per>    </per><div class=snake></div>
`
