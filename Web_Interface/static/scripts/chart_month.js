var ctx2 = document.getElementById('myChart_Month').getContext('2d');
var options = {
  type: 'line',
  data: {
    labels: ['Week 4','Week 3','Past Week','This Week'],
    datasets: [

	    {
	      label: 'Misc',
	      data: [500,  50, 260, 770],
        backgroundColor: ['rgba(255, 99, 132, 0.2)'],
      	borderWidth: 1
    	},
			{
				label: 'Food',
				data: [890, 840, 590, 450],
        backgroundColor: ['rgba(255, 206, 86, 0.2)'],
				borderWidth: 1
			},
			{
				label: 'Shopping',
				data: [3060, 710, 400, 430],
        backgroundColor: ['rgba(153, 102, 255, 0.2)'],
				borderWidth: 1
			},
			{
				label: 'Medicals',
				data: [228,  56, 211, 160],
        backgroundColor: ['rgba(54, 162, 235, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Travel',
				data: [108, 207, 257, 196],
        backgroundColor: ['rgba(255, 0, 0, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Banking Ins',
				data: [0, 0, 0, 1500],
        backgroundColor: ['rgba(75, 192, 192, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'GovtPubBills',
				data: [150, 0, 200, 0],
        backgroundColor: ['rgba(255, 159, 64, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Ration',
				data: [700, 1200, 450, 550],
        backgroundColor: ['rgb(0, 255, 0, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Recharge',
				data: [67, 550, 0, 30],
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