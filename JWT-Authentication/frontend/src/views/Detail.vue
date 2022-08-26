<template>
  <div class="Detail">
    <div v-if="!articleNotFound">
      <article>
        <h1>{{article.title}}</h1>
        <div>{{article.content}}</div>
      </article>
      <div v-if="$store.state.isAuthenticated">
        <hr class="my-4">

        <div v-if="errorDelete" class="alert alert-danger">
          Something went wrong.
        </div>

        <button class="btn btn-warning mr-1" @click="edit=!edit">Edit</button>
        <button class="btn btn-danger" @click="doRemove">Remove</button>

        <div v-if="errorEdit" class="alert alert-danger">
          Something went wrong.
        </div>
        <form @submit.prevent="doEdit" class="pb-5" v-if="edit">
          <hr class="my-4">
          <div class="form-group">
            <label for="TitleInput">Title</label>
            <input type="text" class="form-control" id="TitleInput" v-model="title">
          </div>
          <div class="form-group">
            <label for="ContentInput">Content</label>
            <textarea class="form-control" id="ContentInput" rows="9" v-model="content"></textarea>
          </div>
          <button class="btn btn-warning">Edit</button>
        </form>

      </div>
    </div>
    <div v-else class="alert alert-warning">
      Article not found
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Detail',
  data() {
    return {
      article: {},
      title: "",
      description: "",
      content: "",
      edit: false,
      articleNotFound: false,
      errorEdit: false,
      errorDelete: false
    }
  },
  mounted() {
    axios
      .get(`/api/articles/${this.$route.params.slug}/`)
      .then(response => {
        this.article = response.data

        this.title       = this.article.title
        this.content     = this.article.content
      })
      .catch(e => {
        this.articleNotFound = true
      })
  },
  methods: {
    doEdit() {
      this.$store.dispatch("onStart")
      let article = {
        title: this.title,
        slug: this.title.replaceAll(" ", "-").toLowerCase(),
        content: this.content,
        status:true,
        author:this.$store.state.user_id
      }
      axios
        .put(`/api/articles/${this.$route.params.slug}/`, article)
        .then(response => {
          this.article = article
          this.edit = false
          this.$router.push(`/article/${article.slug}`)
        })
        .catch(error => {
          this.errorEdit = true
        })

    },
    doRemove() {
      this.$store.dispatch("onStart")
      axios
        .delete(`/api/articles/${this.$route.params.slug}/`)
        .then(response => {
          this.$router.push(`/`)
        })
        .catch(error => {
          this.errorDelete = true
        })
      this.$router.push("/")
    }
  }
}
</script>
