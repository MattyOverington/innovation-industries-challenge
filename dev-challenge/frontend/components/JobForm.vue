<template>
  <v-card>
    <v-card-title> Add Job </v-card-title>
    <v-card-text>
      <v-text-field v-model="job.client" label="Client" />
      <v-text-field v-model="job.description" label="Job Description" />
      <v-text-field v-model.number="job.cost" label="Estimated Cost" />
      <v-select v-model.number="job.lead" :items="job.employeeIDs" label="Project Lead"></v-select>
    </v-card-text>
    <v-card-actions>
      <v-btn :disabled="lock" @click="addJob()" color="primary">Save</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ['job_id'],
  created() {
    this.maybeModifyJob(this.job_id)
  },
  data() {
    return {
      job: {},
      lock: false,
    }
  },
  methods: {
    async addJob() {
      this.lock = true
      await this.$axios.$post('/job/job', this.job)
      this.lock = false
      this.job = {}
      this.$emit('save')
    },
    async maybeModifyJob(id) {
      if (!id) this.job = await this.$axios.$get('/job/jobs', { params: { id } })
    }
  },
}
</script>

<style></style>
