// Line Chart
const ctx = document.getElementById("myChart");

new Chart(ctx, {
  type: "line",
  data: {
    labels: [
      "2014",
      "2015",
      "2016",
      "2017",
      "2018",
      "2019",
      "2020",
      "2021",
      "2022",
      "2023",
    ],
    datasets: [
      {
        label: "Total Students",
        data: [2, 3, 5, 3, 6, 4, 5, 2, 4, 7],
        borderWidth: 3,
        borderColor: "#8ec009",
        tension: 0.3,
      },
    ],
  },
  options: {
    legend: {
      display: false,
    },

    scales: {
      x: {
        grid: {
          display: false,
        },
      },
      y: {
        beginAtZero: true,
        grid: {
          display: false,
        },
      },
    },
  },
});
