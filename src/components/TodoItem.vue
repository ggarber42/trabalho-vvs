<template>
  <b-list-group-item>
    <input
      type="checkbox"
      v-on:change="$emit('up-todo', todo.id, !todo.completed, todo.name)"
      v-bind:checked="todo.completed"
    />
    {{ todo.name }}
    <b-button variant="danger" @click="$emit('del-todo', todo.id)" class="del"
      >x</b-button
    >
  </b-list-group-item>
</template>

<script>
export default {
  name: "TodoItem",
  props: ["todo"],
};
</script>

<style >
.btn-danger {
  padding: 0.1em 0.3em !important;
}
</style>