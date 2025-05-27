// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

// Importar componentes
import Login from '../components/Login.vue'
import Home from '../views/Home.vue'
import Admin from '../views/Admin.vue'
import UserProfile from '../views/User.vue'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { requiresGuest: true }
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true }
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  {
    path: '/profile',
    name: 'UserProfile',
    component: UserProfile,
    meta: { requiresAuth: true }
  },
  {
    path: '/usuario/:id',
    name: 'UserDetail',
    component: UserProfile,
    meta: { requiresAuth: true },
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Guards de navegación
router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated
  const isAdmin = store.getters.isAdmin
  
  // Si la ruta requiere estar deslogueado (como login)
  if (to.meta.requiresGuest && isAuthenticated) {
    next('/home')
    return
  }
  
  // Si la ruta requiere autenticación
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login')
    return
  }
  
  // Si la ruta requiere ser admin
  if (to.meta.requiresAdmin && !isAdmin) {
    next('/home')
    return
  }
  
  next()
})

export default router