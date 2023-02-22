<template>
  <v-card>
    <v-breadcrumbs :items="breadcrumbs" divider="/"></v-breadcrumbs>
    <v-card-title>
      Job List <v-btn icon @click="dialog = true"><v-icon>mdi-plus</v-icon></v-btn></v-card-title
    >
    <v-data-table :headers="headers" :items="jobs">
      <template v-slot:item.delete="{ item }">
        <v-btn icon @click="deleteJob(item.id)"><v-icon>mdi-delete</v-icon></v-btn>
      </template>
      <template v-slot:item.modify="{ item }">
        <v-btn icon @click="setModifyJobID(item.id)"><v-icon>mdi-square-edit-outline</v-icon></v-btn>
      </template>
    </v-data-table>
    <v-dialog v-model="dialog">
      <job-form :job_id="this.modifyJobID ? this.modifyJobID : null"
        @save="
          dialog = false
          getJobs()
          setModifyJobID(0)
        "
      />
    </v-dialog>
    <v-card variant="tonal">Total Est. Job Cost: {{this.totalCost}}</v-card>
  </v-card>
</template>

<script>
import JobForm from '../components/JobForm.vue'
export default {
  components: { JobForm },
  created() {
    this.getJobs()
    this.getTotalCost()
    this.getEmployeeIDs()
    this.setModifyJobID(0)
  },

  data() {
    return {
      dialog: false,
      totalCost: 0,
      jobs: [],
      employeeIDS: [],
      breadcrumbs: [
        {
          title: 'Home',
          disabled: false,
          href: '/',
        },
        {
          title: 'Jobs',
          disabled: true,
          href: 'job',
        }
      ],
      modifyJobID: 0,
      headers: [
        { text: 'Client', value: 'client' },
        { text: 'Description', value: 'description' },
        { text: 'Completed', value: 'completed' },
        { text: 'Estimated Cost', value: 'cost' },
        { text: 'Job Lead', value: 'lead' },
        { text: 'Remove Job', value: 'delete'},
        { text: 'Modify Job', value: 'modify'}
      ],
    }
  },

  methods: {
    async getJobs() {
      this.jobs = await this.$axios.$get('/job/jobs')
      console.log(this.jobs)
    },
    async deleteJob(id) {
      await this.$axios.$delete('/job/job', { params: { id } })
      this.getJobs()
    },
    async getEmployeeIDs() {
      let employees = await this.$axios.$get('/employee/employees')
      this.employeeIDs = employees.map(employee => employee['id'])
      console.log(this.employeeIDs)
    },
    setModifyJobID(id) {
      this.modifyJobID = id;
    },
    getTotalCost() {
      let totalcost = 0
      this.jobs.forEach(job => {
        totalcost += job['cost']
      })
      this.totalCost = totalcost
    }
  },
}
</script>

<style></style>
