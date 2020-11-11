<template>
<div>
    <h1>编辑题目</h1>

      <h1>{{id}}</h1>
</div>
</template>

<script>
export default {
data(){
    return{
        id: this.$route.params.problemId,
    }
}
}
</script>

<style>

</style>