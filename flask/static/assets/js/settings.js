const messagesApp = {
  messageSelector: ".flash-message",
  messageElList: [],
  init() {
    this.messageElList = Array.from(
      document.querySelectorAll(this.messageSelector)
    );

    toastr.options = {
      closeButton: false,
      debug: false,
      newestOnTop: true,
      progressBar: true,
      positionClass: "toast-top-right",
      preventDuplicates: false,
      onclick: null,
      showDuration: "300",
      hideDuration: "1000",
      timeOut: "10000",
      extendedTimeOut: "1000",
      showEasing: "swing",
      hideEasing: "linear",
      showMethod: "fadeIn",
      hideMethod: "fadeOut",
    };

    this.messageElList.forEach((el) => {
      toastr[el.dataset.type](el.dataset.message);
    });
  },
};

document.addEventListener("DOMContentLoaded", () => {
  messagesApp.init();
});
