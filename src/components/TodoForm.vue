<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset">
     <b-form-input v-model="name" placeholder="Adicione um item"></b-form-input>
       <b-button type="submit" variant="primary">Enviar</b-button>
      <b-button type="reset" variant="secondary">Limpar</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data(){
    return{
      name: ''
    }
  },
  props: ["todos"],
  methods: {
    onSubmit(e){
      e.preventDefault();
      axios
        .post('http://localhost:8000/api/v1/',{
          name: this.name
        })
        .then(res => this.todos.push(res.data))
        // eslint-disable-next-line no-console
        .catch(err => console.log(err))
        .finally(() => this.name = '');
    },
    onReset(e){
      e.preventDefault();
      this.name = '';
    }
  }
};
</script>

<style>
button.btn{
    margin: 1em;
}
</style>