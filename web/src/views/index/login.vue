<template>
    <div class="login">
        <div class="login-input">
            <el-form :model="ruleForm" :rules="rules" status-icon ref="ruleForm">
                <el-form-item class="username" label="用户名" prop="username">
                    <el-input v-model="ruleForm.username"></el-input>
                </el-form-item>
                <el-form-item class="petname" label="昵称" prop="petname">
                    <el-input v-model="ruleForm.petname"></el-input>
                </el-form-item>
                <el-form-item class="password" label="密码" prop="pass">
                    <el-input type="password" v-model="ruleForm.pass"></el-input>
                </el-form-item>
                <el-form-item class="checkPass" label="确认密码" prop="checkPass">
                    <el-input type="password" v-model="ruleForm.checkPass"></el-input>
                </el-form-item>
                <el-form-item class="email" label="邮箱" prop="email">
                    <el-input v-model="ruleForm.email"></el-input>
                </el-form-item>
                <el-button @click="submitForm('ruleForm')">注册</el-button>
            </el-form>
        </div>
    </div>
</template>

<script>
import {getRegisterMultidata} from '../../network/user'

export default {
    // created(){
    //     getRegisterMultidata().then(res => {
    //         console.log(res);
    //     })
    // },

    data(){
        var checkname = (rule, value, callback) => {
            if(!value){
                return callback(new Error('用户名不能为空'));
            }else{
                callback();
            }
        };
        var vaildatePass = (rule, value, callback) => {
            if(value === ''){
                return callback(new Error('请输入密码'));
            }else{
                if(this.ruleForm.checkPass !== ''){
                    this.$refs.ruleForm.validateField('checkPass');
                }
                callback();
            }
        };
        var vaildatePass2 = (rule, value, callback) => {
            if(value === ''){
                return callback(new Error('请再次输入密码'));
            }else if(value !== this.ruleForm.pass){
                callback(new Error('两次输入的密码不一致！'));
            }else{
                callback();
            }
        };
        var checkEmail = (rule, value, callback) => {
            var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");
            if(!value){
                return callback(new Error('邮箱不能为空'));
            }
            setTimeout(() => {
                if(!reg.test(value)){
                    callback(new Error('请输入正确的邮箱'));
                }else{
                    callback();
                }
            },1000);
        };
        return{
            ruleForm:{
                username: '',
                petname: '',
                pass: '',
                checkPass: '',
                email: ''
            },
            rules: {
                username: [
                    {validator: checkname, trigger: 'blur'}
                ],
                pass: [
                    {validator: vaildatePass, trigger: 'blur'}
                ],
                checkPass: [
                    {validator: vaildatePass2, trigger: 'blur'}
                ],
                email: [
                    {validator: checkEmail, trigger: 'blur'}
                ]
            }
        }
    },
    methods: {
        submitForm(formname){
            this.$refs[formname].validate((valid) => {
                if(valid){
                    alert('注册成功');
                    console.log(this.ruleForm);
                    getRegisterMultidata({
                        username: this.ruleForm.username,
                        name: this.ruleForm.petname,
                        password: this.ruleForm.pass,
                        email: this.ruleForm.email
                    }).then((res) => {
                        console.log(res);
                        this.$router.push('/signIn');
                    })
                }else{
                    alert('err');
                    return false;
                }
            });
        }
    }
}
</script>

<style>
.login{
    width: 100%;
    display: flex;
    justify-content: center;
    margin-top: 50px;
}
.login-input{
    width: 400px;
}


</style>
