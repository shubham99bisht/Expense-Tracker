var ctx2 = document.getElementById('myChart_Year').getContext('2d');
var options = {
  type: 'line',
  data: {
    labels: ['May','June','July','Aug','Sept','Oct','Nov','Dec','Jan','Feb','March','April'],
    datasets: [

	    {
	      label: 'Misc',
	      data: [2900,  651, 2760,  530, 1469, 2361, 2549, 1993, 2956, 1165,  694, 1232],
        backgroundColor: ['rgba(255, 99, 132, 0.2)'],
      	borderWidth: 1
    	},
			{
				label: 'Food',
				data: [2862, 2516, 1700, 2301, 1459,  636, 1598, 2554, 2033,  816, 2704, 2677],
        backgroundColor: ['rgba(255, 206, 86, 0.2)'],
				borderWidth: 1
			},
			{
				label: 'Shopping',
				data: [2440, 2006,  573, 1943, 2106, 2115, 1475, 2631, 2149, 2511, 2076, 1098],
        backgroundColor: ['rgba(153, 102, 255, 0.2)'],
				borderWidth: 1
			},
			{
				label: 'Medicals',
				data: [2299, 1994, 1950, 1277,  578, 2053, 1278,  650, 2644, 1855, 1366, 1324],
        backgroundColor: ['rgba(54, 162, 235, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Travel',
				data: [1895, 1018, 1226, 1114, 1861, 1286, 1635, 2567,  732, 1678, 2249,  834],
        backgroundColor: ['rgba(255, 0, 0, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Banking Ins',
				data: [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500],
        backgroundColor: ['rgba(75, 192, 192, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'GovtPubBills',
				data: [1429, 1232, 1157,  567,  726,  512,  607,  721,  604, 1433,  827, 1155],
        backgroundColor: ['rgba(255, 159, 64, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Ration',
				data: [2569, 2389, 2968, 1082, 2918, 2453, 2465, 1912, 2328, 2290, 2937, 1832],
        backgroundColor: ['rgb(0, 255, 0, 0.2)',],
				borderWidth: 1
			},
			{
				label: 'Recharge',
				data: [270, 190, 380, 180, 160, 110, 350, 300, 350, 280, 160, 110],
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