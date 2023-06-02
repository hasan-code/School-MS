// Get all the menu elements
const menuItems = document.querySelectorAll(".menu-wrapper");

// Attach click event listener to each menu element
menuItems.forEach((menuItem) => {
  menuItem.addEventListener("click", toggleSubmenu);
});

// Function to toggle the submenu
function toggleSubmenu(event) {
  // Prevent the default action of the link
  event.preventDefault();

  // Get the corresponding submenu and moreIcon element
  const submenu = this.querySelector(".submenu");

  const moreIcon = this.querySelector(".more");

  // Toggle the display of the submenu
  submenu.style.display = submenu.style.display === "flex" ? "none" : "flex";

  moreIcon.style.transform =
    moreIcon.style.transform === "rotate(180deg)"
      ? "rotate(0deg)"
      : "rotate(180deg)";
}
