import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Chapter from '../views/Chapter.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'COV',
    component: Home,
  },
  {
    path: '/FOR',
    name: 'FOR',
    component: Home,
  },
  {
    path: '/HIG',
    name: 'HIG',
    component: Home,
  },
  {
    path: '/:bookId/:chapterIdx?',
    name: 'Chapter',
    component: Chapter,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return { selector: to.hash };
    } else if (savedPosition) {
      return savedPosition;
    } else {
      return { x: 0, y: 0 };
    }
  },
});

export default router;
