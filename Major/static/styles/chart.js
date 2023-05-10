const data1 = {
   labels: [
      'Easy',
      'Medium',
      'Hard',
   ],
   datasets: [{
      label: 'Question',
      data: [11, 16, 4],
      backgroundColor: [
         'rgb(82, 243, 61)',
         'rgb(255, 205, 86)',
         'rgb(255, 0, 0)',


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