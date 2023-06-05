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

// OPEN & CLOSE "VIEW ALL SENT NOTIFICATIONS" MODAL OF TEACHERS & STUDENTS
const viewAllTeacherNotificationsBtn = document.getElementById(
  "viewAllTeacherNotifications"
);
const viewAllTeacherNotificationsModal = document.getElementById(
  "all-notifications-teacher-modal"
);

const viewAllStudentNotificationsBtn = document.getElementById(
  "viewAllStudentNotifications"
);
const viewAllStudentNotificationsModal = document.getElementById(
  "all-notifications-student-modal"
);

viewAllTeacherNotificationsBtn.addEventListener("click", () => {
  viewAllTeacherNotificationsModal.classList.toggle("active");
});

viewAllStudentNotificationsBtn.addEventListener("click", () => {
  viewAllStudentNotificationsModal.classList.toggle("active");
});
