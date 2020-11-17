<template>
<!-- 只是写了一个界面，功能什么的还没有实现 -->
  <div>
<el-button @click="resetDateFilter">清除日期过滤器</el-button>
  <el-button @click="clearFilter">清除所有过滤器</el-button>
  <el-table
    ref="filterTable"
    :data="tableData"
    style="width: 100%">
    <el-table-column
      prop="name"
      label="用户名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="题目编号"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="运行结果"
      width="180">
    </el-table-column>
    <el-table-column
      prop="address"
      label="消耗内存"
      :formatter="formatter">
    </el-table-column>
    <el-table-column
      prop="address"
      label="运行时间"
      :formatter="formatter">
    </el-table-column>
    <el-table-column
      prop="tag"
      label="使用语言"
      width="100"
      :filters="[{ text: 'C', value: 'C' }, { text: 'Python', value: 'Python' }
      ,{ text: 'C++', value: 'C++' },{ text: 'Java', value: 'Java' }]"
      :filter-method="filterTag"
      filter-placement="bottom-end">
      <template slot-scope="scope">
        <el-tag
          :type="scope.row.tag === 'C' ? 'primary' : 'success'"
          disable-transitions>{{scope.row.tag}}</el-tag>
      </template>
    </el-table-column>
        <el-table-column
      prop="date"
      label="提交时间"
      sortable
      width="180"
      column-key="date"
      :filters="[{text: '2016-05-01', value: '2016-05-01'}, {text: '2016-05-02', value: '2016-05-02'}, {text: '2016-05-03', value: '2016-05-03'}, {text: '2016-05-04', value: '2016-05-04'}]"
      :filter-method="filterHandler"
    >
    </el-table-column>
  </el-table>

  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
          tag: 'C'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄',
          tag: 'Python'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄',
          tag: 'C'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄',
          tag: 'Python'
        }]
      }
    },
    methods: {
      resetDateFilter() {
        this.$refs.filterTable.clearFilter('date');
      },
      clearFilter() {
        this.$refs.filterTable.clearFilter();
      },
      formatter(row, column) {
        return row.address;
      },
      filterTag(value, row) {//页面内
        return row.tag === value;
      },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      }
    }
  }
</script>

<style>

</style>