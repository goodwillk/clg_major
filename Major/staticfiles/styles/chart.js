const data1 = {
   labels: [
      'Red',
      'Green',
      'Yellow',
      'Grey',
      'Blue'
   ],
   datasets: [{
      label: 'My First Dataset',
      data: [11, 16, 7, 3, 14],
      backgroundColor: [
         'rgb(255, 99, 132)',
         'rgb(75, 192, 192)',
         'rgb(255, 205, 86)',
         'rgb(201, 203, 207)',
         'rgb(54, 162, 235)'
      ]
   }]
};
const config0 = {
   type: 'line',
   data: data1,
   options: {}
};
const config1 = {
   type: 'polarArea',
   data: data1,
   options: {}
};
const config2 = {
   type: 'radar',
   data: data1,
   options: {
      elements: {
         line: {
            borderWidth: 3
         }
      }
   },
};
const config3 = {
   type: 'bar',
   data: data1,
   options: {
      responsive: true,
      plugins: {
         legend: {
            position: 'top',
         },
         title: {
            display: true,
            text: 'Chart.js Bar Chart'
         }
      }
   },
};