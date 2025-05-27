<!-- components/UserList.vue -->
<template>
  <div class="user-card">
    <div class="user-header">
      <h3>Perfil de Usuario</h3>
      <span class="user-badge" :class="user.rol === 'admin' ? 'badge-admin' : 'badge-user'">
        {{ user.rol }}
      </span>
    </div>
    
    <div class="user-body">
      <div class="user-info">
        <p><strong>ID:</strong> {{ user.id }}</p>
        <p><strong>Nombre:</strong> {{ user.nombre }}</p>
        <p><strong>Correo:</strong> {{ user.correo }}</p>
        <p><strong>Rol:</strong> {{ user.rol }}</p>
      </div>
      
      <div v-if="showMeta" class="user-meta">
        <p v-if="user.fecha_creacion"><strong>Creado:</strong> {{ formatDate(user.fecha_creacion) }}</p>
        <p v-if="user.ultimo_acceso"><strong>Último acceso:</strong> {{ formatDate(user.ultimo_acceso) }}</p>
      </div>
    </div>
    
    <div class="user-actions">
      <button 
        class="btn btn-danger" 
        @click="confirmDelete"
        :disabled="user.rol === 'admin' && isCurrentUser"
      >
        🗑️ Eliminar Usuario
      </button>
      
      <button 
        v-if="user.rol !== 'admin'" 
        class="btn btn-warning" 
        @click="promoteToAdmin"
      >
        ⬆️ Hacer Admin
      </button>
    </div>
    
    <!-- Modal de confirmación -->
    <div v-if="showConfirm" class="confirm-modal">
      <div class="confirm-backdrop" @click="showConfirm = false"></div>
      <div class="confirm-content">
        <h4>Confirmar Eliminación</h4>
        <p>¿Estás seguro de que quieres eliminar al usuario <strong>{{ user.nombre }}</strong>?</p>
        <div class="confirm-actions">
          <button class="btn btn-secondary" @click="showConfirm = false">Cancelar</button>
          <button class="btn btn-danger" @click="deleteUser">Confirmar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserCard',
  props: {
    user: {
      type: Object,
      required: true,
      validator(value) {
        // Validar que el objeto user tenga las propiedades necesarias
        return value && 
               typeof value.id !== 'undefined' && 
               typeof value.nombre === 'string' && 
               typeof value.correo === 'string' && 
               typeof value.rol === 'string'
      }
    },
    showMeta: {
      type: Boolean,
      default: false
    },
    currentUserId: {
      type: [String, Number],
      default: null
    }
  },
  
  data() {
    return {
      showConfirm: false
    }
  },
  
  computed: {
    isCurrentUser() {
      return this.currentUserId && this.user.id === this.currentUserId
    }
  },
  
  mounted() {
    // Debug: verificar que los datos llegan correctamente
    console.log('UserCard montado con usuario:', this.user)
  },
  
  methods: {
    confirmDelete() {
      this.showConfirm = true
    },
    
    deleteUser() {
      this.showConfirm = false
      this.$emit('delete-user', this.user.id)
    },
    
    promoteToAdmin() {
      this.$emit('promote-user', this.user.id)
    },
    
    formatDate(dateString) {
      if (!dateString) return 'N/A'
      
      try {
        const date = new Date(dateString)
        return date.toLocaleDateString('es-ES', {
          year: 'numeric',
          month: 'short',
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit'
        })
      } catch (error) {
        return 'Fecha inválida'
      }
    }
  }
}
</script>

<style scoped>
.user-card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  position: relative;
}

.user-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.user-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #f0f0f0;
}

.user-header h3 {
  margin: 0;
  color: #2c3e50;
  font-size: 1.2rem;
}

.user-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: bold;
  text-transform: uppercase;
}

.badge-admin {
  background-color: #e74c3c;
  color: white;
}

.badge-user {
  background-color: #3498db;
  color: white;
}

.user-body {
  margin-bottom: 1rem;
}

.user-info p {
  margin: 0.5rem 0;
  color: #34495e;
}

.user-info strong {
  color: #2c3e50;
  min-width: 60px;
  display: inline-block;
}

.user-meta {
  margin-top: 1rem;
  padding-top: 0.5rem;
  border-top: 1px solid #f0f0f0;
  font-size: 0.9rem;
}

.user-meta p {
  margin: 0.25rem 0;
  color: #7f8c8d;
}

.user-actions {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

.btn-danger {
  background-color: #e74c3c;
  color: white;
}

.btn-danger:hover:not(:disabled) {
  background-color: #c0392b;
}

.btn-warning {
  background-color: #f39c12;
  color: white;
}

.btn-warning:hover:not(:disabled) {
  background-color: #e67e22;
}

.btn-secondary {
  background-color: #95a5a6;
  color: white;
}

.btn-secondary:hover:not(:disabled) {
  background-color: #7f8c8d;
}

/* Modal de confirmación */
.confirm-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1000;
}

.confirm-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
}

.confirm-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 90%;
}

.confirm-content h4 {
  margin: 0 0 1rem 0;
  color: #e74c3c;
}

.confirm-content p {
  margin: 0 0 1.5rem 0;
  color: #2c3e50;
}

.confirm-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}

@media (max-width: 768px) {
  .user-card {
    padding: 1rem;
  }
  
  .user-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .user-actions {
    flex-direction: column;
  }
  
  .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>