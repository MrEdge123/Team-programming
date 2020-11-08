<template>
  <div class="body">
    <div>Copyright @2019 wavedanger 版权所有</div>
  </div>
</template>

<script>
export default {
  name: 'v-footer',
  props: {
    msg: String
  }
}
</script>

<style scoped>
.body{
    width:100%;
    height:60px;
    color:white;
    background-color:#333;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
  }
</style>
