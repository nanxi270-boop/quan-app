<template>
  <div>
    <h1>策略回测 📝</h1>
    <el-card style="margin-top: 20px">
      <el-form :model="backtestRequest" label-width="120px">
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="股票代码">
              <el-input v-model="backtestRequest.symbol" placeholder="例如: AAPL" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="策略">
              <el-select v-model="backtestRequest.strategy" placeholder="选择策略" style="width: 100%">
                <el-option v-for="s in strategies" :key="s.id" :label="s.name" :value="s.id" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="20">
          <el-col :span="12">
            <el-form-item label="开始日期">
              <el-date-picker
                v-model="backtestRequest.start_date"
                type="date"
                placeholder="选择开始日期"
                format="YYYY-MM-DD"
                value-format="YYYY-MM-DD"
                style="width: 100%"
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="结束日期">
              <el-date-picker
                v-model="backtestRequest.end_date"
                type="date"
                placeholder="选择结束日期"
                format="YYYY-MM-DD"
                value-format="YYYY-MM-DD"
                style="width: 100%"
              />
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item label="初始资金">
          <el-input-number v-model="backtestRequest.initial_capital" :min="1000" :step="10000" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="runBacktest" :loading="loading">开始回测</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    <el-card v-if="backtestResult" style="margin-top: 20px">
      <h3>回测结果</h3>
      <el-row :gutter="20">
        <el-col :span="6">
          <div class="result-card">
            <div class="label">初始资金</div>
            <div class="value">¥{{ backtestResult.initial_capital.toFixed(2) }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="result-card">
            <div class="label">最终权益</div>
            <div class="value">¥{{ backtestResult.final_equity.toFixed(2) }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="result-card">
            <div class="label">总收益率</div>
            <div class="value" :class="backtestResult.total_return_pct >= 0 ? 'profit' : 'loss'">
              {{ backtestResult.total_return_pct.toFixed(2) }}%
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="result-card">
            <div class="label">交易次数</div>
            <div class="value">{{ backtestResult.num_trades }}</div>
          </div>
        </el-col>
      </el-row>
      <div style="margin-top: 20px; height: 400px;">
        <v-chart :option="chartOption" />
      </div>
      <el-table v-if="backtestResult.trades.length > 0" :data="backtestResult.trades" style="margin-top: 20px">
        <el-table-column prop="date" label="日期" />
        <el-table-column prop="type" label="类型">
          <template #default="scope">
            <el-tag :type="scope.row.type === 'buy' ? 'primary' : 'success'">
              {{ scope.row.type === 'buy' ? '买入' : '卖出' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="price" label="价格" />
        <el-table-column prop="shares" label="数量" />
      </el-table>
    </el-card>
  </div>
</template>
<script>
import axios from 'axios'
import * as echarts from 'echarts'
import VChart from 'vue-echarts'
export default {
  name: 'Backtest',
  components: {
    VChart
  },
  data() {
    const defaultStart = new Date()
    defaultStart.setFullYear(defaultStart.getFullYear() - 1)
    return {
      strategies: [],
      loading: false,
      backtestRequest: {
        symbol: 'AAPL',
        strategy: 'ma_cross',
        start_date: this.formatDate(defaultStart),
        end_date: this.formatDate(new Date()),
        initial_capital: 100000
      },
      backtestResult: null,
      chartOption: {}
    }
  },
  mounted() {
    this.fetchStrategies()
  },
  methods: {
    formatDate(date) {
      return date.toISOString().split('T')[0]
    },
    async fetchStrategies() {
      try {
        const res = await axios.get('/api/strategies')
        this.strategies = res.data.strategies
      } catch (err) {
        this.$message.error('获取策略列表失败')
      }
    },
    async runBacktest() {
      this.loading = true
      try {
        const res = await axios.post('/api/backtest', this.backtestRequest)
        this.backtestResult = res.data
        this.updateChart()
        this.$message.success('回测完成')
      } catch (err) {
        this.$message.error('回测失败: ' + err.message)
      } finally {
        this.loading = false
      }
    },
    updateChart() {
      const dates = this.backtestResult.equity_curve.map(item => item.date)
      const equity = this.backtestResult.equity_curve.map(item => item.equity)
      
      this.chartOption = {
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          data: dates
        },
        yAxis: {
          type: 'value',
          name: '权益'
        },
        series: [{
          data: equity,
          type: 'line',
          smooth: true,
          lineStyle: {
            color: '#1890ff'
          },
          areaStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              { offset: 0, color: 'rgba(24, 144, 255, 0.3)' },
              { offset: 1, color: 'rgba(24, 144, 255, 0.05)' }
            ])
          }
        }]
      }
    }
  }
}
</script>
<style scoped>
.result-card {
  text-align: center;
  padding: 15px;
  background: #f5f7fa;
  border-radius: 8px;
}
.result-card .label {
  font-size: 14px;
  color: #909399;
  margin-bottom: 8px;
}
.result-card .value {
  font-size: 24px;
  font-weight: bold;
}
.profit {
  color: #67c23a;
}
.loss {
  color: #f56c6c;
}
</style>
