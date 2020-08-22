<template>
<v-container class="container-first">
    <h1 class="display-2 font-weight-bold   align-center text-center justify-center">
        Bienvenido
    </h1>
    <v-row class="text-center">

        <v-col class="mb-0 pa-0" cols="12">

            <v-row justify="center">
                <v-col cols="12" class="d-flex align-center text-center justify-center">
                    <v-img :src="require('../assets/images/screen.png')" class=" drop pa-0" contain height="340" />

                    <vue-typed-js  class="contenedor" :strings="['!Gracias por elegirnos¡', '¿En que te podemos ayudar?','¿Quieres saber tu saldo?', 'Acerca la manilla al validador','vuelve pronto']" :loop="true" :backSpeed="60" :typeSpeed="100" :startDelay="2000">
                        <h1>Hola <span class="typing "></span></h1>
                    </vue-typed-js>
                </v-col>
            </v-row>

            <v-col class="texto-label" cols="12">
                <h2 class="headline font-weight-bold mb-3 title-1">
                    id: {{data.id}}
                </h2>
                <h3 class="headline font-weight-bold mb-3 title-1">

                    Saldo: {{data.money}}
                </h3>
                <h4 class="headline font-weight-bold mb-3 title-1">
                    Pasaporte: {{data.passport}}
                </h4>
            </v-col>
        </v-col>
    </v-row>
</v-container>
</template>

<script>
import {
    mapGetters
} from 'vuex'
// import {mapActions} from 'vuex'

export default {
    name: 'HelloWorld',
    data: () => ({}),
    computed: {
        ...mapGetters([
            'title'
        ]),
        ...mapGetters([
            'data'
        ]),
    },
}
</script>

<style lang="scss" scoped>
.drop {
    filter: drop-shadow(7px 7px 7px rgba(0, 0, 0, 0.7));
}

.title-1 {
    background-color: rgb(144, 247, 247);
}

.contenedor {

    // top: 150px;
    // left: 350px;
    position: absolute !important;
    margin: auto;
    overflow: hidden;
    z-index: 9;
  font-size: 1rem!important;

}
@media (max-width: 600px){
  .contenedor {   font-size: .6rem!important;
}
}
@media (min-width: 600px) and (max-width: 800px){
  .contenedor {   font-size: .8rem!important;
}
}

.container-first {
    border: solid black 6px;
    padding-top: 0 !important;
    background-color: rgb(212, 233, 233);
}

.contenedor-title {
    // top: 67px;
    // left: 450px;
    position: absolute !important;
    margin: auto;
    overflow: hidden;
    z-index: 9;
  
}
</style>
