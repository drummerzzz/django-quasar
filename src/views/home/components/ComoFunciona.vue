<template >
  <div class="w1 section">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-7 col-lg-6 col-xl-6">
          <h5>Como funciona?</h5>
          <div class="row icon-section">
            <div class="col-4">
              <img src="/static/images/icon-1.jpg" alt />
              <p>Selecione sua área</p>
            </div>
            <div class="col-4">
              <img src="/static/images/icon-2.jpg" alt />
              <p>Personalize</p>
            </div>
            <div class="col-4">
              <img src="/static/images/icon-3.jpg" alt />
              <p>Publique em suas redes sociais</p>
            </div>
          </div>
          <div class="mt-5 mb-4">
            <div class="embed-responsive embed-responsive-16by9">
              <iframe
                width="560"
                height="315"
                src="https://www.youtube.com/embed/6i-ASaK9_HU"
                frameborder="0"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
              ></iframe>
            </div>
          </div>
          <h2>
            Escolha o melhor
            <br />plano para você.
          </h2>
          <a v-bind:href="url" class="btn btn-secondary">
            <span>Veja nossos planos</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script >


export default { 
  props: ['url'],
  name: "ComoFunciona"
};
</script>

