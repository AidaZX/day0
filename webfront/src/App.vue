/* eslint-disable */
<template>
  <div id="app">
    <el-table
      :data="tableDataSource"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="Name"
        width="180">
      </el-table-column>
      <el-table-column
        prop="file_type"
        label="Type"
        width="180">
      </el-table-column>
      <el-table-column
        prop="size"
        label="Size">
      </el-table-column>
      <el-table-column
      fixed="right"
      width="120">
      <template slot-scope="scope">
        <el-button
          @click="deleteRow(scope.$index,scope.row)"
          type="text"
          size="small">
          Delete
        </el-button>
      </template>
      </el-table-column>
    </el-table>
    <el-upload
      class="upload-demo"
      :data="file_detail"
      :before-upload="beforeUpload"
      :on-success = "onSuccess"
      drag
      action="http://localhost:8000/api/posts/"
      multiple>
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">Drag or Drop File Here，or<em> chick here </em>to open a file browser</div>
    </el-upload>

  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'App',
  data() {
    return{
      tableDataSource : [],
      file_detail:{
      }

    }
  },
  created() {
    this.get_file_list();
  },
  methods:{
    onSuccess(){
      location.reload();
      this.get_file_list();
    },
    get_file_list(){
        console.log("hello");
        this.$http.get('http://localhost:8000/api/posts/').then((res) => {
        this.tableDataSource = res.body
        console.log(this.tableDataSource)});
    },
    deleteRow(index,data){
      let id = data.id;
      this.$http.delete(`http://localhost:8000/api/posts/${id}`).then((res) => {
        console.log(this.res);
        location.reload();
        });
    },
    beforeUpload(param){
      this.file_detail.file_type = param.type;
      this.file_detail.size = param.size;
      this.file_detail.name = param.name;
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
</style>
