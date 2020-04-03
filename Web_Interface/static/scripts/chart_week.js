var ctx2 = document.getElementById('myChart_Week').getContext('2d');
var options = {
  type: 'line',
  data: {
    labels: ['29-03-2020','30-03-2020','31-03-2020','01-04-2020','02-04-2020','03-04-2020','04-04-2020',],
    datasets: [

	    {
	      label: 'Misc',
	      data: [250, 0, 100, 60, 100, 30, 50],
        backgroundColor: ['rgba(255, 99, 132, 0.2)'],
      	borderWidth: 1
    	},
			{
				label: 'Food',
				data: [450, 1000, 590, 1200, 300, 200, 145],
        backgroundColor: ['rgba(255, 206, 86, 0.2)'],
				borderWidth: 1
			},
			{
				label: 'Shopping',
				data: [0,1500,0,0,300,0,250],
        backgroundColor: ['rgba(153, 102, 255, 0.2)'],
				borderWidth: 1
			},
			{
				label: 'Medicals',
				data: [170, 0, 120, 0, 0, 100, 0],
        backgroundColor: ['rgba(54, 162, 235, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Travel',
				data: [70, 90, 120, 0, 25, 100, 0],
        backgroundColor: ['rgba(255, 0, 0, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Banking Ins',
				data: [0, 0, 0, 0, 0, 0, 1500],
        backgroundColor: ['rgba(75, 192, 192, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'GovtPubBills',
				data: [150, 0, 0, 0, 200, 0, 120],
        backgroundColor: ['rgba(255, 159, 64, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Ration',
				data: [700, 0, 1200, 0, 450, 0, 0],
        backgroundColor: ['rgb(0, 255, 0, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Recharge',
				data: [67, 550, 0, 30, 0, 50, 0],
        backgroundColor: ['rgb(255, 255, 128, 0.2)'],
				borderWidth: 1
			}
		]
  },
  options: {
    scales: { yAxes: [{
              scaleLabel: {
                      display: true,
                      labelString: 'Expense Amount',
                      fontSize: 23
              },
              ticks: {
                reverse: false
                  }
              }],
              xAxes: [{
                        scaleLabel: {
                                display: true,
                                labelString: 'Timeline',
                                fontSize: 23
                        }
                      }]
            },
    legend: {display: true,
              position: 'top',
              labels: {
                  fontSize: 15,
                  boxWidth: 50
              }
            }
  },

}
var myLineChart = new Chart(ctx2, options);