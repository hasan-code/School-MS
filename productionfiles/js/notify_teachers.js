// This function filters out the teacher when the user types in the search input field.
function searchTeacher() {
  let searchInputField, filter, table, tr, td, inputTxt;
  searchInputField = document.getElementById("search-teacher");
  filter = searchInputField.value.toUpperCase();
  table = document.getElementById("teacherTable");
  tr = table.getElementsByTagName("tr");

  for (let i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
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

// OPEN & CLOSE "VIEW ALL SENT NOTIFICATIONS" MODAL OF TEACHERS & STUDENTS
const viewAllTeacherNotificationsBtn = document.getElementById(
  "viewAllTeacherNotifications"
);
const viewAllNotificationsModalContainer = document.getElementById(
  "all-notifications-modal-container"
);

const allNotificationsModal = document.getElementById(
  "all-notifications-modal"
);

viewAllTeacherNotificationsBtn.addEventListener("click", () => {
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
