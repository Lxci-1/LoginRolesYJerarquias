<!-- components/Login.vue -->
<template>
  <div class="login-container">
    <div class="login-card">
      <!-- Header elegante -->
      <div class="login-header">
        <div class="logo-wrapper">
          <svg class="logo-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 12C14.7614 12 17 9.76142 17 7C17 4.23858 14.7614 2 12 2C9.23858 2 7 4.23858 7 7C7 9.76142 9.23858 12 12 12Z" fill="currentColor"/>
            <path d="M12 14C7.58172 14 4 17.5817 4 22H20C20 17.5817 16.4183 14 12 14Z" fill="currentColor"/>
          </svg>
        </div>
        <h1 class="welcome-title">Bienvenido de vuelta</h1>
        <p class="welcome-subtitle">Ingresa tus credenciales para continuar</p>
      </div>
      
      <!-- Alerta de error mejorada -->
      <div v-if="$store.getters.error" class="error-alert">
        <svg class="error-icon" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
        <span>{{ $store.getters.error }}</span>
      </div>
      
      <!-- Formulario elegante -->
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="input-group">
          <label class="input-label">Correo electrónico</label>
          <div class="input-container">
            <svg class="input-icon" viewBox="0 0 20 20" fill="currentColor">
              <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
              <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
            </svg>
            <input 
              type="email"
              v-model="form.correo"
              placeholder="tu@email.com"
              class="form-input"
              required
              :disabled="$store.getters.isLoading"
            >
          </div>
        </div>
        
        <div class="input-group">
          <label class="input-label">Contraseña</label>
          <div class="input-container">
            <svg class="input-icon" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a5 5 0 0110 0z" clip-rule="evenodd" />
            </svg>
            <input 
              type="password"
              v-model="form.contrasena"
              placeholder="••••••••"
              class="form-input"
              required
              :disabled="$store.getters.isLoading"
            >
          </div>
        </div>
        
        <button 
          type="submit"
          class="login-button"
          :disabled="$store.getters.isLoading"
          :class="{ 'loading': $store.getters.isLoading }"
        >
          <span v-if="$store.getters.isLoading" class="button-content">
            <div class="loading-spinner"></div>
            Iniciando sesión...
          </span>
          <span v-else class="button-content">
            <svg class="button-icon" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M3 3a1 1 0 011 1v12a1 1 0 11-2 0V4a1 1 0 011-1zm7.707 3.293a1 1 0 010 1.414L9.414 9H17a1 1 0 110 2H9.414l1.293 1.293a1 1 0 01-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            Iniciar Sesión
          </span>
        </button>
      </form>
      
      <!-- Credenciales de prueba con diseño profesional -->
      <div class="demo-section">
        <div class="demo-header">
          <svg class="demo-icon" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
          </svg>
          <h3>Credenciales de prueba</h3>
        </div>
        
        <div class="credentials-grid">
          <div class="credential-card admin">
            <div class="credential-header">
              <svg class="role-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9.504 1.132a1 1 0 01.992 0l8 4.5a1 1 0 01-.496 1.868L18 7.5V16a2 2 0 01-2 2H4a2 2 0 01-2-2V7.5L2 7.5a1 1 0 01-.496-1.868l8-4.5zM6 4a1 1 0 012 0v2a1 1 0 01-2 0V4zm6 0a1 1 0 012 0v2a1 1 0 01-2 0V4z" clip-rule="evenodd" />
              </svg>
              <span class="role-title">Administrador</span>
            </div>
            <div class="credential-info">
              <div class="credential-field">
                <span class="field-label">Email:</span>
                <code class="field-value">admin@test.com</code>
              </div>
              <div class="credential-field">
                <span class="field-label">Pass:</span>
                <code class="field-value">admin123</code>
              </div>
            </div>
          </div>
          
          <div class="credential-card user">
            <div class="credential-header">
              <svg class="role-icon" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
              </svg>
              <span class="role-title">Usuario</span>
            </div>
            <div class="credential-info">
              <div class="credential-field">
                <span class="field-label">Email:</span>
                <code class="field-value">user@test.com</code>
              </div>
              <div class="credential-field">
                <span class="field-label">Pass:</span>
                <code class="field-value">user123</code>
              </div>
            </div>
          </div>
        </div>
        
        <p class="demo-note">
          <svg class="note-icon" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
          El administrador debe crear estos usuarios primero
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      form: {
        correo: '',
        contrasena: ''
      }
    }
  },
  
  mounted() {
    this.$store.dispatch('clearError')
  },
  
  methods: {
    async handleLogin() {
      const result = await this.$store.dispatch('login', this.form)
      
      if (result.success) {
        if (this.$store.getters.isAdmin) {
          this.$router.push('/admin')
        } else {
          this.$router.push('/home')
        }
      }
    }
  }
}
</script>

