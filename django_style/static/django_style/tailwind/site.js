((callback) => {
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", callback);
  } else {
    callback();
  }
})(() => {
  document.querySelectorAll("[data-toggle]").forEach((el) => {
    el.addEventListener("click", (e) => {
      e.preventDefault();
      const targetName = el.getAttribute("data-toggle");
      document.querySelectorAll(`[data-name="${targetName}"]`).forEach((target) => {
        target.classList.toggle("hidden");
      });
    });
  });
});
