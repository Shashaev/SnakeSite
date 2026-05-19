
<script>
    export default {
        data() {
            return {
                count: 1,
                add_count() {
                    if ((this.count) >= this.cards_all.length || this.count === 'max') {
                        this.count = 'max'
                        return
                    }
                    this.count++
                    this.cards.push(this.cards_all[this.count - 1])
                },
                cards_all: [
                    {
                        title: 'Медянка',
                        description: (
                            'Змея с гладкой чешуей. Существуют разновидности ' +
                            'медянок с общими признаками. Названия видов змей связаны с ' +
                            'цветом руды. Предки верили, что укусившие людей медянки умрут ' + 
                            'к закату, когда земля окрашивается оттенками меди. Неядовитых ' +
                            'змей часто путают по внешнему виду с опасными гадюками.' +
                            'Важное отличие в форме зрачков. У медянок они круглые, у ' +
                            'гадюк — вертикальные. Окрас серо-коричневый, кроме фрагментов ' +
                            'медного окраса на голове.'
                        ),
                        image: 'image/медянка.jpg',
                    },
                    {
                        title: ' Обыкновенный уж',
                        description: `
                            Поселяется в местах, приближенных к воде, хорошо плавает, 
                            погружается под воду до 20 минут. По земле передвигается до 7 км/ч. 
                            Умеет лазать по деревьям. Длина тела 1-2 метра. 
                            По краям головы сзади часто хорошо различима пара 
                            желтовато-оранжевых пятен. Брюхо светловатое, с 
                            темными пятнами разной геометрии. Активность ужей проявляется в 
                            дневное время, ночью они скрываются в дуплах, лесной подстилке, 
                            норах грызунов.
                        `,
                        image: 'image/Уж обыкновенный.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                    {
                        title: 'Lorem ipsum',
                        description: `
                            Lorem ipsum dolor sit amet.
                        `,
                        image: 'image/kotik.jpg',
                    },
                ],
                cards: [
                    {
                        title: 'Медянка',
                        description: (
                            'Змея с гладкой чешуей. Существуют разновидности ' +
                            'медянок с общими признаками. Названия видов змей связаны с ' +
                            'цветом руды. Предки верили, что укусившие людей медянки умрут ' + 
                            'к закату, когда земля окрашивается оттенками меди. Неядовитых ' +
                            'змей часто путают по внешнему виду с опасными гадюками.' +
                            'Важное отличие в форме зрачков. У медянок они круглые, у ' +
                            'гадюк — вертикальные. Окрас серо-коричневый, кроме фрагментов ' +
                            'медного окраса на голове.'
                        ),
                        image: 'image/медянка.jpg',
                    },
                ]
            }
        }
    }
</script>

<template>
    <div id="app" class="content">
        <div class="button_menu">
            <button class="main_button" :class="{'dis_btn': count==='max' }" @click="add_count()">{{ count }}</button>
        </div>
        <div class="main_block">
            <div class="title">
                <h1>Виды змей и не только </h1>
            </div>
            <div class="cards">
                <div class="card" v-for="el in cards">
                    <img :src=el.image alt="type_snake">
                    <div class="title_card">
                        <h2>{{ el.title }}</h2>
                    </div>
                    <div class="text_card">
                        <p>
                            {{ el.description }}
                        </p>
                    </div>
                </div>
                <div class="end" v-if="count === 'max'">
                    <p>Больше элементов нет, скоро будут обновления!</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style src="../assets/css/list_type_snakes.css" scoped></style>
