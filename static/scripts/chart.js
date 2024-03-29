function fill_chart_Details(){
  // alert("I'm called now");
  document.getElementById("Loader").style.display = "none";
  document.getElementById("myChart").style.display = "block";

  var user = firebase.auth().currentUser;
  var userid = user.uid;
	var ref = firebase.database().ref('Bills/'+userid);

	ref.on('value', function(snapshot) {
		  jsn = snapshot.val();
      console.log(jsn);
      var arr = [0, 0, 0, 0, 0, 0, 0, 0, 0];
      var dict = {"Misc":0, "Food":1, "Shopping":2, "Medicals":3, "Travel":4, "Banking-Insurance":5, "Govt Public Bills":6, "Ration":7, "Recharge Payment":8 }

      for (var transid in jsn)
      {
        if (transid!=0){
          // arr[jsn[transid]["Category"]]+= parseInt(jsn[transid]["Amount"].split(",").join(""));
          arr[dict[jsn[transid]["Category"]]]+= parseInt(jsn[transid]["Amount"].split(",").join(""));
        }
      }

      for (var key in dict) {
        document.getElementById(key).innerHTML= arr[dict[key]];
            console.log(dict[key]);
         }

      console.log(arr);

      var ctx = document.getElementById('myChart').getContext('2d');
      var myChart = new Chart(ctx, {
          type: 'doughnut',
          data: {
              labels: [ "Misc", "Food", "Shopping", "Medicals", "Travel", "Banking-Insurance", "Govt Public Bills", "Ration", "Recharge Payment" ],
              datasets: [{
                  label: 'Expenditure per Category',
                  // data: [2000, 540, 9500, 3500],
                  data: arr,
                  backgroundColor: [
                    // 'rgba(255, 99, 132, 0.2)',
                      'rgba(255, 0, 0, 0.2)',
                      'rgba(54, 162, 235, 0.2)',
                      'rgba(255, 206, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(153, 102, 255, 0.2)',
                      'rgba(255, 159, 64, 0.2)',
                      'rgb(0, 255, 0, 0.2)',
                      'rgb(255, 132, 255, 0.2)',
                      'rgb(255, 255, 128, 0.2)'
                  ],
                  // backgroundColor: ['rgb(255, 99, 132)','rgb(0, 255, 0)','rgb(255, 99, 132)','rgb(128, 255, 0)','rgb(0, 255, 255)','rgb(255, 255, 0)','rgb(255, 255, 128)'],

                  borderColor: [
                    // 'rgba(255, 99, 132, 1)',
                      'rgba(255, 0, 0, 1)',
                      'rgba(54, 162, 235, 1)',
                      'rgba(255, 206, 86, 1)',
                      'rgba(75, 192, 192, 1)',
                      'rgba(153, 102, 255, 1)',
                      'rgba(255, 159, 64, 1)',
                      'rgb(0, 255, 0, 1)',
                      'rgb(255, 132, 255, 1)',
                      'rgb(255, 255, 128)'
                  ],
                  borderWidth: 1
              }]
          },
          options: {

            legend: {display: true,
                      position: 'bottom',
                      labels: {
                          fontSize: 15,
                          boxWidth: 50
                      }
                    }
          }
      });
    });
}


firebase.auth().onAuthStateChanged(function(user) {
	if (user){fill_chart_Details()} });
