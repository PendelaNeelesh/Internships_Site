<template>
  <div v-if="verifeidstatus && managerstatus" class="formdiv">
    <div class="form">
      <form class="formcontents" @submit.prevent="handlesubmit" >
        <label>Company: </label>
        <input type="text" v-model="getformdata.comp">
        <label>Email: </label>
        <input type="email" v-model="getformdata.email">
        <label>Title: </label>
        <input type="text" v-model="getformdata.title">
        <label>Type: </label>
        <input type="text"  v-model="getformdata.type">
        <label>Location: </label>
        <input type="text"  v-model="getformdata.loc">
        <label>Pay: </label>
        <input type="number"  v-model="getformdata.pay">
        <label>Description:</label>
        <textarea rows = "5" cols = "60" name = "description" v-model="getformdata.desc">
           
         </textarea>
         <label> ID:{{ getformdata.id }} </label>
        <div class="submit">
          <button>Modify Intern</button>
        </div>
      </form>
    </div>
  </div>
  <div v-else>
    Please login
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
    name: "Modify",
    data(){
      return {
        comp: "",
        email: "",
        loc: "",
        pay: 0,
        desc: "",
        title: "",
        type: "",
      }
    },
    computed: {
      ...mapGetters(['verifeidstatus']),
      ...mapGetters(['managerstatus']),
      ...mapGetters( ['getuser']),
      ...mapGetters( ['getformdata']),
    },
    methods: {
      handlesubmit(){
        var data = {
          comp: this.getformdata.comp,
          email: this.getformdata.email,
          loc: this.getformdata.loc,
          pay: this.getformdata.pay,
          desc: this.getformdata.desc,
          title: this.getformdata.title,
          type: this.getformdata.type,
	  id: this.getformdata.id,
          user: this.getuser
        }
        this.$store.dispatch("modifyintern",data)
      }
    },
}
</script>

<style scoped>
    .formdiv{
        background-image: url('../assets/background.jpg');
        width: inherit;
        height: inherit;
        display: flex;
        justify-content: center;
        align-items: center;
        
    }
    .form{
      width: 50%;
      min-height: 50%; 
      height: fit-content;
      background: white;
      border-radius: 15px;
      box-shadow: inset 0 0 2000px rgba(255, 255, 255, .5);
      opacity: 0.8;
      padding: 5px;
    }
    form{
      margin-right: 0px;
      width: 100%;
      text-align: left;
      padding: 40px;
    }
    label{
      color: black;
      display: inline-block;
      margin: 25px 0 15px;
      font-size: 0.6em;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-weight: bold;
      font-size: 15px;
    }
    input{
      display: block;
      padding: 10px 6px;
      width: 100%;
      box-sizing: border-box;
      border: none;
      border-bottom: 1px solid black;
      color: black;
      font-weight: bold;
    }
    button{
      background: rgb(26, 26, 182);
      border: 0px;
      padding: 10px 20px;
      margin-top: 20px;
      color: white;
      border-radius: 20px;
    }
    .submit{
      text-align: center;

    }
    textarea{
        margin-top: 5px;
    }
</style>
