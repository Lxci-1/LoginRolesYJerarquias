<!-- views/User.vue -->
<template>
  <div class="user-profile-container">
    <div class="profile-header">
      <h1>{{ isOwnProfile ? 'Mi Perfil' : 'Perfil de Usuario' }}</h1>
      <p>Información personal del usuario</p>
    </div>

    <div v-if="loading" class="loading-section">
      <div class="spinner"></div>
      <p>Cargando información del usuario...</p>
    </div>

    <div v-if="error" class="alert alert-error">
      {{ error }}
    </div>

    <div v-if="usuario && !loading" class="profile-content">
      <div class="profile-card">
        <div class="profile-avatar">
          <div class="avatar-large">
            {{ usuario.nombre.charAt(0).toUpperCase() }}
          </div>
          <div class="avatar-status" :class="statusClass">
            {{ usuario.rol === 'admin' ? 'Administrador' : 'Usuario' }}
          </div>
        </div>

        <div class="profile-info">
          <h2>{{ usuario.nombre }}</h2>
          <p class="user-email">{{ usuario.correo }}</p>

          <div class="info-grid">
            <div class="info-item">
              <label>ID de Usuario:</label>
              <span>{{ usuario.id }}</span>
            </div>

            <div class="info-item">
              <label>Rol:</label>
              <span class="role-badge" :class="roleClass">
                {{ usuario.rol === 'admin' ? 'Administrador' : 'Usuario Regular' }}
              </span>
            </div>

            <div class="info-item" v-if="usuario.fecha_registro">
              <label>Fecha de Registro:</label>
              <span>{{ formatDate(usuario.fecha_registro) }}</span>
            </div>

            <div class="info-item">
              <label>Estado:</label>
              <span class="status-active">Activo</span>
            </div>
          </div>
        </div>
      </div>

      <div class="profile-actions">
        <div class="actions-card">
          <h3>Acciones Disponibles</h3>

          <div class="actions-grid">
            <button 
              class="action-btn" 
              @click="goToHome"
              v-if="isOwnProfile"
            >
              🏠 Ir al Inicio
            </button>

            <button 
              class="action-btn" 
              @click="goToAdmin"
              v-if="isAdmin"
            >
              ⚙️ Panel Admin
            </button>

            <button 
              class="action-btn secondary" 
              @click="goBack"
            >
              ← Volver
            </button>

            <button 
              class="action-btn danger" 
              @click="logout"
              v-if="isOwnProfile"
            >
              🚪 Cerrar Sesión
            </button>
          </div>
        </div>
      </div>

      <div class="profile-stats" v-if="isOwnProfile">
        <div class="stats-card">
          <h3>Estadísticas</h3>

          <div class="stats-grid">
            <div class="stat-item">
              <div class="stat-number">1</div>
              <div class="stat-label">Sesión Activa</div>
            </div>

            <div class="stat-item">
              <div class="stat-number">{{ getDaysRegistered(usuario.fecha_registro) }}</div>
              <div class="stat-label">Días Registrado</div>
            </div>

            <div class="stat-item">
              <div class="stat-number">{{ usuario.rol === 'admin' ? 'Full' : 'Limited' }}</div>
              <div class="stat-label">Acceso</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserProfile',
  props: {
    id: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      usuario: null,
      loading: false,
      error: null
    }
  },
  computed: {
    currentUser() {
      return this.$store.getters.currentUser
    },
    isOwnProfile() {
      return !this.id || parseInt(this.id) === this.currentUser.id
    },
    isAdmin() {
      return this.currentUser.rol === 'admin'
    },
    statusClass() {
      return {
        'status-admin': this.usuario?.rol === 'admin',
        'status-user': this.usuario?.rol === 'usuario'
      }
    },
    roleClass() {
      return {
        'role-admin': this.usuario?.rol === 'admin',
        'role-user': this.usuario?.rol === 'usuario'
      }
    }
  },
  watch: {
    id: {
      handler: 'loadUser',
      immediate: true
    }
  },
  methods: {
    async loadUser() {
      this.loading = true
      this.error = null

      try {
        const userId = this.id || this.currentUser.id

        if (this.isOwnProfile) {
          this.usuario = { ...this.currentUser }
        } else {
          const response = await axios.get(`/usuario/${userId}`)
          this.usuario = response.data
        }
      } catch (err) {
        this.error = 'No se pudo cargar la información del usuario.'
      } finally {
        this.loading = false
      }
    },
    formatDate(dateString) {
      if (!dateString) return 'No disponible'
      const date = new Date(dateString)
      return date.toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    },
    getDaysRegistered(fecha) {
      if (!fecha) return 0
      const startDate = new Date(fecha)
      const now = new Date()
      const diffTime = Math.abs(now - startDate)
      return Math.floor(diffTime / (1000 * 60 * 60 * 24))
    },
    goToHome() {
      this.$router.push('/')
    },
    goToAdmin() {
      this.$router.push('/admin')
    },
    goBack() {
      this.$router.back()
    },
    logout() {
      this.$store.dispatch('logout')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.user-profile-container {
  max-width: 900px;
  margin: auto;
  padding: 2rem;
}

.profile-header {
  text-align: center;
  margin-bottom: 2rem;
}

.loading-section {
  text-align: center;
}

.profile-card, .actions-card, .stats-card {
  background: #fff;
  border-radius: 10px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.profile-avatar {
  text-align: center;
  margin-bottom: 1rem;
}

.avatar-large {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #2980b9, #3498db);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: bold;
  margin: 0 auto;
}

.avatar-status {
  margin-top: 0.5rem;
  font-weight: bold;
}

.status-admin {
  color: #e74c3c;
}

.status-user {
  color: #27ae60;
}

.profile-info h2 {
  margin: 0;
  color: #2c3e50;
}

.user-email {
  color: #7f8c8d;
  margin-bottom: 1rem;
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.info-item label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.25rem;
}

.role-badge {
  padding: 0.25rem 0.5rem;
  border-radius: 12px;
  font-size: 0.85rem;
  color: white;
}

.role-admin {
  background-color: #c0392b;
}

.role-user {
  background-color: #2ecc71;
}

.status-active {
  background-color: #2ecc71;
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 12px;
  font-size: 0.85rem;
}

.actions-grid, .stats-grid {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.action-btn {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  background-color: #2980b9;
  color: white;
  cursor: pointer;
}

.action-btn.secondary {
  background-color: #7f8c8d;
}

.action-btn.danger {
  background-color: #e74c3c;
}

.stat-item {
  flex: 1;
  text-align: center;
}

.stat-number {
  font-size: 1.8rem;
  font-weight: bold;
  color: #34495e;
}

.stat-label {
  color: #7f8c8d;
}
</style>
