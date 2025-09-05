document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("theme-toggle");
  const body = document.body;

  // Load saved theme
  if (localStorage.getItem("theme") === "dark") {
    body.classList.add("dark-mode");
    toggleBtn.textContent = "☀️";
  }

  // Toggle button click
  toggleBtn.addEventListener("click", () => {
    body.classList.toggle("dark-mode");

    if (body.classList.contains("dark-mode")) {
      toggleBtn.textContent = "☀️"; // light mode icon
      localStorage.setItem("theme", "dark");
    } else {
      toggleBtn.textContent = "🌙"; // dark mode icon
      localStorage.setItem("theme", "light");
    }
  });
});
