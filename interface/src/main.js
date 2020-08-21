import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "@babel/polyfill";
import "roboto-fontface/css/roboto/roboto-fontface.css";
import "@mdi/font/css/materialdesignicons.css";
import VueTypedJs from "vue-typed-js";
import VueSocketio from "vue-socket.io";

// Vue.use(VueSocketio, "http://192.168.1.18:4567");
Vue.use(VueTypedJs);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
