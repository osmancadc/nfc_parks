import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    title: 'Hello world title',
    data: 0
  },
  getters:{
    title: state => state.title,
    data: state=> state.data
   
  },
  mutations: {
    SOCKET_NEW_CONNECTION  (state, data){
      state.data = data
      console.log(data.id)
    }
  },

  modules: {
  }
})
