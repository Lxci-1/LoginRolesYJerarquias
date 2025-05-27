<!-- views/Admin.vue -->
<template>
  <div class="admin-container">
    <div class="admin-header">
      <div class="header-content">
        <div class="header-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM21 9V7L15 1H5C3.89 1 3 1.89 3 3V19C3 20.1 3.9 21 5 21H11V19H5V3H13V9H21Z"/>
          </svg>
        </div>
        <div class="header-text">
          <h1>Panel de Administración</h1>
          <p>Gestión de usuarios del sistema</p>
        </div>
      </div>
      <div class="header-decoration"></div>
    </div>

    <div class="admin-stats">
      <div class="stat-box total-users">
        <div class="stat-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M16 4C18.2 4 20 5.8 20 8S18.2 12 16 12 12 10.2 12 8 13.8 4 16 4M16 14C20.4 14 24 15.8 24 18V20H8V18C8 15.8 11.6 14 16 14M8 4C10.2 4 12 5.8 12 8S10.2 12 8 12 4 10.2 4 8 5.8 4 8 4M8 14C12.4 14 16 15.8 16 18V20H0V18C0 15.8 3.6 14 8 14Z"/>
          </svg>
        </div>
        <div class="stat-content">
          <h3>{{ usuarios.length }}</h3>
          <p>Total Usuarios</p>
        </div>
        <div class="stat-accent"></div>
      </div>
      
      <div class="stat-box admin-users">
        <div class="stat-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,2A3,3 0 0,1 15,5V7A3,3 0 0,1 12,10A3,3 0 0,1 9,7V5A3,3 0 0,1 12,2M12,11C14.67,11 20,12.33 20,15V20H4V15C4,12.33 9.33,11 12,11M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
          </svg>
        </div>
        <div class="stat-content">
          <h3>{{ adminCount }}</h3>
          <p>Administradores</p>
        </div>
        <div class="stat-accent"></div>
      </div>
      
      <div class="stat-box regular-users">
        <div class="stat-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 4A4 4 0 0 1 16 8A4 4 0 0 1 12 12A4 4 0 0 1 8 8A4 4 0 0 1 12 4M12 14C16.42 14 20 15.79 20 18V20H4V18C4 15.79 7.58 14 12 14Z"/>
          </svg>
        </div>
        <div class="stat-content">
          <h3>{{ userCount }}</h3>
          <p>Usuarios Regulares</p>
        </div>
        <div class="stat-accent"></div>
      </div>
    </div>

    <div class="admin-actions">
      <button 
        class="btn btn-success" 
        @click="showRegisterModal = true"
      >
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z"/>
        </svg>
        Registrar Nuevo Usuario
      </button>
      <button 
        class="btn btn-primary" 
        @click="loadUsers"
        :disabled="loading"
      >
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M17.65,6.35C16.2,4.9 14.21,4 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20C15.73,20 18.84,17.45 19.73,14H17.65C16.83,16.33 14.61,18 12,18A6,6 0 0,1 6,12A6,6 0 0,1 12,6C13.66,6 15.14,6.69 16.22,7.78L13,11H20V4L17.65,6.35Z"/>
        </svg>
        Actualizar Lista
      </button>
      <button 
        class="btn btn-info" 
        @click="debugData"
      >
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M20,8H17.19C16.74,7.22 16.12,6.55 15.37,6.04L17,4.41L15.59,3L13.42,5.17C12.96,5.06 12.49,5 12,5C11.51,5 11.04,5.06 10.59,5.17L8.41,3L7,4.41L8.62,6.04C7.88,6.55 7.26,7.22 6.81,8H4V10H6.09C6.04,10.33 6,10.66 6,11V12H4V14H6V15C6,15.34 6.04,15.67 6.09,16H4V18H6.81C7.85,19.79 9.78,21 12,21C14.22,21 16.15,19.79 17.19,18H20V16H17.91C17.96,15.67 18,15.34 18,15V14H20V12H18V11C18,10.66 17.96,10.33 17.91,10H20V8Z"/>
        </svg>
        Debug Data
      </button>
    </div>

    <div v-if="error" class="alert alert-error">
      <svg viewBox="0 0 24 24" fill="currentColor">
        <path d="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
      </svg>
      {{ error }}
    </div>

    <div v-if="success" class="alert alert-success">
      <svg viewBox="0 0 24 24" fill="currentColor">
        <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
      </svg>
      {{ success }}
    </div>

    <!-- Debug info -->
    <div v-if="showDebug" class="debug-info">
      <div class="debug-header">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M20,8H17.19C16.74,7.22 16.12,6.55 15.37,6.04L17,4.41L15.59,3L13.42,5.17C12.96,5.06 12.49,5 12,5C11.51,5 11.04,5.06 10.59,5.17L8.41,3L7,4.41L8.62,6.04C7.88,6.55 7.26,7.22 6.81,8H4V10H6.09C6.04,10.33 6,10.66 6,11V12H4V14H6V15C6,15.34 6.04,15.67 6.09,16H4V18H6.81C7.85,19.79 9.78,21 12,21C14.22,21 16.15,19.79 17.19,18H20V16H17.91C17.96,15.67 18,15.34 18,15V14H20V12H18V11C18,10.66 17.96,10.33 17.91,10H20V8Z"/>
        </svg>
        <h3>Información de Debug:</h3>
      </div>
      <pre>{{ debugInfo }}</pre>
    </div>

    <div class="users-section">
      <div class="section-header">
        <div class="section-title">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M16 4C18.2 4 20 5.8 20 8S18.2 12 16 12 12 10.2 12 8 13.8 4 16 4M16 14C20.4 14 24 15.8 24 18V20H8V18C8 15.8 11.6 14 16 14M8 4C10.2 4 12 5.8 12 8S10.2 12 8 12 4 10.2 4 8 5.8 4 8 4M8 14C12.4 14 16 15.8 16 18V20H0V18C0 15.8 3.6 14 8 14Z"/>
          </svg>
          <h2>Lista de Usuarios ({{ usuarios.length }} usuarios)</h2>
        </div>
        <div class="section-line"></div>
      </div>
      
      <div v-if="loading" class="loading-spinner">
        <div class="spinner-container">
          <div class="spinner"></div>
          <div class="spinner-glow"></div>
        </div>
        <p>Cargando usuarios...</p>
      </div>

      <div v-else-if="usuarios.length === 0" class="no-users">
        <div class="no-users-icon">
          <svg viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,2C13.1,2 14,2.9 14,4C14,5.1 13.1,6 12,6C10.9,6 10,5.1 10,4C10,2.9 10.9,2 12,2ZM21,9V7L15,1H5C3.89,1 3,1.89 3,3V19C3,20.1 3.9,21 5,21H11V19H5V3H13V9H21Z"/>
          </svg>
        </div>
        <p>No hay usuarios registrados en el sistema.</p>
        <span>Comienza registrando el primer usuario</span>
      </div>

      <div v-else class="users-grid">
        <UserCard 
          v-for="(usuario, index) in usuarios" 
          :key="`user-${usuario.id}-${index}`"
          :user="usuario"
          :showMeta="true"
          @delete-user="handleDeleteUser"
        />
      </div>
    </div>

    <!-- Modal de registro -->
    <Register 
      :show="showRegisterModal"
      @close="showRegisterModal = false"
      @user-registered="handleUserRegistered"
    />
  </div>
