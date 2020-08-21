<template>
<v-app>
    <v-app-bar app color="info" dark>
        <v-container>
            <v-row>
                <v-col cols="2">
                    <v-img alt="Vuetify Logo" class="shrink mr-2 pt-4" contain src="./assets/logo.png" transition="scale-transition" width="50" />
                </v-col>
                  <v-spacer></v-spacer>
                <v-col>
                  
                    <v-img alt="Vuetify Name" class="shrink mt-1 hidden-sm-and-down drop " min-width="100" src="./assets/images/title.png" width="350" />
                </v-col>
                     <v-spacer></v-spacer>
                  <v-col cols="2">
                    <v-img alt="Vuetify Logo" class="shrink ml-16 pt-4" contain src="./assets/logo2.png" transition="scale-transition" width="50" />
                </v-col>
            </v-row>
        </v-container>
        <!-- <div class="d-flex align-center">
            <v-img alt="Vuetify Logo" class="shrink mr-2" contain src="./assets/logo.png" transition="scale-transition" width="40" />
            <v-spacer></v-spacer>
            <v-img alt="Vuetify Name" class="shrink mt-1 hidden-sm-and-down " contain min-width="100" src="./assets/images/title.png" width="250" />
        </div> -->

    </v-app-bar>
<v-container>
    <v-main>
        <HelloWorld />
    </v-main>
    </v-container>
</v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
    name: 'App',

    components: {
        HelloWorld,
    },

    data: () => ({
        //
    }),
};
</script>
<style lang="scss" scoped>
.drop {
    filter: drop-shadow(0 1px 3px rgba(0, 0, 0, 0.7));
}
</style>
