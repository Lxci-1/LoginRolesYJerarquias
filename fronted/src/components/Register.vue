<!-- components/Register.vue -->
<template>
  <div class="register-modal" v-if="show">
    <div class="modal-backdrop" @click="closeModal"></div>
    <div class="modal-content">
      <div class="modal-header">
        <h3>Registrar Nuevo Usuario</h3>
        <button class="close-btn" @click="closeModal">&times;</button>
      </div>

      <div class="modal-body">
        <div v-if="error" class="alert alert-error">
          {{ error }}
        </div>

        <div v-if="success" class="alert alert-success">
          {{ success }}
        </div>

        <form @submit.prevent="handleRegister">
          <div class="form-group">
            <label for="nombre">Nombre Completo:</label>
            <input
              type="text"
              id="nombre"
              v-model="form.nombre"
              class="form-control"
              required
              :disabled="loading"
            >
          </div>

          <div class="form-group">
            <label for="correo">Correo Electrónico:</label>
            <input
              type="email"
              id="correo"
              v-model="form.correo"
              class="form-control"
              required
              :disabled="loading"
            >
          </div>

          <div class="form-group">
            <label for="contrasena">Contraseña:</label>
            <input
              type="password"
              id="contrasena"
              v-model="form.contrasena"
              class="form-control"
              required
              minlength="6"
              :disabled="loading"
            >
          </div>

          <div class="form-group">
            <label for="confirmar">Confirmar Contraseña:</label>
            <input
              type="password"
              id="confirmar"
              v-model="form.confirmarContrasena"
              class="form-control"
              required
              :disabled="loading"
            >
          </div>

          <div class="form-actions">
            <button
              type="button"
              class="btn btn-secondary"
              @click="closeModal"
              :disabled="loading"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="btn btn-primary"
              :disabled="loading"
              @click="handleRegister"
            >
              <span v-if="loading">Registrando...</span>
              <span v-else>Registrar Usuario</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Register',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      form: {
        nombre: '',
        correo: '',
        contrasena: '',
        confirmarContrasena: ''
      },
      loading: false,
      error: null,
      success: null
    }
  },
  computed: {
    isFormValid() {
      return this.form.nombre &&
             this.form.correo &&
             this.form.contrasena &&
             this.form.confirmarContrasena &&
             this.form.contrasena === this.form.confirmarContrasena &&
             this.form.contrasena.length >= 6
    }
  },
  watch: {
    show(value) {
      if (value) {
        this.resetForm()
      }
    }
  },
  methods: {
    async handleRegister(event) {
      // Prevenir el comportamiento por defecto del formulario
      if (event) {
        event.preventDefault()
      }

      console.log('handleRegister ejecutado') // Para debugging

      // Validación de contraseñas
      if (this.form.contrasena !== this.form.confirmarContrasena) {
        this.error = 'Las contraseñas no coinciden'
        return
      }

      // Validación básica del formulario
      if (!this.form.nombre || !this.form.correo || !this.form.contrasena) {
        this.error = 'Todos los campos son obligatorios'
        return
      }

      this.loading = true
      this.error = null
      this.success = null

      try {
        console.log('Enviando datos:', this.form) // Para debugging

        // Verificar si el store y la acción existen
        if (!this.$store || !this.$store.dispatch) {
          throw new Error('Store no está disponible')
        }

        const result = await this.$store.dispatch('register', {
          nombre: this.form.nombre,
          correo: this.form.correo,
          contrasena: this.form.contrasena
        })

        console.log('Resultado del registro:', result) // Para debugging

        if (result && result.success) {
          this.success = 'Usuario registrado exitosamente'
          this.$emit('user-registered')
          setTimeout(() => {
            this.closeModal()
          }, 2000)
        } else {
          this.error = result?.message || 'No se pudo registrar el usuario'
        }
      } catch (err) {
        console.error('Error en el registro:', err) // Para debugging
        this.error = 'Error en el registro: ' + (err.message || 'Error desconocido')
        
        // Si no hay store configurado, mostrar mensaje específico
        if (err.message === 'Store no está disponible') {
          this.error = 'Error: Sistema de registro no configurado'
        }
      } finally {
        this.loading = false
      }
    },
    closeModal() {
      this.$emit('close')
      this.resetForm()
    },
    resetForm() {
      this.form = {
        nombre: '',
        correo: '',
        contrasena: '',
        confirmarContrasena: ''
      }
      this.error = null
      this.success = null
      this.loading = false
    }
  }
}
</script>

<style scoped>
.register-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 999;
}

.modal-backdrop {
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
}

.modal-content {
  position: relative;
  max-width: 500px;
  margin: 10% auto;
  background: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-header h3 {
  margin: 0;
}

.alert {
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 4px;
}

.alert-error {
  background-color: #fdd;
  color: #a00;
  border: 1px solid #faa;
}

.alert-success {
  background-color: #dfd;
  color: #080;
  border: 1px solid #afa;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box;
}

.form-control:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}

.form-control:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s;
}

.btn:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
}

.btn-secondary:hover:not(:disabled) {
  background-color: #5a6268;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background-color: #0056b3;
}

.close-btn {
  background: transparent;
  border: none;
  font-size: 24px;
  cursor: pointer;
  color: #999;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-btn:hover {
  color: #333;
}
</style>

<style scoped>
.register-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 999;
}
.modal-backdrop {
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
}
.modal-content {
  position: relative;
  max-width: 500px;
  margin: 10% auto;
  background: #fff;
  padding: 20px;
  border-radius: 8px;
}
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.alert {
  padding: 10px;
  margin-bottom: 10px;
}
.alert-error {
  background-color: #fdd;
  color: #a00;
}
.alert-success {
  background-color: #dfd;
  color: #080;
}
.form-group {
  margin-bottom: 10px;
}
.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
.close-btn {
  background: transparent;
  border: none;
  font-size: 20px;
  cursor: pointer;
}
</style>



<style scoped>
.register-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background: white;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  z-index: 1001;
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  margin: 0;
  color: #2c3e50;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #aaa;
  padding: 0;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-btn:hover {
  color: #333;
}

.modal-body {
  padding: 1.5rem;
}

.form-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  margin-top: 1.5rem;
}

.btn-secondary {
  background-color: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background-color: #545b62;
}
</style>