</template>

<script>
import axios from 'axios'
import UserCard from '../components/UserList.vue'
import Register from '../components/Register.vue'

export default {
  name: 'Admin',
  components: {
    UserCard,
    Register
  },
  
  data() {
    return {
      usuarios: [],
      loading: false,
      error: null,
      success: null,
      showRegisterModal: false,
      showDebug: false,
      debugInfo: null
    }
  },
  
  computed: {
    adminCount() {
      return this.usuarios.filter(u => u.rol === 'admin').length
    },
    
    userCount() {
      return this.usuarios.filter(u => u.rol === 'usuario').length
    }
  },
  
  async mounted() {
    await this.loadUsers()
  },
  
  methods: {
    async loadUsers() {
      this.loading = true
      this.error = null
      
      try {
        console.log('🔄 Cargando usuarios desde API...')
        
        const response = await axios.get('/usuarios')
        
        console.log('📡 Respuesta completa:', response)
        console.log('📊 Datos recibidos:', response.data)
        console.log('🔢 Cantidad de usuarios:', response.data?.length || 'No es array')
        
        // Verificar si la respuesta es un array
        if (Array.isArray(response.data)) {
          this.usuarios = response.data
          console.log('✅ Usuarios asignados correctamente:', this.usuarios)
        } else {
          console.error('❌ La respuesta no es un array:', typeof response.data)
          this.error = 'Formato de respuesta inválido del servidor'
          this.usuarios = []
        }
        
        // Verificar duplicados
        const ids = this.usuarios.map(u => u.id)
        const uniqueIds = [...new Set(ids)]
        if (ids.length !== uniqueIds.length) {
          console.warn('⚠️ Se detectaron usuarios duplicados:', ids)
        }
        
      } catch (error) {
        console.error('❌ Error al cargar usuarios:', error)
        this.error = error.response?.data?.detail || 'Error al cargar usuarios'
        this.usuarios = []
      } finally {
        this.loading = false
      }
    },
    
    async handleDeleteUser(userId) {
      try {
        console.log('🗑️ Eliminando usuario con ID:', userId)
        
        await axios.delete(`/usuario/${userId}`)
        this.success = 'Usuario eliminado correctamente'
        
        // Recargar la lista después de eliminar
        await this.loadUsers()
        
        setTimeout(() => {
          this.success = null
        }, 3000)
      } catch (error) {
        console.error('❌ Error al eliminar usuario:', error)
        this.error = error.response?.data?.detail || 'Error al eliminar usuario'
      }
    },
    
    async handleUserRegistered() {
      console.log('✅ Usuario registrado, recargando lista...')
      this.success = 'Usuario registrado exitosamente'
      
      // Esperar un momento antes de recargar para asegurar que el backend haya procesado
      setTimeout(async () => {
        await this.loadUsers()
      }, 500)
      
      setTimeout(() => {
        this.success = null
      }, 3000)
    },
    
    debugData() {
      this.showDebug = !this.showDebug
      this.debugInfo = {
        totalUsuarios: this.usuarios.length,
        usuarios: this.usuarios,
        ids: this.usuarios.map(u => u.id),
        nombres: this.usuarios.map(u => u.nombre),
        timestamp: new Date().toISOString()
      }
      console.log('🐛 Debug Info:', this.debugInfo)
    }
  }
}
</script>

