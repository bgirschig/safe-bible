import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Chapter from '../views/Chapter.vue';
import Highlights from '../views/Highlights.vue';
import NotFound from '../views/NotFound.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: Home,
  },
  {
    path: '/index.html',
    component: Home,
  },
  {
    path: '/foreword',
    name: 'foreword',
    component: Home,
  },
  {
    path: '/highlights',
    name: 'highlights',
    component: Highlights,
  },
  { path: '/404', component: NotFound },  
  {
    path: '/:bookId/:chapterIdx?',
    name: 'Chapter',
    component: Chapter,
  },
  { path: '*', redirect: '/404' },
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

router.beforeEach((to, from, next) => {
  if (to.name === 'Chapter' && to.params.chapterIdx === undefined) {
    // ensure there is a chapter index for chapter routes
    return next(`/${to.params.bookId}/1`);
  }
  return next();
});

export default router;
