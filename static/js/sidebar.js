const settingsMenu = document.getElementById("settings-menu");
const submenu = document.getElementById("sub-menu");

settingsMenu.addEventListener("click", () => {
    submenu.classList.toggle("active");
});