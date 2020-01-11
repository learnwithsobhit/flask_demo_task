import Vue from 'vue';
import Router from 'vue-router';
import TaskDashboard from '../components/TaskDashboard.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/dashboard',
      name: 'Tasks',
      component: TaskDashboard,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
