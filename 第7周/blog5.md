| 软件工程 | [点我](https://edu.cnblogs.com/campus/gdgy/informationsecurity1812/) |
| :-----------------: | :---------------: |
| 作业要求 | [点我](https://edu.cnblogs.com/campus/gdgy/informationsecurity1812/homework/11162) |
| 作业目标 | 关于Alpah版本软件的项目报告 |
----

[toc]

# 一、项目文档和代码
## 1.1 博客相关链接汇总
- [团队展示和选题](https://www.cnblogs.com/blockchik/p/13849545.html)
- [需求规格说明](https://www.cnblogs.com/blockchik/p/13888209.html)
- [需求改进&系统设计](https://www.cnblogs.com/blockchik/p/13916494.html)
- [项目冲刺集合](https://www.cnblogs.com/blockchik/p/13971831.html)

## 1.2 GitHub仓库
[https://github.com/MrEdge123/Team-programming](https://github.com/MrEdge123/Team-programming)


# 二、Alpha版本测试报告

## 2.1 功能测试

### 2.1.1功能列表
|功能模块	|	具体功能介绍(应用场景)	|
|:--|:--|
|题目模块|**题目列表的展示**<br>用户可以在题目列表看到所有的编程题目的展示|
|	|**题目的查找**<br>	用户可以通过搜索快速定位题目|
|	|**题目的增加、修改、删除**<br>	管理员可以在题目编辑界面对题目进行增添，修改和删除|
|数据模块|	**数据列表**<br> 管理员点击编辑数据进入对应题目的数据列表|
|	|**数据的增加、修改、删除**<br>	管理员可以增添，修改删除对应题目的数据|
|用户模块|	**登陆注册**<br>用户使用账号密码登陆 ；若无账号，可以注册账号；若忘记密码，可以选择忘记密码进行验证并修改密码		|
|	|**用户信息管理**<br>用户修改密码 用户可以修改昵称，用户可以修改昵称	|
|测评模块|	**评测程序**<br>用户提交代码，返回判定结果	|
|	|**状态保存**<br> 用户点击状态列表，可以查看判定结果	|
|	|**重判题目**<br> 用户要求重判题目|
|比赛模块|	**管理比赛**<br>管理员新建一道或多道限时题目作为比赛题目|
||**实时榜单**<br>查看状态的实时结果|

### 2.1.2场景测试
#### 场景一
1. **背景**
1). 典型用户——学生小明
2). 假设在线测评系统已有练习的题库，且已完成用户系统功能。
2. **场景**  
**Step 1:**小明打开网站准备开始做题，首先他先`登录`网站，输入用户名和密码即登录成功；若没有账号可以`注册账号`后登陆。
**Step 2:**小明点击`状态查看`了之前的做题历史记录，然后点击`题目列表`，点击进入`题目详情`页进入练习界面开始练习。
**Step 3:**小明完成了一道题目后，点击`提交答案`，页面跳转至状态界面，并显示解题状态；

#### 场景二
1. **背景**
1). 典型用户——老师/管理员 
2). 假设在线测评系统已有练习的题库，且已完成用户系统功能。
2. **场景**  
**Step 1:**老师`登录网站`，通过后台授权得到账号，输入用户名和密码即登录成功，此外，由于权限不同，老师可以看到包含题目编辑的导航栏。
**Step 2:**老师点击`题目编辑`可以对题目进行修改，然后点击`新建题目`，进入添加题目添加界面。
**Step 3:**老师完成了一道题目的描述后，点击`添加`，页面跳转至题目编辑界面，完成该添加操作。
**Step 4:**老师想修改题目，点击`编辑图标`，页面跳转至题目编辑界面，完成该添加操作。
**Step 5:**老师想删除题目，点击`删除图标`，页面跳转至题目编辑界面，完成该添加操作。
**Step 6:**老师在`数据编辑`界面进行`数据添加`，点击`添加`，页面跳转至数据列表界面，完成该添加操作。
**Step 7:**老师在`数据编辑`界面进行`数据修改`，点击`修改图标`，页面跳转至数据列表界面，进行题目修改后点击`修改`完成该添加操作。
**Step 8:**老师在`数据编辑`界面进行`数据删除`，点击`删除图标`，页面跳转至数据列表界面，进行题目修改后点击`修改`完成该添加操作。

### 2.1.3测试结果

#### 用户模块
|功能测试	|	效果	|测试结果|
|:--|:--|:--|
|用户登陆|用户账号密码匹配，登录成功，账号错误提示未注册，密码不匹配提示密码错误 |成功|
|用户注册|输入格式判断，需要填入对应信息 |成功|
|用户退出登录|	注销登录	|成功|
|题目列表的展示|展示所有题目|成功|
|题目的查找|	用户可以通过搜索快速定位题目|成功|
|评测程序|提交代码，返回判定结果	|成功|
|状态保存|点击状态列表，可以查看判定结果	|成功|
|实时榜单|查看状态的实时结果|未实现|
|用户信息管理|用户修改密码 用户可以修改昵称，用户可以修改邮箱|未实现|
#### 管理员模块
|功能测试	|	效果	|测试结果|
|:--|:--|:--|
|题目的增加、修改、删除|管理员可以在题目编辑界面对题目进行增添，修改和删除|成功|
|数据列表| 管理员点击编辑数据进入对应题目的数据列表|成功|
|数据的增加、修改、删除|管理员可以增添，修改删除对应题目的数据|成功|
|管理比赛|管理员新建一道或多道限时题目作为比赛题目|未实现|


### 2.1.4Bug清单
1. **已经修复的Bug**
- 服务器切换终端后被停止：通过守护进程解决
- 提交代码API只有通过和答案错误两种状态，其他识别不了：在守护进程重定向错误流
- 跨域问题：通过设置samesite属性来解决
- 访问不了服务器的数据库：开放MySQL端口，阿里云安全规则和宝塔linux面板都要设置
- 前端后台的数据请求时数据格式不统一
- 登陆时不合法用户(没有在数据库内)也能登陆
- 用户新建数据后，没有展示在数据列表，但是在题目详情有展示
2. **现阶段还未修复的Bug**
- 在题目修改和数据修改部分，仅不修改的地方会修改为空

## 2.2 兼容性测试
 Chrome浏览器 、2345浏览器均能够成功使用
## 2.3 性能测试

## 2.5 出口条件
- 完成所有的测试类型
- 没有影响用户正常使用的 bug
- 通过压力测试，并且设计符合用户要求
- 没有 bug 或 bug 经过风险评估
- 通过交叉检查，非该代码开发人员测试通过
- 产品使用说明书或用户手册等已经完备

# 三、Alpha版本发布说明

## 3.1 发布地址

## 3.2 运行环境
 Chrome浏览器

## 3.3 安装教程
点击进入网址，无需安装
## 3.4 功能介绍
(1)**登录注册功能**
- **登陆界面**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121203557349-1740843977.png)

- **登陆实例**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121203639709-1776818902.png)

- **注册界面，填入相关信息即可注册**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121203815145-1730867113.png)

(2)**点击导航栏，查看题目列表**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121203843814-1857433645.png)


(3)**查看状态列表**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121203859279-1306051940.png)


(4)**查看题目详情**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121203930471-539717865.png)


(5)**问题模块**

- **点击问题编辑，进入问题编辑界面，可以修改，删除，新建问题**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121204002600-1281236721.png)

- **点击新建题目按钮，进入问题添加界面**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121204156524-493762382.png)



(6)**数据处理模块**
- **点击数据编辑，进入数据编辑界面，可以修改，删除，新建数据(例子)**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121204018894-1434972295.png)

- **点击新建题目按钮，进入问题添加界面**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121204416649-1175359978.png)


(7)**退出界面**
<br>
![](https://img2020.cnblogs.com/blog/2147899/202011/2147899-20201121204441094-1831151878.png)



## 3.5 系统已知问题
- 在代码提交处还未实现分页和编辑器效果
- 搜索功能还未完善