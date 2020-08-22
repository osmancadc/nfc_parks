<template>
<v-container class="container-first">

    <v-row class="text-center">
        <v-col class="mb-0 pa-0">
            <v-col cols="12">

                <h1 class="display-2 font-weight-bold mb-1 contenedor-title ">
                    Bienvenido
                </h1>
                <vue-typed-js class="contenedor" :strings="['!Gracias por elegirnos¡', '¿En que te podemos ayudar?','¿Quieres saber tu saldo?', 'Acerca la manilla al validador','vuelve pronto']" :loop="true" :backSpeed="60" :typeSpeed="100" :startDelay="2000">
                    <h1>Hola <span class="typing "></span></h1>
                </vue-typed-js>
                <v-img :src="require('../assets/images/screen.png')" class=" drop pa-0" contain height="340" />
            </v-col>
            <v-col class="texto-label" cols="12">
                <h2 class="headline font-weight-bold mb-3 title-1">
                    id: {{state.data.id}}
                </h2>
                <h3 class="headline font-weight-bold mb-3 title-1">
                    
                    Saldo: {{state.data.money}}
                </h3>
                <h4 class="headline font-weight-bold mb-3 title-1">
                    Pasaporte: {{state.data.passport}}
                </h4>
            </v-col>
        </v-col>
    </v-row>
</v-container>
</template>

<script>
import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    data: {}
  },
  mutations: {
    SOCKET_NEW_CONNECTION  (state, data){
      this.state.data = data;
      console.log(this.state.data)
    }
  },
  actions: {
    
  },
  modules: {
  }
})

</script>

<style lang="scss" scoped>
.drop {
    filter: drop-shadow(7px 7px 7px rgba(0, 0, 0, 0.7));
}

.title-1 {
    background-color: rgb(144, 247, 247);
}

.contenedor {

    top: 150px;
    left: 350px;
    position: absolute !important;
    margin: auto;
    overflow: hidden;
    z-index: 9;

}

.container-first {
    border: solid black 6px;
    padding-top: 0 !important;
    background-color: rgb(212, 233, 233);
}

.contenedor-title {
    top: 67px;
    left: 450px;
    position: absolute !important;
    margin: auto;
    overflow: hidden;
    z-index: 9;
}
</style>
