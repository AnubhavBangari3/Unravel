
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function sendFriendRequest(id){
    console.log(id)
    

        fetch(`http://127.0.0.1:8000/FriendRequest/${id}`,{
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            

        })
       
         .then((data)=>{
        console.log(data)
        location.reload();
        
        })
        
        .catch((error) => {
            console.error('Error:', error);
        });

}


    
function sendMessage(id){
    console.log("Sending message to:",id)

    document.getElementById('sendingMessageForm').addEventListener("submit",function(e){
        e.preventDefault();
        let messageText = document.getElementById('sendM').value;
        console.log(messageText)
        let formData=new FormData();
        formData.append("body",messageText);

        fetch(`http://127.0.0.1:8000/sendingMessage/${id}`,{
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            body:formData,
        })
        .then((response) => {
            return response.json()
        })
        .then((data)=>{
            console.log(data)
          location.reload();
           // $("#sendingMessageForm").trigger('reset');
           
        })
    })
}

    var scrollSpy = new bootstrap.ScrollSpy(document.body, {
        target: '#navbar-example3'
      })



      function deleteMessage(id){
        //  console.log(id)
          fetch(`http://127.0.0.1:8000/DeleteMessage/${id}/`,{
              method:'DELETE',
              headers:{
                  'X-CSRFToken':csrftoken,
              },
             
          })
          .then((response) => {
              console.log("Post deleted")
              location.reload();
          })
      }