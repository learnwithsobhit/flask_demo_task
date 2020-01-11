<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <h1>Assignee: Elam</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>Add Task</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Task</th>
              <th scope="col">Status</th>
              <th scope="col">Deadline</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in tasks" :key="index">
              <td>
                <li style="float:left;">
                <a class="text-link" href="#">
                          {{ item.task }}
                </a>
                </li>
              </td>
              <td>{{ item.status }}</td>
              <td>{{ item.deadline }}</td>
              <!-- <td>
                <span v-if="Task.read">Yes</span>
                <span v-else>No</span>
              </td> -->
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addTaskModal"
            id="task-modal"
            title="Add a new task"
            hide-footer
            hide-backdrop
            content-class="shadow">
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-task-title-group"
                    label="Task:"
                    label-for="form-task-title-input">
          <b-form-input id="form-task-title-input"
                        type="text"
                        v-model="addTaskForm.task"
                        required
                        placeholder="Enter Task Title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-status-group"
                      label="Status:"
                      label-for="form-status-input">
            <b-form-input id="form-status-input"
                          type="text"
                          v-model="addTaskForm.status"
                          required
                          placeholder="Enter status">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-time-group"
                      label="Deadline:"
                      label-for="form-time-input">
            <b-form-input id="form-time-input"
                          type="text"
                          v-model="addTaskForm.deadline"
                          required
                          placeholder="Enter deadline">
            </b-form-input>
          </b-form-group>
        <!-- <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addTaskForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group> -->
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      tasks: [],
      addTaskForm: {
        task: '',
        status: '',
        deadline: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
            console.error(error);
        });
    },
    addTask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'New Task added at the end!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
            console.log(error);
          this.getTasks();
        });
    },
    initForm() {
      this.addTaskForm.task = '';
      this.addTaskForm.status = '';
      this.addTaskForm.deadline = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      // let read = false;
      // if (this.addTaskForm.read[0]) read = true;
      const payload = {
        task: this.addTaskForm.task,
        status: this.addTaskForm.status,
        deadline: this.addTaskForm.deadline, // property shorthand
      };
      this.addTask(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
