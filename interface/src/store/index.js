import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    title: 'Hello world title',
    data: 0,
  },
  getters: {
    data: state => state.data,
  },
  mutations: {
    SOCKET_NEW_BAND(state, data) {
      state.data = data
      document.getElementById('loading').style.display = 'block';
    },
    SOCKET_DATA(state, data){
      state.data = data
      document.getElementById('loading').style.display = 'none';
    }
  },

  modules: {}
})