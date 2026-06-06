<script>
    export default {
        data() {
            return {
                BASE: import.meta.env.VITE_API_BASE_URL,
                leaderboard: [],
            }
        },
        methods: {
            async getLeaderboard() {
                try {
                    const res = await fetch(
                        `${this.BASE}/v1/game/leaderboard`,
                        { credentials: 'include' },
                    );
                    if (!res.ok) throw new Error();
                    this.leaderboard = await res.json();
                } catch (err) {
                    console.error('API error:', err);
                }
            }
        },
        mounted() {
            this.getLeaderboard();
        },
    }
</script>

<template>
    <div class="content">
        <div class="main_block">
            <div class="title">
                <h1>Таблица лидеров</h1>
            </div>
            <div class="leaderboard">
                <div class="leaderboard-header">
                    <span class="col-rank">#</span>
                    <span class="col-name">Игрок</span>
                    <span class="col-score">Очки</span>
                </div>
                <div
                    class="leaderboard-row"
                    v-for="(line, index) in leaderboard"
                    :key="index"
                    :class="{
                        'rank-gold': index === 0,
                        'rank-silver': index === 1,
                        'rank-bronze': index === 2,
                    }"
                >
                    <span class="col-rank">{{ index + 1 }}</span>
                    <span class="col-name">{{ line.username }}</span>
                    <span class="col-score">{{ line.maxscore }}</span>
                </div>
                <div class="leaderboard-empty" v-if="leaderboard.length === 0">
                    <p>Пока никто не играл...</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .content {
        display: flex;
        justify-content: center;
        background-color: #FEFAE0;
        min-height: 100vh;
    }

    .main_block {
        width: 85vw;
        max-width: 700px;
        padding-top: 40px;
    }

    .title {
        height: 120px;
        background-color: #FAEDCD;
        border: 1px solid #D4A373;
        border-bottom-left-radius: 25px;
        border-bottom-right-radius: 25px;
        margin-top: 100px;
        margin-bottom: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    h1 {
        font-weight: normal;
    }

    .leaderboard {
        background-color: #CCD5AE;
        border-radius: 30px;
        overflow: hidden;
        margin-bottom: 100px;
    }

    .leaderboard-header {
        display: grid;
        grid-template-columns: 60px 1fr 120px;
        padding: 16px 24px;
        background-color: #D4A373;
        color: #fff;
        font-size: 0.95rem;
    }

    .leaderboard-row {
        display: grid;
        grid-template-columns: 60px 1fr 120px;
        padding: 14px 24px;
        border-bottom: 1px solid #b8c28a;
        background-color: #CCD5AE;
        transition: background-color 0.2s;
    }

    .leaderboard-row:last-child {
        border-bottom: none;
    }

    .rank-gold {
        background-color: #f5e6c0;
    }

    .rank-silver {
        background-color: #dde0d8;
    }

    .rank-bronze {
        background-color: #e8cdb0;
    }

    .col-rank {
        font-weight: 500;
        color: #5a4a2a;
    }

    .col-name {
        color: #3a3020;
    }

    .col-score {
        text-align: right;
        font-weight: 500;
        color: #5a4a2a;
    }

    .leaderboard-empty {
        padding: 40px;
        text-align: center;
        color: #7a6a4a;
    }
</style>
