<template>
  <div>
    <h1>仪表盘 📊</h1>
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :span="6">
        <el-card>
          <div class="stat-item">
            <div class="stat-label">总权益</div>
            <div class="stat-value">¥{{ accountInfo.balance?.toFixed(2) }}</div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card>
          <div class="stat-item">
            <div class="stat-label">总收益</div>
            <div class="stat-value profit">{{ accountInfo.total_profit?.toFixed(2) }}</div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card>
          <div class="stat-item">
            <div class="stat-label">今日盈亏</div>
            <div class="stat-value" :class="accountInfo.daily_pnl >= 0 ? 'profit' : 'loss'">
              {{ accountInfo.daily_pnl >= 0 ? '+' : '' }}{{ accountInfo.daily_pnl?.toFixed(2) }}
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card>
          <div class="stat-item">
            <div class="stat-label">持仓数量</div>
            <div class="stat-value">{{ accountInfo.positions?.length }}</div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-card style="margin-top: 20px">
      <h3>当前持仓</h3>
      <el-table :data="accountInfo.positions" style="width: 100%">
        <el-table-column prop="symbol" label="代码" />
        <el-table-column prop="quantity" label="数量" />
        <el-table-column prop="avg_price" label="平均价" />
        <el-table-column prop="current_price" label="当前价" />
        <el-table-column prop="pnl" label="盈亏">
          <template #default="scope">
            <span :class="scope.row.pnl >= 0 ? 'profit' : 'loss'">
              {{ scope.row.pnl >= 0 ? '+' : '' }}{{ scope.row.pnl.toFixed(2) }}
            </span>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Dashboard',
  data() {
    return {
      accountInfo: {
        balance: 0,
        total_profit: 0,
        daily_pnl: 0,
        positions: []
      }
    }
  },
  mounted() {
    this.fetchAccountInfo()
  },
  methods: {
    async fetchAccountInfo() {
      try {
        const res = await axios.get('/api/account/info')
        this.accountInfo = res.data
      } catch (err) {
        this.$message.error('获取账户信息失败')
      }
    }
  }
}
</script>
<style scoped>
.stat-item {
  text-align: center;
  padding: 10px 0;
}
.stat-label {
  font-size: 14px;
  color: #909399;
  margin-bottom: 8px;
}
.stat-value {
  font-size: 28px;
  font-weight: bold;
}
.profit {
  color: #67c23a;
}
.loss {
  color: #f56c6c;
}
h1 {
  margin-bottom: 0;
}
h3 {
  margin-bottom: 15px;
}
</style>
