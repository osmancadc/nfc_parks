import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        data: {},
    },
    getters: {
        data: state => state.data,
    },
    mutations: {
        SOCKET_NEW_BAND(state, data) {
            state.data = data
            document.getElementById('loading').style.display = 'block';
            (new Vue()).$socket.emit('loading', { data })
        },
        SOCKET_DATA(state, data) {
            state.data = data
            document.getElementById('loading').style.display = 'none';
            setTimeout(() => {
                (new Vue()).$socket.emit('ready', {})
                state.data = {}
            }, 5000);
        }
    },
    actions: {
        socket_loading: (state, rootState) => {
            rootState.io.emit('loading', { "id": 123 });
        }
    },
    modules: {}
})