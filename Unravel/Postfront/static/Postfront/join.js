
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

function JoinGroup(id){

console.log(id)
fetch(`http://127.0.0.1:8000/Groups/join/${id}/`,{
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
                'Content-Type':'application/json',
            },
           body:id,
        })
        .then((response) => {
            console.log("Done")
           // putItHere = "'group_id"+id+"'";
           // console.log(putItHere);
            
            // $("#putItHere").load(location.href + " #putItHere");
            location.reload();
            
            // window.onload=function(){
            //     $("#putItHere").focus();
            // }
           
        })
}

function GroupPost(id){
    console.log(id)

    document.getElementById('groupPostForm').addEventListener('submit',function(e){
        e.preventDefault();
        let group_posting_text=document.getElementById('group_posting_text').value;
        let posting_image=document.getElementById('group_posting_image');
        
        let curr_user_id=document.getElementById('curr_user_id').value;

        var formData=new FormData();

        formData.append("group_text",group_posting_text);
        formData.append("group_image",posting_image.files[0]);

        //formData.append("Posted",curr_user_id);
        
        console.log(group_posting_text,posting_image);
        fetch(`http://127.0.0.1:8000/Groups/join/${id}/post/`,{
            method:'POST',
            headers:{
               
                'X-CSRFToken': csrftoken,
                //'Content-Type': 'application/json',
                
            },
    
            body:formData,
            
         })
    
        .then((response) => {
            return response.json()
        })
        .then((data)=>{
            console.log(data)
            location.reload();
            $("#groupPostForm").trigger('reset');
        })
        .catch((error) => {
            console.error('Error:', error);
        });

    })
}
//need to look at reloading
function UpdateGroupPost(id,text){
    console.log(id);
    document.getElementById('updating_text').value=text;

    document.getElementById('UpdateGroupPostForm').addEventListener('submit', function(e){
        e.preventDefault();

        let updating_text=document.getElementById('updating_text').value;
        
        let old_image=document.getElementById('group_post_image').src;
        //console.log("old-",old_image);
        let updating_image=document.getElementById('updating_image')
        let group_id=document.getElementById('group_id').value;
        console.log(group_id)
        let formData=new FormData();
        if (updating_image){
            
            formData.delete("group_image")
            formData.set("group_image",updating_image.files[0])
        }
        else{
            formData.delete("group_image")
            formData.set("group_image",old_image)
        }
        
        

        //console.log("New:",updating_image)

        formData.delete("group_text")
        formData.set("group_text",updating_text)
        console.log(formData);

        fetch(`http://127.0.0.1:8000/UpdateGroupPost/${id}/`,{
            method:'PUT',
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
           
        })
    })
}

function DeleteGroupPost(id){
  //  console.log(id)
    fetch(`http://127.0.0.1:8000/DeleteGroupPost/${id}/`,{
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

function createGroup(){

    document.getElementById('CreateGroupForm').addEventListener('click',function(e){
        e.preventDefault();

        let titleGroup=document.getElementById('titleGroup').value;
        
        let description=document.getElementById('description').value;

        var select = document.getElementById('c');
		var option = select.options[select.selectedIndex].value;
        console.log(select,option);

        let formData=new FormData();
        formData.append("name",titleGroup);
        formData.append('category',option);
        formData.append("description",description)


        fetch('http://127.0.0.1:8000/CreateGroup',{
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
        $("#CreateGroupForm").trigger('reset');
        })
        
        .catch((error) => {
            console.error('Error:', error);
        });

    })
}

function likeGroupPost(id){
    console.log("Liked post no - ",id)
    fetch(`http://127.0.0.1:8000/Groups/join/post/${id}/like_group_post`,{
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
           
        })
        .then((response) => {
            console.log("Liked")
            location.reload();
            
            
        })
}
//I am not using it anymore
function rewardsFunction(id,re){
    document.getElementById('rewardForm').addEventListener('click',function(e){
        e.preventDefault();
    let formData=new FormData();
    if (re === 'pawn'){
        formData.append('reward','pawn');
    }
    else if (re === 'rook'){
        formData.append('reward','rook');
        
    }
    else if (re === 'bishop'){
      
        formData.append('reward','bishop');
    }
    else if (re === 'knight'){

        formData.append('reward','knight');
    }
    else if (re === 'queen'){
        
        formData.append('reward','queen');
    }
    else{
        formData.append('reward','king');
    }
    console.log(id,re);
    fetch(`http://127.0.0.1:8000/Groups/join/post/${id}/reward`,{
        method:'POST',
        headers:{
            'X-CSRFToken':csrftoken,
        },
       body:formData,
    })
    .then((response) => {
        return response.json()
        })
    .then((data) => {
        console.log(data)
        //location.reload();   
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    });
}
var scrollSpy = new bootstrap.ScrollSpy(document.body, {
    target: '#navbar-example2'
  })
  
function sendGroupMessage(id){
    console.log(id)

    document.getElementById('groupChatForm').addEventListener("submit",function(e){
        e.preventDefault();
        //Group/<int:pk>/chat
        let message=document.getElementById('sendsMs').value;
        let formData=new FormData();
        formData.append("message_body",message);
        fetch(`http://127.0.0.1:8000/Group/${id}/chat`,{
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
          
           
        })
    })
}