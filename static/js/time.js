// Time
function time() {
  const hr = document.querySelector(".hour");
  const min = document.querySelector(".minute");
  const sec = document.querySelector(".second");

  const d = new Date();
  let hour = d.getHours();
  let minute = d.getMinutes();
  let second = d.getSeconds();

  hour < 10 ? (hr.innerHTML = "0" + hour) : (hr.innerHTML = hour);
  minute < 10 ? (min.innerHTML = "0" + minute) : (min.innerHTML = minute);
  second < 10 ? (sec.innerHTML = "0" + second) : (sec.innerHTML = second);
}
var interval = setInterval(time, 1000);
