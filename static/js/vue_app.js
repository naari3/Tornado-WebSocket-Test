window.onload = function () {
  Vue.component('result-item', {
    props: ['rslt'],
    template: `<li>
                <p><span class="tokenized">{{ rslt.text }}</span></p>
              </li>`
  });

  app = new Vue({
    el: '#app',
    data: {
      tokenizing: false,
      results: [],
    }
  });
}
