
function fill_transaction_Details()
{
	var jsn = "";
	// var promise = new Promise(function(resolve, reject) {
	// 		var user = firebase.auth().currentUser;
	// 		console.log(user);
	// 		if(user) {
	// 		resolve();
	// 		} else {
	// 		reject();
	// 		}
	// 	})
	//
	// promise.then(function() {
	// 			console.log("successMessage");
	// 		})
	// 		.catch(function() {
	// 			console.log("errorMessage");
	// 		});
	// return true;

	// while(!user){var user = firebase.auth().currentUser;}
	var user = firebase.auth().currentUser;
	console.log(user);
	console.log(user.email);
	var userid = user.email.split("@")[0].split(".")[0]
	var ref = firebase.database().ref('Bills/'+userid);
	ref.on('value', function(snapshot) {
	  // console.log(snapshot.val());
	  jsn = snapshot.val();
	});

	console.log(jsn);
	// return true;


		var a1 = "<div class='row' style='text-align:center;'><div class='col-md-2'>#";
	  var a2 = '</div><div class="col-md-2">';
		var a3= '</div><div class="col-md-3">';
		var a4= '</div><div class="col-md-3">';
	  var a5= '</div><div class="col-md-2">';
		var a6 = '</div></div>';

	  for (var transid in jsn)
	  {
			if (transid!=0){var g;
				// console.log("hello")
	      g= document.createElement('div');
				g.classList.add("card");
				g.classList.add("mystyle");
	      g.id = transid;
	      document.body.appendChild(g);
	      var abc = a1+transid + a2+jsn[transid]["Date"] + a3+jsn[transid]["Vendor"] + a4+jsn[transid]["Category"] + a5+jsn[transid]["Amount"] + a6;
				// console.log(abc);
	      document.getElementById(g.id).innerHTML=abc;}
	    }}





// setTimeout(function(){  var a1 = "<div class='row' style='text-align:center;'><div class='col-md-2'>#";
//   var a2 = '</div><div class="col-md-2">';
// 	var a3= '</div><div class="col-md-3">';
// 	var a4= '</div><div class="col-md-3">';
//   var a5= '</div><div class="col-md-2">';
// 	var a6 = '</div></div>';
//
//   for (var transid in jsn)
//   {
// 		if (transid!=0){var g;
// 			// console.log("hello")
//       g= document.createElement('div');
// 			g.classList.add("card");
// 			g.classList.add("mystyle");
//       g.id = transid;
//       document.body.appendChild(g);
//       var abc = a1+transid + a2+jsn[transid]["Date"] + a3+jsn[transid]["Vendor"] + a4+jsn[transid]["Category"] + a5+jsn[transid]["Amount"] + a6;
// 			// console.log(abc);
//       document.getElementById(g.id).innerHTML=abc;}
//     }}, 8000);
// }

// fill_transaction_Details();
