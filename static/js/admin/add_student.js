
// ADD STUDENT FORM MODAL
const modal = document.getElementById("AddStudent");
const overlay = document.getElementById("overlay");
const btn = document.getElementById("addStudentBtn");

btn.addEventListener("click", () => {
  modal.classList.add("open");
  overlay.classList.add("open");
});

window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.classList.remove("open");
    overlay.classList.remove("open");
  }
});

// SUCCESS DIALOG
const successAlertCloseBtn = document.getElementById("successAlertCloseBtn");
const successAlertDialog = document.getElementById("successAlert");

// successAlertCloseBtn.addEventListener("click", () => {
//   successAlertDialog.style.display = successAlertDialog.style.display === "flex" ? "none" : "flex";
// });

// ADD STUDENT FORM
let currentTab = 0;
showTab(currentTab);

function showTab(n) {
  const tab = document.getElementsByClassName("tab");
  tab[n].style.display = "block";
  tab[n].classList.toggle("active");

  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == tab.length - 1) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
}

function nextPrev(n) {
  const tab = document.getElementsByClassName("tab");
  // if (n == 1 && !validateForm()) return false;
  tab[currentTab].style.display = "none";
  currentTab = currentTab + n;

  if (currentTab >= tab.length) {
    document.getElementById("addStudentForm").submit();
    return false;
  }

  showTab(currentTab);
}