<style scoped>
.admin-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

.admin-header {
  position: relative;
  margin-bottom: 3rem;
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 50%, #ff3838 100%);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(238, 90, 36, 0.3);
}

.header-content {
  display: flex;
  align-items: center;
  padding: 3rem;
  position: relative;
  z-index: 2;
}

.header-icon {
  width: 80px;
  height: 80px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 2rem;
  backdrop-filter: blur(10px);
}

.header-icon svg {
  width: 40px;
  height: 40px;
  color: white;
}

.header-text h1 {
  margin: 0 0 0.5rem 0;
  font-size: 3rem;
  color: white;
  font-weight: 700;
  text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

.header-text p {
  margin: 0;
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 300;
}

.header-decoration {
  position: absolute;
  top: 0;
  right: 0;
  width: 200px;
  height: 200px;
  background: linear-gradient(45deg, rgba(255,255,255,0.1), transparent);
  border-radius: 50%;
  transform: translate(50%, -50%);
}

.admin-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.stat-box {
  position: relative;
  background: white;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 15px 35px rgba(0,0,0,0.1);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.stat-box:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 25px 50px rgba(0,0,0,0.15);
}

.stat-icon {
  width: 70px;
  height: 70px;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-icon svg {
  width: 35px;
  height: 35px;
  color: white;
}

.total-users .stat-icon {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.admin-users .stat-icon {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.regular-users .stat-icon {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.stat-content h3 {
  font-size: 2.8rem;
  margin: 0 0 0.3rem 0;
  font-weight: 700;
  color: #2c3e50;
}

.stat-content p {
  margin: 0;
  color: #7f8c8d;
  font-weight: 500;
  font-size: 1.1rem;
}

.stat-accent {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 4px;
}

.total-users .stat-accent {
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
}

.admin-users .stat-accent {
  background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
}

.regular-users .stat-accent {
  background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
}

.admin-actions {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 3rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 15px 30px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  position: relative;
  overflow: hidden;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn svg {
  width: 20px;
  height: 20px;
}

.btn:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.btn-success {
  background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
  color: white;
  box-shadow: 0 8px 20px rgba(17, 153, 142, 0.3);
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
}

.btn-info {
  background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
  color: #8b4513;
  box-shadow: 0 8px 20px rgba(252, 182, 159, 0.3);
}

.alert {
  padding: 1.5rem;
  margin-bottom: 2rem;
  border-radius: 12px;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.alert svg {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
}

.alert-error {
  background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
  color: #721c24;
  border-left: 5px solid #ff6b6b;
}

.alert-success {
  background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
  color: #155724;
  border-left: 5px solid #38ef7d;
}

.debug-info {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 15px;
  padding: 2rem;
  margin-bottom: 3rem;
  color: white;
  box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}

.debug-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 1rem;
}

.debug-header svg {
  width: 24px;
  height: 24px;
}

.debug-header h3 {
  margin: 0;
  font-size: 1.5rem;
}

.debug-info pre {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  padding: 1.5rem;
  overflow-x: auto;
  font-size: 14px;
  backdrop-filter: blur(10px);
  color: rgba(255, 255, 255, 0.9);
}

.users-section {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

.section-header {
  margin-bottom: 3rem;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 1rem;
}

.section-title svg {
  width: 32px;
  height: 32px;
  color: #667eea;
}

.section-title h2 {
  margin: 0;
  color: #2c3e50;
  font-size: 2.2rem;
  font-weight: 700;
}

.section-line {
  height: 4px;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  border-radius: 2px;
  width: 100px;
}

.users-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 2.5rem;
}

.loading-spinner {
  text-align: center;
  padding: 4rem;
}

.spinner-container {
  position: relative;
  width: 80px;
  height: 80px;
  margin: 0 auto 2rem;
}

.spinner {
  width: 80px;
  height: 80px;
  border: 6px solid rgba(102, 126, 234, 0.1);
  border-top: 6px solid #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  position: relative;
  z-index: 2;
}

.spinner-glow {
  position: absolute;
  top: -10px;
  left: -10px;
  width: 100px;
  height: 100px;
  background: radial-gradient(circle, rgba(102, 126, 234, 0.2) 0%, transparent 70%);
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 0.5; }
  50% { transform: scale(1.1); opacity: 0.8; }
}

.loading-spinner p {
  font-size: 1.2rem;
  color: #667eea;
  font-weight: 500;
}

.no-users {
  text-align: center;
  padding: 4rem;
  color: #7f8c8d;
}

.no-users-icon {
  width: 120px;
  height: 120px;
  margin: 0 auto 2rem;
  background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.no-users-icon svg {
  width: 60px;
  height: 60px;
  color: white;
}

.no-users p {
  font-size: 1.4rem;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  font-weight: 600;
}

.no-users span {
  font-size: 1.1rem;
  color: #7f8c8d;
  font-style: italic;
}

@media (max-width: 768px) {
  .admin-container {
    padding: 1rem;
  }
  
  .header-content {
    flex-direction: column;
    text-align: center;
    padding: 2rem;
  }
  
  .header-icon {
    margin-right: 0;
    margin-bottom: 1rem;
  }
  
  .header-text h1 {
    font-size: 2.2rem;
  }
  
  .admin-stats {
    grid-template-columns: 1fr;
  }
  
  .stat-box {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .admin-actions {
    flex-direction: column;
    align-items: stretch;
  }
  
  .admin-actions .btn {
    width: 100%;
    justify-content: center;
  }
  
  .users-grid {
    grid-template-columns: 1fr;
  }
  
  .section-title {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
}
</style>