// offline data
db.enablePersistence()
  .catch(err => {
      if(err.code == 'failed-precondition'){
        //   probably multiple tabs open at once
          console.log('persistence failed');
      } else if(err.code == 'unimplemented'){
          console.log('persistence is not avaliable');
      }
  });

// real-time listener
db.collection('devices').onSnapshot((snapshot)=>{
    // console.log(snapshot.docChanges());
    snapshot.docChanges().forEach(change => {
        // console.log(change,change.doc.data(), change.doc.id);
        if(change.type === 'added'){
            // add the document data to the web page
            renderDevice(change.doc.data(),change.doc.id);

        }
        if(change.type === 'removed'){
            // remove the document data from the web page
            removeDevice(change.doc.id);
        }
    });
});

// add new device
const form = document.querySelector('form');
form.addEventListener('submit',evt => {
    evt.preventDefault();
    scrape().then(function(devices) {
        // Run this when your request was successful
        console.log(devices);
        devices.forEach(device=>{
                           db.collection('devices').add(device)
                           .catch(err => console.log(err));
                       });
      }).catch(function(err) {
        // Run this when promise was rejected via reject()
        error();
        console.log(err)
      })
    form.title.value = '';
});

// delete a device
const deviceContainer = document.querySelector('.devices');
deviceContainer.addEventListener('click',evt => {
    // console.log(evt);
    if(evt.target.tagName === 'I'){
        const id = evt.target.getAttribute('data-id');
        db.collection('devices').doc(id).delete();
    }
});

function scrape() {
    return new Promise(function(resolve, reject) {
      $.ajax({
        type: 'POST',
        url: "http://127.0.0.1:3000/scrape/",
        data: JSON.stringify({"item_id":form.title.value}),
        contentType: 'application/json; charset=utf-8',
        success: function(data){
             resolve(data)
        },
        error: function(err) {
          reject(err)
        }
});
    });
  }