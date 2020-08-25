<template>
<v-container class="container-first">
    <h1 class="display-2 font-weight-bold   align-center text-center justify-center title-welcome">
        Bienvenido
    </h1>
    <v-row class="text-center">
        <v-col class="mb-0 pa-0" cols="12">
            <div max-width="50vw">
                <v-row justify="center">
                    <v-col cols="12" class="d-flex align-center text-center justify-center">
                        <v-img :src="require('../assets/images/screen.png')" class=" drop pa-0" max-width="60vw" />
                        <vue-typed-js class="contenedor" :strings="['!Gracias por elegirnos¡', '¿En que te podemos ayudar?','¿Quieres saber tu saldo?', 'Acerca la manilla al validador','vuelve pronto']" :loop="true" :backSpeed="60" :typeSpeed="100" :startDelay="2000">
                            <h1>Hola <span class="typing "></span></h1>
                        </vue-typed-js>
                    </v-col>
                </v-row>
            </div>
        </v-col>
    </v-row>
    <v-row class="align-center text-center justify-center  container-ides  items-data ">
        <v-col class="texto-label title-container  " md="6" sm="12" xs="12">
            <h2 v-if="data.id < 0 " class="headline font-weight-bold mb-3 title-1 text-sm-left ">
                <span class="pr-2 title-information">Id: </span> {{data.id}}
            </h2>
            <h2 v-if="data.id > 0 " class="headline font-weight-bold mb-3 title-1 text-sm-left ">
                <span class="pr-2 title-information">Id: </span> {{newData.id}}
            </h2>
            <h3 v-if="data.money !== 0 " class="headline font-weight-bold mb-3 title-1 text-sm-left">
                <span class="pr-2 title-information"> Saldo: </span> ${{data.money}}
            </h3>
             <h3  v-if="data.money === 0"  class="headline font-weight-bold mb-3 title-1 text-sm-left">
                <span class="pr-2 title-information"> Saldo: </span> ${{newData.money}}
            </h3>
            <h4 class="headline font-weight-bold mb-3 title-1 text-sm-left">
                <span class="pr-2 title-information">Usuario:</span> {{data.passport}}
            </h4>
        </v-col>
    </v-row>
    <div class="text-center">
        <v-btn color="primary" dark @click.stop="dialog = false">
            Open Dialog
        </v-btn>
        <v-dialog v-model="dialog" max-width="290">
            <v-card>
                <v-card-title class="headline">New Read</v-card-title>
                <v-card-text>
                    ID: {{newRead.id}} <br>
                    SALDO: {{newRead.money}}
                </v-card-text>
                <v-card-text>

                </v-card-text>
                <h3 class="text-center">Loading...</h3>
                <div class="text-center">
                    <v-progress-circular :size="70" :width="7" color="info" indeterminate></v-progress-circular>
                </div>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="info" text @click="dialog = false">
                        salir
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</v-container>
</template>

<script>
import {
    mapGetters
} from 'vuex'
// import {mapActions} from 'vuex'

export default {
    name: 'HelloWorld',
    data: () => ({
        dialog: true,
    }),
    computed: {
        ...mapGetters([
            'title'
        ]),
        ...mapGetters([
            'data'
        ]),
        ...mapGetters([
            'newRead'
        ]),
        ...mapGetters([
            'newData'
        ]),
    },
}
</script>

<style lang="scss" scoped>
.drop {
    filter: drop-shadow(7px 7px 7px rgba(15, 11, 11, 0.3));
}

.title-1 {
    background-color: rgb(234, 234, 236);
}

.container-ides {
    max-width: 100vw !important;

}

.title-welcome {
    font-family: 'Roboto', sans-serif;
    color: rgb(149, 240, 240);
    text-shadow: 3px 1px rgba(0, 0, 0, 0.8);
    -webkit-text-stroke: 1px black;
    text-transform: uppercase;
}

.title-information {
    color: rgb(246, 250, 252);
    -webkit-text-stroke: 1px black;
    color: transparent;
}

.items-data {

    text-shadow: 1px 1px rgba(145, 140, 140, 0.4);
    color: rgb(65, 65, 65);
    font-size: 10px !important;
    text-align: justify;

}

.contenedor {
    position: absolute !important;
    margin: auto;
    overflow: hidden;
    z-index: 9;
    font-size: 1rem !important;
    color: #fff;
    text-shadow: 2px 4px rgba(0, 0, 0, 0.4);

}

@media (max-width: 600px) {
    .contenedor {
        font-size: .6rem !important;
    }

    .items-data h2,
    .items-data h3,
    .items-data h4 {
        font-size: 1rem !important;
    }
}

@media (min-width: 600px) and (max-width: 800px) {
    .contenedor {
        font-size: .8rem !important;
    }

    .drop {
        max-width: 90vw !important;
    }
}

@media (min-width: 800px) and (max-width: 1200px) {

    .drop {
        max-width: 90vw !important;
    }
}

@media (min-width: 300px) and (max-width: 600px) {
    .contenedor {
        font-size: .5rem !important;
    }

    .drop {
        max-width: 90vw !important;
    }

    .title-welcome {
        font-size: 2.3rem !important;
    }
}

@media (min-width: 900px) and (max-width:1400px) {
    .contenedor {
        font-size: 1.1rem !important;
    }
}

@media (min-width: 1500px) and (max-width:3000px) {
    .contenedor {
        font-size: 1.4rem !important;
    }
}

.container-first {
    border: solid black 6px;
    padding-top: 0 !important;
    background-color: rgb(233, 247, 247);
}

.contenedor-title {
    position: absolute !important;
    margin: auto;
    overflow: hidden;
    z-index: 9;
}
</style>
