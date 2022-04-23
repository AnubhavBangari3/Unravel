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

//profile user
let profile=document.getElementById('user_id').value; 
//user 
let user=document.getElementById('curr_user').value;
//contains profile id
let curr_user_id=document.getElementById('curr_user_id').value;
//for showing post data
function AllPost(){
    var wrapper=document.getElementById('all');
    wrapper.innerHTML="";
    var url="http://127.0.0.1:8000/Posts";

    fetch(url,)
    .then((response)=>response.json())
    .then(function(data){
        console.log(data);
        let list=data;
        

        for (var i in list){
            //Need to update video front end
            // if (list[i].video !== null) 
            // {
            //     var item=`
            // <div class="card my-2">
            //     <h5 class="card-title my-2">Author :${list[i].author}</h5>
            //     <div class="image_class"><img src="${list[i].image}" class="card-img-top img-fluid" alt="..."></div>
            //     <br>
            //      <div class="video_class">
            //         <video style="width:100%;" controls> 
            //             <source src="${list[i].video}" type="video/mp4">
                    
            //         </video>
                 
            //      </div>
            //      <br>
                
            //     <div class="card-body">
                  
            //       <p class="card-text">Text:${list[i].text}</p>
                  
            //     </div>
            // </div>
            
            
            // `
            // }
            //this is for showing del and update option for author who has created the post
             if (curr_user_id == list[i].author){
                var item=`
            <div class="card my-4">
                
               <div class="for_image_update" style="display:flex;width:800px;justify-content:space-between;margin:0 auto;">
              
               <h5 class="card-title my-2">Author :${list[i].username}</h5>
               <div class="dropdown">
                           <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">

                           </button>
                           <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
                           <input type="hidden" name="post" id="postID" value="{{list.id}}"/>
                           <li><button type="button" class="dropdown-item" data-bs-toggle="modal" data-bs-target="#exampleModal" onClick="EditPost(${list[i].id})">Update</button></li>
                            <li><button class="dropdown-item" onClick="DeletePost(${list[i].id})">Delete</button></li>

                           </ul>
               </div>
               </div>
                  
               
                <div class="image_class"><img src="${list[i].image}" id="old_img" class="card-img-top img-fluid" alt="..."></div>

                
                <div class="card-body">
                   
                    <div class="btn-group my-2" role="group" aria-label="Basic example">
                        <div>
                        
                        <span>
                        <button type="button" class="btn btn-dark mx-4" onClick="LikePost(${list[i].id})" value="liked">Liked</button>
                        <br><h6 id="liked${list[i].id}" ><b>Total likes   ${list[i].total_likes}</b></h6>
                        </span>
                        <!--
                        <i class="far fa-thumbs-up fa-3x mx-4"></i><i class="fas fa-thumbs-down fa-3x"></i>-->
                        </div>
                        <div><a href="single_post/${list[i].id}"><i class="fa-solid fa-comment fa-2x mx-2"></i></a>
                        <br>
                        <b>Total comments ${list[i].commentC}</b>
                        </div>
                      <!--  <div>
                    
                      <input type="hidden" name="post" id="postID" value="{{list.id}}"/>
                      <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" onClick="EditPost(${list[i].id})">Update</button>
                      <button class="btn btn-danger" onClick="DeletePost(${list[i].id})">Delete</button>
                  </div> -->
                        
                    </div>
                    
                    <hr>
                  
                  <p class="card-text"><b>Text</b> - ${list[i].text}</p>
                  <br>
                  
                  
                  
                </div>
            </div>
            
                <!-- Modal to show update Information -->
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title post_no" id="exampleModalLabel">Update Post</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    
                    <div class="modal-body">

                            <div id="p" style="display:flex;justify-content:center;text-align:center;">

                            <form method="POST" action="" enctype="multipart/form-data" id="UpdateForm">
                    
                                
                                <div class="posting_data">
                                
                                    <div class="form-group">
                                        <input type="textarea" name="updating_text" value="" id="updating_text" placeholder="Write something .."
                                        style="width:350px;height:80px;">
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label id="updating_images">Upload Photo</label>
                                        
                                        <input type="file" name="updating_image" id="updating_image">
                                    </div>
                                    <br>
                                   
                                </div>
                                <br>
                                <button class="btn btn-dark">Update</button>
                            </form>
                        </div>

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        
                    </div>
                    </div>
                </div>
                </div>
            
            
            `
         
            
            }
            //del and update button will not be shown 
            else{
                var item=`
                <div class="card my-4">
                       
                   
                <h5 class="card-title my-2">Author :${list[i].username}</h5>
                    <div class="image_class"><img src="${list[i].image}" class="card-img-top img-fluid" alt="..."></div>

                    <div class="card-body">
                       
                        <div class="btn-group my-2" role="group" aria-label="Basic example">
                            <div>
                           <!-- <i class="far fa-thumbs-up fa-3x mx-4"></i>-->
                           <span>
                            <button type="button" class="btn btn-dark mx-4" onClick="LikePost(${list[i].id})" value="liked">Liked</button>
                            <br>
                            <h6 id="liked${list[i].id}" ><b>Total likes   ${list[i].total_likes}</b></h6>
                            </span>
                            </div>
                            <div><a href="single_post/${list[i].id}"><i class="fa-solid fa-comment fa-2x mx-2"></i></a>
                            <br>
                            <b>Total comments ${list[i].commentC}</b></div>
                            
                        </div>
                        
                        <hr>
                      
                      <p class="card-text"><b>Text</b> - ${list[i].text}</p>

                      <br>
                  
                  
                      
                    </div>
                </div>
                
                
                `
            }
            wrapper.innerHTML+=item;
            
        }
       
        
      
       
    })
}

