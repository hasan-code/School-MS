// This function filters out the student when the user types in the search input field.
function searchStudent() {
  let searchInputField, filter, table, tr, td, inputTxt;
  searchInputField = document.getElementById("search-student");
  filter = searchInputField.value.toUpperCase();
  table = document.getElementById("studentTable");
  tr = table.getElementsByTagName("tr");

  for (let i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      inputTxt = td.textContent || td.innerText;
      if (inputTxt.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

// OPEN & CLOSE "VIEW ALL SENT NOTIFICATIONS" MODAL OF STUDENTS
const viewAllStudentNotificationsBtn = document.getElementById(
  "viewAllStudentNotifications"
);
const viewAllNotificationsModalContainer = document.getElementById(
  "all-notifications-modal-container"
);

const allNotificationsModal = document.getElementById(
  "all-notifications-modal"
);

viewAllStudentNotificationsBtn.addEventListener("click", () => {
  viewAllNotificationsModalContainer.classList.toggle("active");
  allNotificationsModal.classList.toggle("active");
});

window.addEventListener("click", (e) => {
  if (
    e.target == viewAllNotificationsModalContainer &&
    e.target != allNotificationsModal
  ) {
    viewAllNotificationsModalContainer.classList.toggle("active");
    allNotificationsModal.classList.toggle("active");
  }
});