<style scoped>
/* Variables CSS para consistencia */
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --surface-color: rgba(255, 255, 255, 0.95);
  --text-primary: #1e293b;
  --text-secondary: #64748b;
  --border-color: #e2e8f0;
  --error-color: #ef4444;
  --success-color: #10b981;
  --admin-color: #8b5cf6;
  --user-color: #06b6d4;
}

/* Reset y base */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow-x: hidden;
}

/* Contenedor principal */
.login-container {
  min-height: 100vh;
  width: 100vw;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: url('https://fondosmil.co/fondo/52045.jpg') center/cover no-repeat fixed;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.login-container::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  background: var(--primary-gradient);
  opacity: 0.4;
  backdrop-filter: blur(1px);
  z-index: 1;
}

/* Tarjeta principal */
.login-card {
  background: var(--surface-color);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  box-shadow: 
    0 32px 64px rgba(0, 0, 0, 0.12),
    0 0 0 1px rgba(255, 255, 255, 0.1);
  width: 100%;
  max-width: 440px;
  padding: 3rem;
  position: relative;
  z-index: 10;
  animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Header del login */
.login-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.logo-wrapper {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 72px;
  height: 72px;
  background: var(--primary-gradient);
  border-radius: 20px;
  margin-bottom: 1.5rem;
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.25);
}

.logo-icon {
  width: 32px;
  height: 32px;
  color: white;
}

.welcome-title {
  font-size: 1.875rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0 0 0.5rem 0;
  letter-spacing: -0.025em;
}

.welcome-subtitle {
  font-size: 1rem;
  color: var(--text-secondary);
  margin: 0;
  font-weight: 400;
}

/* Alerta de error */
.error-alert {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.25rem;
  background: #fef2f2;
  border: 1px solid #fecaca;
  border-radius: 12px;
  color: var(--error-color);
  font-weight: 500;
  margin-bottom: 1.5rem;
}

.error-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

/* Formulario */
.login-form {
  margin-bottom: 2rem;
}

.input-group {
  margin-bottom: 1.5rem;
}

.input-label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.input-container {
  position: relative;
}

.input-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  color: var(--text-secondary);
  z-index: 1;
}

.form-input {
  width: 100%;
  padding: 1rem 1rem 1rem 3rem;
  border: 2px solid var(--border-color);
  border-radius: 12px;
  font-size: 1rem;
  color: var(--text-primary);
  background: #fafbfc;
  transition: all 0.2s ease;
}

.form-input:focus {
  outline: none;
  border-color: #667eea;
  background: white;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-input:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.form-input::placeholder {
  color: #94a3b8;
}

/* Botón de login */
.login-button {
  width: 100%;
  padding: 1rem 1.5rem;
  background: var(--primary-gradient);
  border: none;
  border-radius: 12px;
  color: white;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}

.login-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
}

.login-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.button-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.button-icon {
  width: 20px;
  height: 20px;
}

.loading-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Sección de credenciales */
.demo-section {
  border-top: 1px solid var(--border-color);
  padding-top: 2rem;
}

.demo-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.demo-icon {
  width: 20px;
  height: 20px;
  color: var(--text-secondary);
}

.demo-header h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.credentials-grid {
  display: grid;
  gap: 1rem;
  margin-bottom: 1rem;
}

.credential-card {
  padding: 1.25rem;
  border-radius: 12px;
  border: 1px solid var(--border-color);
  background: #fafbfc;
}

.credential-card.admin {
  border-left: 4px solid var(--admin-color);
}

.credential-card.user {
  border-left: 4px solid var(--user-color);
}

.credential-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.role-icon {
  width: 18px;
  height: 18px;
}

.credential-card.admin .role-icon {
  color: var(--admin-color);
}

.credential-card.user .role-icon {
  color: var(--user-color);
}

.role-title {
  font-weight: 600;
  font-size: 0.875rem;
  color: var(--text-primary);
}

.credential-info {
  display: grid;
  gap: 0.5rem;
}

.credential-field {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.field-label {
  font-size: 0.8rem;
  color: var(--text-secondary);
  font-weight: 500;
}

.field-value {
  background: white;
  color: var(--text-primary);
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
  border: 1px solid var(--border-color);
}

.demo-note {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  color: var(--text-secondary);
  font-size: 0.8rem;
  line-height: 1.4;
  margin-top: 1rem;
}

.note-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
  margin-top: 0.1rem;
}

/* Responsive */
@media (max-width: 480px) {
  .login-container {
    padding: 1rem;
  }
  
  .login-card {
    padding: 2rem 1.5rem;
  }
  
  .welcome-title {
    font-size: 1.5rem;
  }
}
</style>