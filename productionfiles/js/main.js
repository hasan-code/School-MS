// SIDEBAR JS
const menu = document.querySelector(".menu");
// const hamburgerIcon = document.getElementById("hamburger");
// const crossIcon = document.getElementById("cross");
const bodyContainer = document.querySelector(".body-container");
const body = document.querySelector("body");

menu.addEventListener("click", () => {
  body.classList.toggle("active");
  bodyContainer.classList.toggle("active");
  // menu.classList.toggle("active");

  // if (crossIcon.style.display === "none") {
  //   crossIcon.style.display = "block";
  // }

  // if (hamburgerIcon.style.display === "block") {
  //   hamburgerIcon.style.display = "none";
  // }
});

// Profile Modal

const openModal = document.getElementById("ProfileModal");

const profile = document.getElementById("pofile");

const closeModel = document.getElementById("cross");

profile.addEventListener("click", () => {
  openModal.classList.toggle("active");
});

closeModel.addEventListener("click", () => {
  openModal.classList.toggle("active");
});

// function closeModal(event) {
//   if (event.target === profileModal) {
//     profileModal.classList.toggle("active");
//   }
// }

// document.addEventListener("click", closeModal);
