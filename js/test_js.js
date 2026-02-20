
console.log(10 + 1)
console.log(10 ** 500)
console.log('a' + 'b')
console.log("a" + 'o' * 100)
console.log("a" + "b" * 10)
console.log('a' + 10)


function log(a, b) {
    const c = a + b
    console.log(c)
}

log(10, 5)
log('f', 1.1)
log('fasdf ')
const a = 10
// a = 20

const randomObject = {
    'a': 100,
    'b': 200,
}

console.log(randomObject)
// console.log(random_value)
let aaa
console.log(aaa)
console.log(undefined)
console.dir(undefined)
console.table(undefined)
console.dir(randomObject)
console.table(randomObject)

// const random_value2

var random_value3
console.log(random_value3)
// len random_value3
// console.log(random_value3)
var random_value3 = 10
console.log(random_value3)

const random_value4 = 10
console.log(random_value3)
// var random_value4 = 20

console.log(randomObject['a'])
randomObject['a'] = 'alksjdflkjskdlf'
console.log(randomObject['a'])
const randomObject2 = randomObject
console.log(randomObject2['a'])
randomObject2['a'] = '111111111111'
console.log(randomObject2['a'])
console.log(randomObject['a'])

randomObject['a'] = randomObject
console.log(randomObject['a'])
console.log(
    randomObject['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
    ['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']['a']
)
console.log(randomObject.b)
randomObject.b = 1000
console.log(randomObject.b)
// randomObject.'a' = 10

const number = 20
const bool = true
const string = 'string value'
const undefined_value = undefined
const null_value = null
const link_to_object = {}


function logType(a) {
    console.log(typeof(a))
}

console.log('Основные простоые типы JS')
logType(number)
logType(bool)
logType(string)
logType(undefined_value)
logType(null_value)
logType(link_to_object)

console.table(null_value)
console.dir(null_value)

const logHelloWorld = () => {
    console.log('Hello World!')
}

logHelloWorld()

// logHelloWorld = 10

logHelloWorld.a = 100
console.log(logHelloWorld.a)

console.log(logHelloWorld)
console.log(log)

console.dir(log)
console.dir(logHelloWorld)

console.table(log)
console.table(logHelloWorld)

log.name = 'log_change'
log(1, 1)
// log_change(1, 1)
log.a = 100
console.dir(log)

const infinityFun = () => {
    infinityFun.a += 1
    console.log(infinityFun.a)
    return infinityFun
}

infinityFun.a = 0
infinityFun()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()

// let random_value5 = ++1
// console.log(random_value5)

let random_value5 = -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+1
console.log(random_value5)

random_value5 = +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-1
console.log(random_value5)

console.log(randomObject.asdf)
// console.log(randomObject[asdf])

const list_number = [1, 2, 3, 4]

const view = (c) => {
    console.log(c)
    console.dir(c)
    console.table(c)
}

view(list_number)

const LEN_LIST = 20
const MAX_RANDOM = 1000
while (list_number.length < LEN_LIST) {
    list_number.push(Math.floor(Math.random() * MAX_RANDOM ))
}

console.log(list_number)
for (let i = 0; i < list_number.length; i++) {
    console.log(list_number[i]);
}

console.log('For in ')
for (const el in list_number) {
    console.log(el)
}

for (const el in list_number) {
    console.log(list_number[el])
}

console.log('For of')
for (const el of list_number) {
    console.log(el)
}

console.log('Foreach')
list_number.forEach(el => console.log(el))

console.log('map')
const new_list_nubmer = list_number.map(el => el ** (1.5))
new_list_nubmer.forEach(el => console.log(el))

console.log('good')


console.log(10 in list_number)


const find_or_add = (arr, el) => {
    if (el in arr) {
        return true
    }

    arr.push(el)
    return false
}


console.log(find_or_add(list_number, 10))
console.log('Длина списка - ', list_number.length)
console.log(find_or_add(list_number, 123.124))
console.log('Длина списка - ', list_number.length)

randomObject.c = null
view(randomObject)

const log_property = (obj, key) => {
    console.log(obj[key])
    alert(obj[key])
}

// while (true) {
//     console.log('Введите название свойства для проверки')
//     const key = prompt()
//     if (key in randomObject) {
//         log_property(randomObject, key)
//     } else {
//         alert('Такого поля нет')
//     }
// }

console.log(mainP.innerText)

mainP.after(mainP.cloneNode(true))

const divMainElement = document.querySelector('.main')
const formElement = document.createElement('form')
const labelElement = document.createElement('input')
const buttonElement = document.createElement('button')

buttonElement.innerText = 'Нажми для отправки'
formElement.append(labelElement)
formElement.append(buttonElement)
divMainElement.appendChild(formElement)


labelElement.style.height = '40px'

buttonElement.style.height = '40px'

formElement.style.display = 'flex'
formElement.style.flexDirection = 'column'
formElement.style.justifyContent = 'center'
formElement.style.alignItems = 'center'
formElement.style.gap = '10px'
formElement.style.width = '400px'
formElement.style.height = '400px'
formElement.style.backgroundColor = '#FAEDCD'
formElement.style.borderRadius = '20px'

divMainElement.style.display = 'flex'
divMainElement.style.flexDirection = 'column'
divMainElement.style.justifyContent = 'center'
divMainElement.style.alignItems = 'center'
divMainElement.style.width = '100%';
divMainElement.style.margin = '0';
divMainElement.style.padding = '20px';

document.body.style.overflowX = 'hidden';
// document.body.style.overflowY = 'hidden';

buttonElement.onclick = (event) => {
    event.preventDefault();
    if (isNaN(labelElement.value))
        alert('Не правильный формат ввода (можно только число).')
    else
        alert('Проверка пройдена')
}

const newButtonElement = document.createElement('button')
newButtonElement.innerText = 'Изменить сосотояние формы'
newButtonElement.style.height = '40px'
newButtonElement.style.marginTop = '50px'

divMainElement.append(newButtonElement)

const styleDisplayNext = {
    'none': 'flex',
    'flex': 'none',
}
newButtonElement.onclick = (event) => {
    event.preventDefault()
    formElement.style.display = styleDisplayNext[formElement.style.display];
}

const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://swapi.info/api/people', true);
xhr.onload = function() {
    const data = JSON.parse(this.response);
    
    const container = document.createElement('div');
    container.style.display = 'flex';
    container.style.flexWrap = 'wrap';
    container.style.gap = '20px';
    container.style.justifyContent = 'center';
    
    data.forEach(person => {
    const card = document.createElement('div');
    card.style.width = '300px';
    card.style.padding = '20px';
    card.style.backgroundColor = '#FEFAE0';
    card.style.borderRadius = '20px';
    card.style.boxSizing = 'border-box';
    
    card.innerHTML = `
        <h3>${person.name}</h3>
        <p><strong>Height:</strong> ${person.height}</p>
        <p><strong>Mass:</strong> ${person.mass}</p>
    `;
    
    container.appendChild(card);
    });
    
    divMainElement.appendChild(container);
    
    window.scrollTo(0, 0);
};
  
xhr.send();

const postData = {
    title: 'foo',
    body: 'bar',
    userId: 1
  };

fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    body: JSON.stringify(postData)
  })
    .then((res) => res.json())
    .then((json) => {
      console.log('Ответ сервера:', json)   
      alert(`ID созданного объекта = ${json.id}`)
    })
    .catch((error) => console.error('Ошибка:', error))
