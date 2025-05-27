// store/index.js
import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    user: null,
    token: null,
    loading: false,
    error: null
  },
  
  mutations: {
    SET_USER(state, user) {
      state.user = user
    },
    SET_TOKEN(state, token) {
      state.token = token
    },
    SET_LOADING(state, loading) {
      state.loading = loading
    },
    SET_ERROR(state, error) {
      state.error = error
    },
    CLEAR_AUTH(state) {
      state.user = null
      state.token = null
    }
  },
  
  actions: {
    async login({ commit }, credentials) {
      try {
        commit('SET_LOADING', true)
        commit('SET_ERROR', null)
        
        const formData = new FormData()
        formData.append('username', credentials.correo)
        formData.append('password', credentials.contrasena)
        
        const response = await axios.post('/login', formData)
        
        const token = response.data.access_token
        
        // Decodificar el token para obtener los datos del usuario
        const payload = JSON.parse(atob(token.split('.')[1]))
        
        const user = {
          id: payload.id,
          nombre: payload.nombre,
          correo: payload.correo,
          rol: payload.rol
        }
        
        // Guardar en localStorage
        localStorage.setItem('token', token)
        localStorage.setItem('user', JSON.stringify(user))
        
        // Actualizar store
        commit('SET_TOKEN', token)
        commit('SET_USER', user)
        
        return { success: true }
      } catch (error) {
        const message = error.response?.data?.detail || 'Error de conexión'
        commit('SET_ERROR', message)
        return { success: false, message }
      } finally {
        commit('SET_LOADING', false)
      }
    },
    
    async register({ commit }, userData) {
      try {
        commit('SET_LOADING', true)
        commit('SET_ERROR', null)
        
        await axios.post('/registro', userData)
        return { success: true }
      } catch (error) {
        const message = error.response?.data?.detail || 'Error al registrar usuario'
        commit('SET_ERROR', message)
        return { success: false, message }
      } finally {
        commit('SET_LOADING', false)
      }
    },
    
    logout({ commit }) {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      commit('CLEAR_AUTH')
    },
    
    setUser({ commit }, user) {
      commit('SET_USER', user)
    },
    
    clearError({ commit }) {
      commit('SET_ERROR', null)
    }
  },
  
  getters: {
    isAuthenticated: state => !!state.user,
    currentUser: state => state.user,
    isAdmin: state => state.user?.rol === 'admin',
    isLoading: state => state.loading,
    error: state => state.error
  }
})