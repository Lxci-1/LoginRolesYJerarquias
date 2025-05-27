// main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// CSS básico para estilos
const app = createApp(App)

app.use(store)
app.use(router)

// Interceptor para añadir token a todas las requests
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'

axios.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 401 || error.response?.status === 403) {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      store.dispatch('logout')
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

app.mount('#app')