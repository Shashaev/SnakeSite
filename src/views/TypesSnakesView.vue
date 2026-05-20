
<script>
    export default {
        data() {
            return {
                count: 1,
                cards_all: [],
                cards: []
            }
        },
        methods: {
            async fetchNotes() {
                try {
                    const res = await fetch('/api/v1/note/get_all', { credentials: 'include' });
                    if (!res.ok) throw new Error();
                    const data = await res.json();
                    this.cards_all = data;
                    this.cards = data.length ? [data[0]] : [];
                    this.count = data.length ? 1 : 'max';
                } catch (err) {
                    console.error('API error:', err);
                }
            },
            add_count() {
                if (this.count === 'max' || this.count >= this.cards_all.length) {
                    this.count = 'max';
                    return;
                }
                this.count++;
                this.cards.push(this.cards_all[this.count - 1]);
            }
        },
        mounted() {
            this.fetchNotes();
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
