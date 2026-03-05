<template>
  <div>
    <h1>市场行情 📈</h1>
    <el-card style="margin-top: 20px">
      <el-form-item label="股票代码">
        <el-input v-model="symbol" placeholder="输入股票代码，例如: AAPL" style="width: 300px" />
        <el-button type="primary" @click="fetchData" :loading="loading" style="margin-left: 10px">查询</el-button>
      </el-form-item>
      
      <div v-if="chartData.length > 0" style="height: 500px; margin-top: 20px">
        <v-chart :option="chartOption" />
      </div>
    </el-card>
  </div>
</template>
<script>
import axios from 'axios'
import * as echarts from 'echarts'
import VChart from 'vue-echarts'
export default {
  name: 'Market',
  components: {
    VChart
  },
  data() {
    return {
      symbol: 'AAPL',
      loading: false,
      chartData: [],
      chartOption: {}
    }
  },
  methods: {
    async fetchData() {
      this.loading = true
      try {
        const res = await axios.get(`/api/market/data/${this.symbol}`, { params: { period: '1y' } })
        this.chartData = res.data.data
        this.updateChart()
      } catch (err) {
        this.$message.error('获取行情失败')
      } finally {
        this.loading = false
      }
    },
    updateChart() {
      const dates = this.chartData.map(item => item.Date.split('T')[0])
      const prices = this.chartData.map(item => item.Close)
      
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
          name: '价格'
        },
        series: [{
          data: prices,
          type: 'line',
          name: this.symbol,
          smooth: true
        }]
      }
    }
  }
}
</script>
