<!-- views/Home.vue -->
<template>
  <div class="home-container">
    <div class="welcome-section">
      <div class="welcome-content">
        <div class="welcome-badge">Dashboard</div>
        <h1>¡Bienvenido, {{ $store.getters.currentUser?.nombre }}!</h1>
        <p class="welcome-text">Sistema de Gestión de Usuarios</p>
        <div class="welcome-decoration"></div>
      </div>
    </div>
    
    <div class="stats-grid">
      <div class="stat-card profile-card">
        <div class="stat-icon">👤</div>
        <div class="stat-info">
          <h3>Tu Perfil</h3>
          <p>{{ $store.getters.currentUser?.rol === 'admin' ? 'Administrador' : 'Usuario' }}</p>
        </div>
        <div class="card-glow"></div>
      </div>
      
      <div class="stat-card email-card">
        <div class="stat-icon">📧</div>
        <div class="stat-info">
          <h3>Email</h3>
          <p>{{ $store.getters.currentUser?.correo }}</p>
        </div>
        <div class="card-glow"></div>
      </div>
      
      <div class="stat-card admin-card" v-if="$store.getters.isAdmin">
        <div class="stat-icon">⚙️</div>
        <div class="stat-info">
          <h3>Panel Admin</h3>
          <p>Gestionar usuarios</p>
        </div>
        <div class="card-glow"></div>
      </div>
    </div>
    
    <div class="actions-section">
      <div class="section-header">
        <h2>Acciones Disponibles</h2>
        <div class="header-line"></div>
      </div>
      
      <div class="actions-grid">
        <div class="action-card profile-action" @click="goToProfile">
          <div class="action-background"></div>
          <div class="action-content">
            <div class="action-icon">👤</div>
            <h3>Ver Mi Perfil</h3>
            <p>Consulta tu información personal</p>
          </div>
        </div>
        
        <div class="action-card admin-action" @click="goToAdmin" v-if="$store.getters.isAdmin">
          <div class="action-background"></div>
          <div class="action-content">
            <div class="action-icon">👥</div>
            <h3>Panel de Administración</h3>
            <p>Gestionar usuarios del sistema</p>
          </div>
        </div>
        
        <div class="action-card logout-action" @click="logout">
          <div class="action-background"></div>
          <div class="action-content">
            <div class="action-icon">🚪</div>
            <h3>Cerrar Sesión</h3>
            <p>Salir del sistema de forma segura</p>
          </div>
        </div>
      </div>
    </div>
    
    <div class="info-section">
      <div class="section-header">
        <h2>Información del Sistema</h2>
        <div class="header-line"></div>
      </div>
      <div class="info-grid">
        <div class="info-item version-info">
          <div class="info-icon">🚀</div>
          <div class="info-content">
            <strong>Versión:</strong> 1.0.0
          </div>
        </div>
        <div class="info-item update-info">
          <div class="info-icon">📅</div>
          <div class="info-content">
            <strong>Última actualización:</strong> {{ getCurrentDate() }}
          </div>
        </div>
        <div class="info-item status-info">
          <div class="info-icon">⚡</div>
          <div class="info-content">
            <strong>Estado:</strong> <span class="status-active">Activo</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  
  methods: {
    goToProfile() {
      this.$router.push('/profile')
    },
    
    goToAdmin() {
      this.$router.push('/admin')
    },
    
    logout() {
      this.$store.dispatch('logout')
      this.$router.push('/login')
    },
    
    getCurrentDate() {
      return new Date().toLocaleDateString('es-ES', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.home-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

.welcome-section {
  position: relative;
  text-align: center;
  margin-bottom: 4rem;
  padding: 3rem;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 25px;
  overflow: hidden;
}

.welcome-content {
  position: relative;
  z-index: 2;
}

.welcome-badge {
  display: inline-block;
  background: linear-gradient(45deg, #ff6b6b, #ee5a24);
  color: white;
  padding: 0.5rem 1.5rem;
  border-radius: 25px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.welcome-section h1 {
  margin: 0 0 1rem 0;
  font-size: 3rem;
  font-weight: 700;
  background: linear-gradient(45deg, #ffffff, #f8f9fa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.welcome-text {
  font-size: 1.3rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  font-weight: 300;
}

.welcome-decoration {
  position: absolute;
  top: -50%;
  right: -10%;
  width: 300px;
  height: 300px;
  background: linear-gradient(45deg, #ff9a9e, #fecfef);
  border-radius: 50%;
  opacity: 0.1;
  z-index: 1;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.stat-card {
  position: relative;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 2.5rem;
  border-radius: 20px;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  overflow: hidden;
}

.stat-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

.profile-card:hover {
  background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.1));
}

.email-card:hover {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(26, 188, 156, 0.1));
}

.admin-card:hover {
  background: linear-gradient(135deg, rgba(230, 126, 34, 0.1), rgba(231, 76, 60, 0.1));
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transform: translateX(-100%);
  transition: transform 0.6s;
}

.stat-card:hover .card-glow {
  transform: translateX(100%);
}

.stat-icon {
  font-size: 3rem;
  opacity: 0.8;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}

.stat-info h3 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
  font-size: 1.4rem;
  font-weight: 600;
}

.stat-info p {
  margin: 0;
  color: #7f8c8d;
  font-size: 1.1rem;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
  position: relative;
}

.section-header h2 {
  color: white;
  font-size: 2.2rem;
  font-weight: 700;
  margin: 0 0 1rem 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.header-line {
  width: 80px;
  height: 4px;
  background: linear-gradient(45deg, #ff6b6b, #ee5a24);
  margin: 0 auto;
  border-radius: 2px;
}

.actions-section {
  margin-bottom: 4rem;
}

.actions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.action-card {
  position: relative;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  overflow: hidden;
}

.action-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0;
  transition: opacity 0.3s;
}

.profile-action .action-background {
  background: linear-gradient(135deg, #3498db, #9b59b6);
}

.admin-action .action-background {
  background: linear-gradient(135deg, #e67e22, #e74c3c);
}

.logout-action .action-background {
  background: linear-gradient(135deg, #95a5a6, #34495e);
}

.action-card:hover {
  transform: translateY(-10px) scale(1.05);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
}

.action-card:hover .action-background {
  opacity: 0.1;
}

.action-card:hover .action-content {
  color: white;
}

.action-content {
  position: relative;
  z-index: 2;
  padding: 2.5rem;
  text-align: center;
  transition: color 0.3s;
}

.action-icon {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}

.action-card h3 {
  margin: 0 0 1rem 0;
  color: #2c3e50;
  font-size: 1.4rem;
  font-weight: 600;
  transition: color 0.3s;
}

.action-card p {
  margin: 0;
  color: #7f8c8d;
  font-size: 1rem;
  transition: color 0.3s;
}

.action-card:hover h3,
.action-card:hover p {
  color: white;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.info-section {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 3rem;
  border-radius: 25px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
  border-radius: 15px;
  transition: all 0.3s;
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.info-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.version-info:hover {
  background: linear-gradient(135deg, #e3f2fd, #bbdefb);
}

.update-info:hover {
  background: linear-gradient(135deg, #f3e5f5, #e1bee7);
}

.status-info:hover {
  background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
}

.info-icon {
  font-size: 1.5rem;
  opacity: 0.8;
}

.info-content {
  flex: 1;
  font-size: 1rem;
}

.status-active {
  color: #27ae60;
  font-weight: bold;
  padding: 0.25rem 0.75rem;
  background: rgba(46, 204, 113, 0.1);
  border-radius: 15px;
}

@media (max-width: 768px) {
  .home-container {
    padding: 1rem;
  }
  
  .welcome-section h1 {
    font-size: 2.2rem;
  }
  
  .stats-grid,
  .actions-grid {
    grid-template-columns: 1fr;
  }
  
  .welcome-section {
    padding: 2rem;
  }
  
  .stat-card,
  .action-content {
    padding: 2rem;
  }
}

@media (max-width: 480px) {
  .welcome-section h1 {
    font-size: 1.8rem;
  }
  
  .stat-card,
  .action-content {
    padding: 1.5rem;
  }
  
  .info-section {
    padding: 2rem;
  }
}
</style>