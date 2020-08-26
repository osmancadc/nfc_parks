import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    title: 'Hello world title',
    data: 0,
    newData: 0,
    newRead: 0
  },
  getters: {
    title: state => state.title,
    data: state => state.data,
    newData: state => state.newData,
    newRead: state => state.newRead

  },
  mutations: {
    SOCKET_NEW_CONNECTION(state, data) {
      state.data = data
      console.log(data.id)
    },

    SOCKET_NEW_DATA(state, newData) {
      state.newData = newData
      console.log(newData.id)
    },
    SOCKET_NEW_READ(state, newRead) {
      state.newRead = newRead
      console.log(newRead.money)
    },
  },

  modules: {}
})