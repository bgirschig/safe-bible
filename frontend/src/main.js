import Vue from 'vue';
import VueMatomo from 'vue-matomo';
import App from './App.vue';
import router from './router';
import matomoConfig from './matomoConfig';

matomoConfig.router = router;
Vue.use(VueMatomo, matomoConfig);

Vue.directive('visible', (el, binding) => {
  el.style.visibility = binding.value ? 'visible' : 'hidden'; // eslint-disable-line no-param-reassign
});
Vue.prototype.$window = window;

Vue.config.productionTip = false;

// Report errors
const reportError = (err) => window._paq.push(['trackEvent', 'JS Error', err]);
Vue.config.errorHandler = (err) => {
  reportError(err.message);
  console.error(err);
};
window.onerror = (message) => {
  reportError(message);
  return false;
};

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
