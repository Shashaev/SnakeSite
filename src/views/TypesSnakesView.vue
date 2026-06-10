
<script>
    import { ref, onMounted } from 'vue'

    const isAuthenticated = ref(false)

    onMounted(() => {
        isAuthenticated.value = document.cookie
            .split(';')
            .some(cookie => cookie.trim().startsWith('session_id='))
    })

    export default {
        data() {
            return {
                BASE: import.meta.env.VITE_API_BASE_URL,
                numberNoteInPage: 5,
                page: 0,
                cards: [],
                newCard: {
                    title: '',
                    description: '',
                    file: null,
                },
                previewUrl: null,
                isAuthenticated: (
                    document.cookie
                    .split(';')
                    .some(cookie => cookie.trim().startsWith('session_id='))
                ),
            }
        },
        methods: {
            async fetchNotes() {
                try {
                    const res = await fetch(`${this.BASE}/v1/note/get_all`, { credentials: 'include' });
                    if (!res.ok) throw new Error();
                    this.cards = await res.json();
                } catch (err) {
                    console.error('API error:', err);
                }
            },
            nextPage() {
                window.scrollTo({ top: 0, behavior: 'smooth' });
                if ((this.page + 1) * this.numberNoteInPage >= this.cards.length) {
                    this.page = 0
                    return;
                }
                this.page++;
            },
            onFileChange(e) {
                const file = e.target.files[0];
                if (!file) return;
                this.newCard.file = file;
                this.previewUrl = URL.createObjectURL(file);
            },
            async submitCard() {
                if (!this.newCard.title.trim() || !this.newCard.file) return;
                try {
                    const formData = new FormData();
                    formData.append('title', this.newCard.title);
                    formData.append('description', this.newCard.description);
                    formData.append('image', this.newCard.file);

                    const res = await fetch(`${this.BASE}/v1/note/add`, {
                        method: 'POST',
                        credentials: 'include',
                        body: formData
                    });
                    if (!res.ok) throw new Error();

                    this.newCard = { title: '', description: '', file: null };
                    this.previewUrl = null;
                    await this.fetchNotes();
                } catch (err) {
                    console.error('Ошибка при добавлении:', err);
                }
            },
            async deleteCard(id_note) {
                try {
                    const formData = new FormData();
                    formData.append('id_note', id_note);

                    const res = await fetch(`${this.BASE}/v1/note/delete`, {
                        method: 'POST',
                        credentials: 'include',
                        body: formData
                    });
                    if (!res.ok) throw new Error();

                    await this.fetchNotes();
                } catch (err) {
                    console.error('Ошибка при добавлении:', err);
                }
            },
        },
        mounted() {
            this.fetchNotes();
        }
    }
</script>

<template>
    <div id="app" class="content">
        <div class="button_menu">
            <button
                class="main_button"
                :class="{'dis_btn': page==='max' }"
                @click="nextPage()">Следующая страница
            </button>
        </div>
        <div class="main_block">
            <div class="title">
                <h1>Виды змей и не только</h1>
            </div>
            <div class="cards">
                <div class="card" v-for="el in cards.slice(page * numberNoteInPage, (page + 1) * numberNoteInPage)" :key="el.id">
                    <img :src="`${BASE}${el.image}`" alt="type_snake">
                    <div class="title_card">
                        <h2>{{ el.title }}</h2>
                    </div>
                    <div class="text_card">
                        <p>{{ el.description }}</p>
                    </div>
                    <div v-if="el.is_user">
                        <button class="add-button" @click="deleteCard(el.id_model)">➖ Удалить карточку</button>
                    </div>
                </div>

                <div class="card card-form" v-if="isAuthenticated">
                    <img
                        v-if="previewUrl"
                        :src="previewUrl"
                        alt="preview"
                    >
                    <div v-else class="card-form__image">
                        <label for="file-input" style="cursor:pointer">
                            🐍 Нажмите чтобы выбрать изображение
                        </label>
                        <input
                            id="file-input"
                            type="file"
                            accept="image/*"
                            style="display:none"
                            @change="onFileChange"
                        >
                    </div>

                    <div class="title_card">
                        <input
                            class="title-input"
                            v-model="newCard.title"
                            type="text"
                            placeholder="Название новой карточки"
                        >
                    </div>

                    <div class="text_card">
                        <textarea
                            class="description-textarea"
                            v-model="newCard.description"
                            placeholder="Описание новой карточки"
                        ></textarea>
                    </div>

                    <button class="add-button" @click="submitCard">➕ Добавить карточку</button>
                </div>
                <div class="end">
                    <p>Страница: {{ page + 1 }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style src="../assets/css/list_type_snakes.css" scoped></style>
