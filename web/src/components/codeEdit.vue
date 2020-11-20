<template>
  <codemirror
      v-model="item"
      :options="cmOption"
      class="code-mirror"
      @ready="onCmReady3"
      @focus="onCmFocus"
      @input="onCmCodeChange"
      ref="myCmGenerate">
  </codemirror>
</template>

<script>
import { codemirror } from 'vue-codemirror'
import 'codemirror/mode/javascript/javascript.js'
import '../assets/js/setting'

export default {
  data(){
    return{
      item: '',
      cmOption: {
        tabSize: 2, // tab
        styleActiveLine: true, // 高亮选中行
        lineNumbers: true, // 显示行号
        styleSelectedText: true,
        line: true,
        foldGutter: true, // 块槽
        gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter'],
        highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: true }, // 可以启用该选项来突出显示当前选中的内容的所有实例
        mode: { // 模式, 可查看 codemirror/mode 中的所有模式
          name: 'javascript',
          json: true
        },
        // hint.js options
        hintOptions: {
        // 当匹配只有一项的时候是否自动补全
          completeSingle: false
        },
        // 快捷键 可提供三种模式 sublime、emacs、vim
        keyMap: 'sublime',
        matchBrackets: true,
        showCursorWhenSelecting: true,
        theme: 'monokai', // 主题
        extraKeys: { 'Ctrl': 'autocomplete' } // 可以用于为编辑器指定额外的键绑定，以及keyMap定义的键绑定
      }
    }
  },
  methods: {
    onCmReady3() {
      this.$refs.myCmGenerate.codemirror.setSize('400px', '400px')
    },
    onCmFocus(instance, event) {
      console.log(instance)
      console.log(event)
    },
    onCmCodeChange(instance, obj) {
      console.log(instance)
      console.log(obj)
    }
  }
}
</script>

<style>
.CodeMirror-scroll {
  overflow: scroll !important;
  margin-bottom: 0;
  margin-right: 0;
  padding-bottom: 0;
  height: 100%;
  outline: none;
  position: relative;
  border: 1px solid #dddddd;
}
</style>
<style lang="less" scoped>
.code-mirror{
  font-size : 13px;
  line-height : 150%;
  text-align: left;
}
</style>
