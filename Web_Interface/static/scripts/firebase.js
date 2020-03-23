
var transaction_json;

firebase.auth().onAuthStateChanged(function(user) {
	if (user) {

		if(firebase.auth().currentUser.metadata.lastSignInTime == firebase.auth().currentUser.metadata.creationTime){
			first_login()
		}

		myjson = 10;
		path = window.location.pathname.split("/")
		path = path[path.length-1]
		if(path=="login" || path=="signup"){window.location.replace("transaction");}

		if(user && path=="transaction"){fill_transaction_Details()}
		
		}
	else {
		path = window.location.pathname.split("/")
		path = path[path.length-1]
		if(path!="login" && path!="signup"){
		window.location.replace("login");}
	}
});

// <!--===============================================================================================-->

function login_function(){
	var email = document.getElementById("username").value;
	var password = document.getElementById("password").value;

	firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
		// Handle Errors here.
		var errorMessage = error.message;
		window.alert(errorMessage);
	});

}

// <!--===============================================================================================-->

function logout_function(){
	// window.warning("do you want to log out?");
firebase.auth().signOut().then(function() {
  // Sign-out successful.
}).catch(function(error) {
  // An error happened.
});
}

// <!--===============================================================================================-->

function new_account(){
	var email = document.getElementById("email").value;
	var password1 = document.getElementById("password1").value;
	var password2 = document.getElementById("password2").value;
	if (password1 != password2) {
      window.alert("\nPassword did not match: Please try again...")
      return false; }
	firebase.auth().createUserWithEmailAndPassword(email, password1).catch(function(error) {
  // Handle Errors here.
  var errorCode = error.code;
  var errorMessage = error.message;
  window.alert(errorMessage);
	return false;
});

var username = email.split("@")[0]

alert("Hello, you're registered: "+username)

}


function first_login(){
	var user = firebase.auth().currentUser;
	var userId = user.uid;
	var email = user.email;
	var name = email.split("@")[0]

	firebase.database().ref('Bills/'+userId).set({
		"0000":0
	});

	firebase.database().ref('users/'+userId).set({
		Email:email,
		Name:name,
		Prev_id:"0000"
	});
}





// <!--===============================================================================================-->

function writeUserData(userId, name, email, imageUrl) {
  firebase.database().ref('users/' + userId).set({
    username: name,
    email: email,
    profile_picture : imageUrl
  });
}

function writeTransData(vendor, date, amt, category){
  firebase.database().ref('Bills/shadrak/1007').set({
		Amount: amt,
		Category: category,
    Vendor: vendor,
    Date: date
  }, function(error) {
    if (error) {
      alert("The write failed..."+error);
    } else {
      alert("Data saved successfully!");
    }
  });
 // window.close();
}

 // function DeleteByID(id){
	//  r = confirm("Do you want to delete "+id+"?");
	//  if(r==1){alert("Deleted "+id);}
 // }

function DeleteByID(id) {
	var user = firebase.auth().currentUser;
	r = confirm("Do you want to delete "+id+"?");
  if(r==1){
		console.log(id);
		firebase.database().ref('Bills/' + user.uid +'/'+ id).remove();
		document.getElementById(id).style.display="none";}
}
// <!--===============================================================================================-->

function dummy(){
	window.alert("I'm called");
}
