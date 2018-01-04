<template>
  <el-container>
    <el-header>
      <el-row>
        <el-col :span="24">
          <div class="grid-content bg-purple-dark"> 
            <span style="color:#F56C6C;left:20%">
                  Enchanting Info    
            </span>
          </div>
        </el-col>
      </el-row>
    </el-header>
    <el-container>
      <el-aside width="300px"></el-aside>
      <el-main>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" active-text-color="#F56C6C">
            <el-menu-item index="1">热点</el-menu-item>
            <el-menu-item index="2">财经</el-menu-item>
            <el-menu-item index="3">体育</el-menu-item>
            <el-menu-item index="4">猜你喜欢</el-menu-item>
        </el-menu>
       <!-- {% for news in news_list %}

          <a href = "{{news.getHref}}"> {{ news.getTitle }} </a> {{ news.getTime }}<br/><br/>

        {% endfor %}
        -->
        <!--
        <el-table :data="mylist" show-header="false" border >
          <el-table-column prop="title" style="align:center"></el-table-column>  
          <el-table-column prop="time" style="align:center"></el-table-column>         
        </el-table>
        -->
        <ul>
          <ul v-for='item in mylist'>
            <a href=""><span v-text='item.title'></span></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <span v-text='item.time'></span>
          </ul>
        </ul>


        <div id="app">
          <p>{{ message }}</p>
        </div>
        
      </el-main>
      <el-aside width="300px"></el-aside>
    </el-container>
    
  </el-container>

</template>

<script>
  export default {
    name: 'app',
    data () {
      return {
        message: 'Hello Vue.js!',
        mylist: [{title: 'wss', time: '2017-12-27'}, 
                 {title: 'wangshasha', time: '2017-12-28'}]
      }
    },
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.el-header{
  background-color:;
  color: #333;
  text-align: center;
  line-height: 60px;
} 
.el-main {
  background-color:;
  color: #333;
  text-align: center;
  line-height: 160px;
}

.el-aside {
  line-height: 260px;
  background-color: #FFFFFF;
}

</style>
