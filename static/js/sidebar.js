const settingsMenu = document.getElementById("settings-menu");
const settingsSubMenu = document.getElementById("settings-sub-menu");

settingsMenu.addEventListener("click", () => {
  settingsSubMenu.classList.toggle("active");
});

const attendanceMenu = document.getElementById("attendance-menu");
const attendanceSubMenu = document.getElementById("attendance-sub-menu");

attendanceMenu.addEventListener("click", () => {
  attendanceSubMenu.classList.toggle("active");
});

const notificationMenu = document.getElementById("notification-menu");
const notificationSubMenu = document.getElementById("notification-sub-menu");

notificationMenu.addEventListener("click", () => {
  notificationSubMenu.classList.toggle("active");
});

const applicationMenu = document.getElementById("application-menu");
const applicationSubMenu = document.getElementById("application-sub-menu");

applicationMenu.addEventListener("click", () => {
  applicationSubMenu.classList.toggle("active");
});

const salaryMenu = document.getElementById("salary-menu");
const salarySubMenu = document.getElementById("salary-sub-menu");

salaryMenu.addEventListener("click", () => {
  salarySubMenu.classList.toggle("active");
});
