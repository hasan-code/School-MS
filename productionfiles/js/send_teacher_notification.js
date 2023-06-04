// Get the file input element
const fileInput = document.getElementById("file-input");
const attachFile = document.getElementById("attach-file");

const colorContainer = document.getElementById("color-container");
const textColor = document.getElementById("text-color");

// Text styles
const boldText = document.getElementById("bold-text");
const italicText = document.getElementById("italic-text");
const underlineText = document.getElementById("underline-text");
const leftAlign = document.getElementById("left-align-text");
const centerAlign = document.getElementById("center-align-text");
const rightAlign = document.getElementById("right-align-text");
const justifyAlign = document.getElementById("justify-align-text");

// Text colors
const redColor = document.getElementById("red");
const greenColor = document.getElementById("green");
const yellowColor = document.getElementById("yellow");
const blueColor = document.getElementById("blue");
const orangeColor = document.getElementById("orange");

const textArea = document.querySelector("textarea");
const deleteMessageIcon = document.getElementById("delete-message");

boldText.addEventListener("click", () => {
  textArea.classList.toggle("bold-text-active");
});

italicText.addEventListener("click", () => {
  textArea.classList.toggle("italic-text-active");
});

underlineText.addEventListener("click", () => {
  textArea.classList.toggle("underline-text-active");
});

leftAlign.addEventListener("click", () => {
  textArea.classList.toggle("left-align-text-active");
});

centerAlign.addEventListener("click", () => {
  textArea.classList.toggle("center-align-text-active");
});

rightAlign.addEventListener("click", () => {
  textArea.classList.toggle("right-align-text-active");
});

justifyAlign.addEventListener("click", () => {
  textArea.classList.toggle("justify-align-text-active");
});

// Add a click event listener to the change Color of the TextArea
textColor.addEventListener("click", () => {
  colorContainer.classList.toggle("toggle-color-container");
});

// window.addEventListener("click", (event) => {
//     if (event.target == colorContainer) {
//         colorContainer.classList.toggle("toggle-color-container");
//     }
// });

redColor.addEventListener("click", () => {
  textArea.style.color = "#ff0000";
});

greenColor.addEventListener("click", () => {
  textArea.style.color = "#00d300";
});

yellowColor.addEventListener("click", () => {
  textArea.style.color = "#fff200";
});

blueColor.addEventListener("click", () => {
  textArea.style.color = "#6969ff";
});

orangeColor.addEventListener("click", () => {
  textArea.style.color = "#ffbb00";
});

// Add a click event listener to the button
attachFile.addEventListener("click", () => {
  fileInput.click(); // Simulate a click on the file input element
});

// Add an event listener to the file input element
fileInput.addEventListener("change", handleFileSelect, false);

// Function to handle the file selection
function handleFileSelect(event) {
  const file = event.target.files[0]; // Get the selected file

  if (file) {
    const reader = new FileReader();

    // Add an event listener to the FileReader instance
    reader.addEventListener("load", handleFileLoad, false);

    // Read the file as text or perform any required operations
    // Here, we're reading the file as text, but you can also use readAsDataURL for images, etc.
    reader.readAsText(file);
  }
}

// Function to handle the file load
function handleFileLoad(event) {
  const fileContent = event.target.result; // Get the file content

  // Perform any operations with the file content
  console.log(fileContent);
  // ...rest of your code
}

// Delete message on clicking the delete message icon
deleteMessageIcon.addEventListener("click", () => {
  textArea.value = "";
});

// EMAIL SUGGESTIONS MODAL
const emailInput = document.getElementById("receiver");
const suggestionsModal = document.getElementById("email-suggestions-modal");
// const suggestionsList = document.getElementById("suggestions-list");
const emailLists = document.querySelectorAll(".emails");

emailInput.addEventListener("input", function () {
  const inputText = emailInput.value.toLowerCase();

  for (let i = 0; i < emailLists.length; i++) {
    const email = emailLists[i].textContent.toLowerCase();

    if (email.includes(inputText)) {
      suggestionsModal.style.display = "block";
      emailLists[i].style.display = "";
    } else {
      suggestionsModal.style.display = "none";
      emailLists[i].style.display = "none";
    }
  }
});

// Add click event listener to each filtered email item
for (let i = 0; i < emailLists.length; i++) {
  emailLists[i].addEventListener("click", function () {
    const selectedEmail = emailLists[i].textContent;
    emailInput.value = selectedEmail;
  });
}
