import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import FeedbackView from '@/views/FeedbackView.vue'
import GameView from '@/views/GameView.vue'
import TypesSnakeView from '@/views/TypesSnakesView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
    },
    {
      path: '/feedback',
      name: 'feedback',
      component: FeedbackView,
    },
    {
      path: '/types_snake',
      name: 'types_snake',
      component: TypesSnakeView,
    },
    {
      path: '/game',
      name: 'game',
      component: GameView,
    },
  ],
})

export default router
