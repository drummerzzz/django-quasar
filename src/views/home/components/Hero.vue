<template>
      <div class="banner">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-10">
                    <div class="mb-3 d-block d-md-none">
                        <h2>As redes sociais do seu negócio com conteúdo diário.</h2>
                    </div>
                    <div class="row justify-content-center">
                        <div class="col-7 col-sm-7 col-md-8 col-lg-6">
                            <h2 class="d-none d-md-block">As redes sociais do seu negócio com conteúdo diário.</h2>
                            <p>Publique mais e cresça seu negócio.<br>
                                <strong>Por um preço incrivelmente baixo.</strong>
                            </p>
                            <div class="mt-1">
                                <!-- {% url 'signup:theme_choice' %} -->
                                <a :href="url" class="btn btn-primary">Ganhe uma publicação grátis!</a>
                            </div>
                            <div class="mt-1"><a :href="url" class="btn btn-light">Conheça nossos planos</a>
                            </div>
                        </div>
                        <div class="col-5 col-sm-5 col-md-4 col-lg-4 text-center">
                            <img src="static/images/Xiaomi.png" alt="">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Hero',
  props:['url']
}
</script>

<style>

</style>