AllPost()

//Posting form
document.getElementById('loginForm').addEventListener('submit',function(e){
    e.preventDefault();
    let posting_text=document.getElementById('posting_text').value;
    let posting_image=document.getElementById('posting_image');
    
   let formData=new FormData();
  
    
    formData.append("text",posting_text); 
    formData.append("image",posting_image.files[0]);
    formData.append("Author",profile);
    
   // console.log("Form:",formData)
    fetch('http://127.0.0.1:8000/Create',{
        method:'POST',
        headers:{
           
            'X-CSRFToken': csrftoken,
            // 'Content-Type': 'application/json',
        },

        body:formData,
        
     })

    .then((response) => {
        return response.json()
    })
    .then((data)=>{
        console.log(data)
        //location.reload();
        $("#loginForm").trigger('reset');
    })
    .then((response)=>{
        AllPost()
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    
})

//Yet to solve 1 and 2

//updation is successful now
//1)Now I need to solve the problem of undefined image if we are not updating new image
//2)need to focus on the image that is updated after reloading.(Do this afterwards)
//solve issue 1 and then look at the notes in paper and execute that.
//solve issue 2 afterwards.
let active=0;

function EditPost(id){
    let postid=id;
    
    var url="http://127.0.0.1:8000/Posts";
    fetch(url,)
    .then((response)=>response.json())
    .then(function(data){
        let list=data;

        for (let i in list){
            
            if (postid === list[i].id){
                active=list[i]
            }
            
        }
        //to set the text to previous posttext
      document.getElementById('updating_text').value=active.text;
     
        
    })

    //this is to perofrm update
    document.getElementById('UpdateForm').addEventListener('submit',function(e){
        e.preventDefault();
        let updating_text=document.getElementById('updating_text').value;
        
        let old_image=document.getElementById('old_img').src;
        //console.log("old-",old_image);
        let updating_image=document.getElementById('updating_image')
        let formData=new FormData();

        //var UpdateData=new FormData();
        if (updating_image){
            
            formData.delete("image")
            formData.set("image",updating_image.files[0])
        }
        else{
            formData.delete("image")
            formData.set("image",old_image)
        }
        
        let author_id=active.author;

        //console.log("New:",updating_image)

        formData.delete("text")
        formData.set("text",updating_text)

        formData.delete("Author")
        formData.set("Author",author_id)
       // formData.append("group_id",group_id)
        // for(let val of formData.values())
        // {
        //     console.log(val);
        // }
        
        // console.log("Before:",formData)
    
        fetch(`http://127.0.0.1:8000/Update/${postid}/`,{
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
           // $("#UpdateForm").trigger('reset');
        })
    
    })

}
//for deleting
function DeletePost(id){ 

    //console.log("Delete:",id)
    fetch(`http://127.0.0.1:8000/Delete/${id}/`,{
            method:'DELETE',
            headers:{
                'X-CSRFToken':csrftoken,
            },
           
        })
        .then((response) => {
            AllPost()
        })
        
    
}

//for liking post
//Form for posting like.
//Basically I need to add 1) Change color when liked 2)Dynamic like count increase
function LikePost(id){ 
    console.log("Liked post no - ",id)
    fetch(`http://127.0.0.1:8000/Posts/${id}/like`,{
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
           
        })
        .then((response) => {
            console.log("Liked")
            putItHere = "'liked"+id+"'";
            console.log(putItHere);
            
            location.reload();
            $("#putItHere").load(location.href + " #putItHere");
            // window.onload=function(){
            //     $("#putItHere").focus();
            // }
            
        })
}

