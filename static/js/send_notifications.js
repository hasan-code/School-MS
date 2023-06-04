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

// OPEN AND CLOSE "SEND NOTIFICATION MODAL"
const openNotificationModal = document.querySelectorAll(".open-notification-modal");
const sendNotificationModal = document.getElementById("sendNotificationModal");
openNotificationModal.forEach((modal) => {
  modal.addEventListener("click", () => {
    sendNotificationModal.classList.toggle("active");
  });
});

window.addEventListener("click", (e) => {
  if (e.target == sendNotificationModal) {
    sendNotificationModal.classList.toggle("active");
  }
});
