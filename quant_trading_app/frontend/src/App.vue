<template>
  <div id="app">
    <el-container>
      <el-aside width="200px" class="sidebar">
        <h2>📈 量化交易</h2>
        <el-menu :default-active="activeMenu" router>
          <el-menu-item index="dashboard">
            <span>仪表盘</span>
          </el-menu-item>
          <el-menu-item index="backtest">
            <span>策略回测</span>
          </el-menu-item>
          <el-menu-item index="strategies">
            <span>策略管理</span>
          </el-menu-item>
          <el-menu-item index="portfolio">
            <span>资产组合</span>
          </el-menu-item>
          <el-menu-item index="market">
            <span>市场行情</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <div class="content-wrapper">
          <Dashboard v-if="activeMenu === 'dashboard'" />
          <Backtest v-else-if="activeMenu === 'backtest'" />
          <Strategies v-else-if="activeMenu === 'strategies'" />
          <Portfolio v-else-if="activeMenu === 'portfolio'" />
          <Market v-else-if="activeMenu === 'market'" />
        </div>
      </el-main>
    </el-container>
  </div>
</template>
<script>
import Dashboard from './components/Dashboard.vue'
import Backtest from './components/Backtest.vue'
import Strategies from './components/Strategies.vue'
import Portfolio from './components/Portfolio.vue'
import Market from './components/Market.vue'
export default {
  name: 'App',
  components: {
    Dashboard,
    Backtest,
    Strategies,
    Portfolio,
    Market
  },
  data() {
    return {
      activeMenu: 'dashboard'
    }
  }
}
</script>
<style>
#app {
  height: 100vh;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
.sidebar {
  background: #304156;
  color: white;
}
.sidebar h2 {
  text-align: center;
  padding: 20px 0;
  margin: 0;
  color: white;
}
.content-wrapper {
  padding: 20px;
}
.el-menu {
  background-color: transparent;
  border: none;
}
.el-menu-item {
  color: #bfcbd9 !important;
}
.el-menu-item:hover {
  background-color: #263445 !important;
  color: white !important;
}
.el-menu-item.is-active {
  background-color: #1890ff !important;
  color: white !important;
}
</style>
