// This function filters out the leave application when the user types in the search input field.
function searchApplication() {
    let searchInputField, filter, table, tr, td, inputTxt;
    searchInputField = document.getElementById("search-application");
    filter = searchInputField.value.toUpperCase();
    table = document.getElementById("leaveApplicationTable");
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