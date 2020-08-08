import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Chapter from '../views/Chapter.vue';
import Highlights from '../views/Highlights.vue';

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

router.beforeEach((to, from, next) => {
  if (to.name === 'Chapter' && to.params.chapterIdx === undefined) {
    // ensure there is a chapter index for chapter routes
    return next(`/${to.params.bookId}/1`);
  }
  return next();
});

export default router;
