<template>
    <div class="modal" v-bind:class="mdShow?'show':'unShow'">
      <div class="md-inner">
        <div class="md-top">
          <a href="javascript:" @click="closeModal">关闭</a>
        </div>
        <div class="md-content">
          <slot name="message"></slot>
        </div>
        <div class="md-bottom">
          <slot name="btnGroup"></slot>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'modal',
  props: {
   'mdShow':Boolean
  },
  methods:{
    closeModal(){
      this.$emit("close");
    }
  }
}
</script>

<style scoped>
.show {
  display: block;
}
.unShow {
  display: none;
}
.modal {
  width: 200px;
  height: 150px;
  border: 1px solid #333;
  background-color: white;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  color: #333;
}
.md-top {
  text-align: right;
  padding: 10px;
}
.md-top a {
  text-decoration: none;
  color: #333;
}
.md-bottom a {
  text-decoration: none;
  color: #333;
  border: 1px solid #333;
  margin: 10px;
  padding: 5px;
}
</style>
