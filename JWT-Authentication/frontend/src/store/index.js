import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    refresh:'',
    user_id:''
  },
  mutations: {
    login(state, {token, refresh}) {
      // console.log(token)
      // console.log(refresh)
      state.isAuthenticated = true
      state.token = token
      state.refresh = refresh
      localStorage.setItem("token", token)
      localStorage.setItem("refresh", refresh)
      axios.defaults.headers.common['Authorization'] = "Bearer " + token
    },
    logout(state) {
      state.isAuthenticated = false
      state.token = ''
      state.refresh = ''
      axios.defaults.headers.common['Authorization'] = ""
      localStorage.removeItem("token")
      localStorage.removeItem("refresh")
    },
  },
  actions: {
    onStart (context) {
      let token = localStorage.getItem("token")
      let refresh = localStorage.getItem("refresh")
      if (token) {
        axios.defaults.headers.common['Authorization'] = "Bearer " + token
        axios
          .get('/api/dj-rest-auth/user/')
          .then(response => {
            // console.log(response.data)
            // console.log(token)
            // console.log(refresh)
            this.state.user_id = response.data.pk
            context.commit('login', {token, refresh})
          })
          .catch(error => {
            if (refresh) {
              axios
              .post('/api/dj-rest-auth/token/refresh/', {refresh: refresh})
              .then(response => {
                // console.log(response.data)
                token = response.data.access_token   
                context.commit('login', {token, refresh})
              })
              .catch(error => {
                // console.log(error.data)
                context.commit('logout')
              })
            } else {
              context.commit('logout')
            }
          })
      } else {
        context.commit('logout')
      }
    }
  },
  modules: {
  }
})
