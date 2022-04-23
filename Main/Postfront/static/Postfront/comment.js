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
function Comment(id){
    document.getElementById('commentForm').addEventListener("submit",function(e){
        e.preventDefault();
        var c=document.getElementById('comment').value;
        console.log(c)
        let formData=new FormData();
        formData.append("body",c)
        console.log("FormData: ",formData)
        
        fetch(`http://127.0.0.1:8000/Posts/${id}/comment`,{
                method:'POST',
                headers:{
                    'X-CSRFToken':getCookie('csrftoken'),
                },
                body:formData,
               
            })
            .then((response) => {
                return response.json()
            })
            .then((response) => {
                console.log("Comment on post number :",id)
                location.reload();
                //$("#commentForm").trigger('reset');
                
            })
    
    })
    
    }