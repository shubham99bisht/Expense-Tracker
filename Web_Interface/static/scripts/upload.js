function upload_image_firebase(file, userid, billid){
      console.log(file);
       var storageRef = firebase.storage().ref();
       // Upload file and metadata to the object 'images/mountains.jpg'
       var uploadTask = storageRef.child(userid +'/'+ billid +'/'+ file.name).put(file);

       // Listen for state changes, errors, and completion of the upload.
       uploadTask.on(firebase.storage.TaskEvent.STATE_CHANGED, // or 'state_changed'
         function(snapshot) {
           // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
           var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
           console.log('Upload is ' + progress + '% done');
           switch (snapshot.state) {
             case firebase.storage.TaskState.PAUSED: // or 'paused'
               console.log('Upload is paused');
               break;
             case firebase.storage.TaskState.RUNNING: // or 'running'
               console.log('Upload is running');
               break;
           }
         }, function(error) {}, function() {
         // Upload completed successfully, now we can get the download URL
         uploadTask.snapshot.ref.getDownloadURL().then(function(downloadURL) {
           firebase.database().ref('Bills/'+userid +'/'+ billid).set({"Link":downloadURL});
           console.log('File available at', downloadURL);
         });
       });

       firebase.database().ref('users/'+userid).update({
         "Prev_id":billid
       });

     }