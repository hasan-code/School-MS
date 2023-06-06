// This function filter out the notifications while user type in the input field
function searchNotification() {
  var input = document.getElementById("inputTxt").value.toLowerCase();
  var notifications = document.getElementsByClassName("notifications");

  for (var i = 0; i < notifications.length; i++) {
    var messageBox = notifications[i].getElementsByClassName("message-box")[0];
    var message = messageBox.getElementsByClassName("message")[0];
    var senderName = messageBox.getElementsByClassName("sender-name")[0];

    var messageText = message.textContent || message.innerText;
    var senderNameText = senderName.textContent || senderName.innerText;

    if (
      messageText.toLowerCase().indexOf(input) > -1 ||
      senderNameText.toLowerCase().indexOf(input) > -1
    ) {
      notifications[i].style.display = "";
    } else {
      notifications[i].style.display = "none";
    }
  }
}
