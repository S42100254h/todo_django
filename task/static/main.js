const App = {
  data() {
    return {
      tasks: [],
    };
  },
  compilerOptions: {
    delimiters: ["[[", "]]"],
  },
  methods: {},
  created() {},
};

Vue.createApp(App).mount("#app");
