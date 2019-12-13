<template>
  <!-- Hero -->
 <div>
  <Hero url="/signup/theme-choice/" />
  <ComoFunciona url="/signup/customize/"/>
  <Slider/>
  <RedesSociais/>
  <Estatisticas/>
  <Feedback/>
  <PerguntasFrequents/>
 </div>
</template>

<script>
import Hero from "./components/Hero.vue";
import ComoFunciona from './components/ComoFunciona.vue'
import Slider from './components/Slider.vue'
import RedesSociais from './components/RedesSociais.vue'
import Estatisticas from './components/Estatisticas.vue'
import Feedback from './components/Feedback.vue'
import PerguntasFrequents from './components/PerguntasFrequents.vue'
export default {
  name: "Home",
  props:['url'],
  components: {
    Hero,
    ComoFunciona,
    Slider,
    RedesSociais,
    Estatisticas,
    Feedback,
    PerguntasFrequents
  }
};
</script>

<style>

</style>