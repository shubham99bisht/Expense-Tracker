
function fill_transaction_Details()
{
	var jsn = "";
	var user = firebase.auth().currentUser;
	// console.log(user);
	// console.log(user.email);
	// var userid = user.email.split("@")[0].split(".")[0]
	var userid = user.uid;
	var ref = firebase.database().ref('Bills/'+userid);

	ref.on('value', function(snapshot) {
	  // console.log(snapshot.val());
	  jsn = snapshot.val();
	});

	// console.log(jsn);

var promise = new Promise(function(resolve, reject) {
	setTimeout(function(){  var a1 = "<div class='row' style='text-align:center;'><div class='col-md-2'>";
	  var a2 = '</div><div class="col-md-2">';
		var a3= '</div><div class="col-md-2">';
		var a4= '</div><div class="col-md-2">';
		var a5 = '</div><div class="col-md-1"><div style="font-size:20px;"><a target="_blank" href="';
		var a6 = '"><i class="fa fa-image"></i></a></div></div><div class="col-md-1">  <div style="font-size:20px;">';
		var a7 = '</div></div>  <div class="col-md-1"><div style="font-size:20px;"><a target="_blank" href="https://www.google.com"><i class="fa fa-edit" style="color:blue;"></i></a></div></div>';
		var a8 = '<div class="col-md-1"><div style="font-size:20px;"><i class="fa fa-trash" onclick="DeleteByID('
		var a9 = ')"></i></div></div>';


	  for (var transid in jsn)
	  {
			if (transid!=0){var g;
	      g= document.createElement('div');
				g.classList.add("card");
				g.classList.add("mystyle");
	      g.id = transid;
				console.log("a"+transid);
	      document.body.appendChild(g);
	      var abc = a1+jsn[transid]["date"] + a2+jsn[transid]["vendor"] + a3+jsn[transid]["items"] + a4+jsn[transid]["amount"] + a5;
				abc = abc + jsn[transid]["link"] + a6;
				if(jsn[transid]["status"]==1){abc = abc+ '<i class="fa fa-check" aria-hidden="true" style="color:darkgreen"></i>'+ a7;}
				if(jsn[transid]["status"]==0){abc = abc+ '<i class="fa fa-circle" aria-hidden="true" style="color:orange"></i>'+ a7;}
				abc = abc + a8 +"'"+transid +"'"+ a9;
				// console.log(abc);
	      document.getElementById(g.id).innerHTML=abc;}
	   }
		resolve(jsn);
		}, 6000);
	});
	return promise;
}