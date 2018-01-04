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
        
        <ul>
          <li v-for='item in news_list' class ="news">
            <a v-bind:href='item.href'><span v-text='item.title'></span></a>&nbsp;&nbsp;&nbsp;&nbsp;
            <span v-text='item.time'></span>
          </li>
        </ul>
   
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
      news_list: []
    }
  },
  mounted: function () {
    this.showNews()
  },
  methods: {
    showNews () {
      this.$http.get('http://127.0.0.1:8080/initDemo/get_news')
      .then((response) => {
        var res = response.data
        console.log(res)
        this.news_list = JSON.parse(res['list'])
      })
    }
  }
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
.news{
  overflow:auto;  
}
</style>
