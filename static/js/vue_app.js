window.onload = function () {
  Vue.component('result-item', {
    props: ['rslt'],
    template: `<li>
                <p>元のテキスト: <span class="former">{{ rslt.former_text }}</span></p>
                <p>形態素解析後: <span class="tokenized">{{ rslt.tokenized_text }}</span></p>
              </li>`
  });

  app = new Vue({
    el: '#app',
    data: {
      results: [],
    }
  });
}
