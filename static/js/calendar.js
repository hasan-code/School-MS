// CALENADR
const date = new Date();

let current_year = date.getFullYear();
let today_date = date.getDate();
let today_day = date.getDay();

const isLeapYear = (year) => {
  return (
    (year % 4 === 0 && year % 100 !== 0 && year % 400 !== 0) ||
    (year % 100 === 0 && year % 400 === 0)
  );
};
const getFebDays = (year) => {
  return isLeapYear(year) ? 29 : 28;
};

let days_of_month = [
  31,
  getFebDays(current_year),
  31,
  30,
  31,
  30,
  31,
  31,
  30,
  31,
  30,
  31,
];

const month_names = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

// const week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

let calendarMonth = document.querySelector("#month");
let calendarYear = document.querySelector("#year");

calendarMonth.innerHTML = `${month_names[date.getMonth()]}`;
calendarYear.innerHTML = date.getFullYear();

let day = document.querySelectorAll(".day");
let dateDiv = document.querySelectorAll(".date-div");

for (let i = 0; i < dateDiv.length; i++) {
  let weekday_date = today_date - today_day + i;
  if (weekday_date >= 1 && weekday_date <= days_of_month[date.getMonth()]) {
    day[today_day].classList.add("active-day");
    dateDiv[today_day].classList.add("active-date");
    if (weekday_date == 0) {
      dateDiv[i].style.backgroundColor = "#ff7070";
      dateDiv[i].style.boxShadow =
        "rgba(255, 112, 112, 0.5) 0px 13px 27px -5px, rgba(255, 112, 112, 0.35) 0px 8px 16px -8px";
    }
    if (weekday_date < 10) {
      dateDiv[i].innerHTML = "0" + weekday_date;
    } else {
      dateDiv[i].innerHTML = weekday_date;
    }
  } else {
    dateDiv[i].innerHTML = "  ";
  }
}
