<template>
  <div class="hello">
    <b-menu>
      <b-menu-list label="Menu">
        <b-menu-item icon="information-outline" label="Info"></b-menu-item>
        <b-menu-item
          icon="settings"
          :active="isActive"
          :expanded="isActive"
          @click="isActive = !isActive"
        >
          <template slot="label" slot-scope="props">
            Administrator
            <b-icon class="is-pulled-right" :icon="props.expanded ? 'menu-down' : 'menu-up'"></b-icon>
          </template>
          <b-menu-item icon="account" label="Users"></b-menu-item>
          <b-menu-item icon="cellphone-link">
            <template slot="label" slot-scope="props">
              Devices
              <b-dropdown aria-role="list" class="is-pulled-right" position="is-bottom-left">
                <b-icon icon="dots-vertical" slot="trigger"></b-icon>
                <b-dropdown-item aria-role="listitem">Action</b-dropdown-item>
                <b-dropdown-item aria-role="listitem">Another action</b-dropdown-item>
                <b-dropdown-item aria-role="listitem">Something else</b-dropdown-item>
              </b-dropdown>
            </template>
          </b-menu-item>
          <b-menu-item icon="cash-multiple" label="Payments" disabled></b-menu-item>
        </b-menu-item>
        <b-menu-item icon="account" label="My Account">
          <b-menu-item label="Account data"></b-menu-item>
          <b-menu-item label="Addresses"></b-menu-item>
        </b-menu-item>
      </b-menu-list>
      <b-menu-list>
        <b-menu-item label="Expo" icon="link" tag="router-link" target="_blank" to="/expo"></b-menu-item>
      </b-menu-list>
      <b-menu-list label="Actions">
        <b-menu-item label="Logout"></b-menu-item>
      </b-menu-list>
    </b-menu>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Primary title</h1>
          <h2 class="subtitle">Primary subtitle</h2>
        </div>
      </div>
    </section>
    <img src="@/assets/logo-vue.png" />
    <p>
      For guide and recipes on how to configure / customize this project,
      <br />check out the
      <a
        href="https://cli.vuejs.org"
        target="_blank"
        rel="noopener"
      >vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li>
        <a
          href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel"
          target="_blank"
          rel="noopener"
        >babel</a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint"
          target="_blank"
          rel="noopener"
        >eslint</a>
      </li>
    </ul>
    <h3>Essential Links</h3>
    <ul>
      <li>
        <a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a>
      </li>
      <li>
        <a href="https://forum.vuejs.org" target="_blank" rel="noopener">Forum</a>
      </li>
      <li>
        <a href="https://chat.vuejs.org" target="_blank" rel="noopener">Community Chat</a>
      </li>
      <li>
        <a href="https://twitter.com/vuejs" target="_blank" rel="noopener">Twitter</a>
      </li>
      <li>
        <a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a>
      </li>
    </ul>
    <h3>Ecosystem</h3>
    <ul>
      <li>
        <a href="https://router.vuejs.org" target="_blank" rel="noopener">vue-router</a>
      </li>
      <li>
        <a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/vue-devtools#vue-devtools"
          target="_blank"
          rel="noopener"
        >vue-devtools</a>
      </li>
      <li>
        <a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener">vue-loader</a>
      </li>
      <li>
        <a href="https://github.com/vuejs/awesome-vue" target="_blank" rel="noopener">awesome-vue</a>
      </li>
    </ul>
     <b-steps>
        <b-step-item label="Account" icon="account-key"></b-step-item>
        <b-step-item label="Profile" icon="account"></b-step-item>
        <b-step-item label="Social" icon="account-plus"></b-step-item>
        <b-step-item label="Usuario" pack="fas" icon="user"></b-step-item>
    </b-steps>
  </div>
</template>

<script>
export default {
  name: "VueDemo",
  props: {},
  data() {
    return {
      isActive: true
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

img {
  width: 250px;
}
</style>

<script>
export default {
  data() {
    return {
      isActive: true
    };
  }
};
</script>