<template>
  <div class="Profile">
    <h1>Profile</h1>
    <div class="alert alert-success">Hello {{username}}, I can identify YOU!</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Profile',
  data() {
    return {
      username: ''
    }
  },
  mounted() {
    // console.log($store.state.refresh)
    axios
      .get('/api/dj-rest-auth/user/')
      .then(response => {
        this.username = response.data.username
      })
      .catch(error => {
        let refresh = this.$store.state.refresh
        axios
        .post('/api/dj-rest-auth/token/refresh/', {refresh: refresh})
        .then(response => {
          let token = response.data.access_token   
          context.commit('login', {token, refresh})
        })
        .catch(error => {
          context.commit('logout')
          this.$router.push("/login")
        console.log(error.response.data)
        })
        // this.$store.commit("logout")
        console.log(error.response.data)
      })
  }
}
</script>