<template>
  <div id="app">
    <Header />
     <b-container fluid="sm">
      <b-card title="Lista Todo">
        <TodoForm v-bind:todos="todos"/>
      </b-card>
      <b-card>
        <b-list-group flush v-for="todo in todos" :key="todo.id">
          <TodoItem v-bind:todo="todo" v-on:del-todo="deleteTodo" v-on:up-todo="updateTodo"/>
        </b-list-group>
      </b-card>
    </b-container>
    <!-- <div id="nav">
     <router-link :to="{ name: 'home' }">Vue</router-link> |
     <router-link :to="{ name: 'messages' }">Django Rest</router-link>
    </div>
    <router-view/> -->
  </div>
</template>

<script>
import axios from "axios";

import Header from "./components/Header";
import TodoForm from "./components/TodoForm.vue";
import TodoItem from "./components/TodoItem.vue";


export default {
  name: "App",
  components: {
    Header,
    TodoForm,
    TodoItem
  },
  methods: {
    deleteTodo(id){
      axios
        .delete(`http://localhost:8000/api/v1/${id}/`)
        .then(() => this.todos = this.todos.filter(todo => todo.id !== id))
        // eslint-disable-next-line no-console
        .catch(err => console.log(err));
    },
    updateTodo(id, completed,name){
      axios
        .put(`http://localhost:8000/api/v1/${id}/`,{
          name,
          completed
        })
        // eslint-disable-next-line no-console
        .catch(err => console.log(err));
    }
  },
  data() {
    return {
      todos: [],
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/api/v1/")
      .then((res) => res.data.forEach((dataItem) => this.todos.push(dataItem)))
      // eslint-disable-next-line no-console
      .catch((err) => console.log(err));
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#app .container-sm {
  max-width: 750px;
}

.card-title {
  font-size: 2rem;
}
.card:last-child {
  margin-top: 3vh;
}
.card:last-child .card-body {
  padding: 0;
}
.card:last-child .list-group-item {
  border-bottom: 1px solid #dfdfdf !important;
}
</style>
