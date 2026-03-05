<template>
  <div>
    <h1>策略管理 🎯</h1>
    <el-card style="margin-top: 20px">
      <el-table :data="strategies" style="width: 100%">
        <el-table-column prop="id" label="ID" />
        <el-table-column prop="name" label="名称" />
        <el-table-column prop="description" label="描述" />
        <el-table-column label="操作">
          <template #default>
            <el-button type="primary" size="small">编辑</el-button>
            <el-button type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'Strategies',
  data() {
    return {
      strategies: []
    }
  },
  mounted() {
    this.fetchStrategies()
  },
  methods: {
    async fetchStrategies() {
      try {
        const res = await axios.get('/api/strategies')
        this.strategies = res.data.strategies
      } catch (err) {
        this.$message.error('获取策略失败')
      }
    }
  }
}
</script>
