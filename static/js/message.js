const box = document.querySelector(".box")
const srcUrl = "https://d2pr862w3j3gq8.cloudfront.net/bktask/"

fetch("api/getFile",{
    method:"GET",
    headers:{
        "content-Type":"application/json",
        'X-Requested-With': 'XMLHttpRequest'
    }   
}).then((response) =>
    response.json()
).then((data) => {
    data.data.data.forEach((item, index) => {
        const newText = document.createElement("div");
        const newImg = document.createElement("img");
        newText.classList.add("new-text");
        newText.textContent = item.content;
        newImg.classList.add("image")
        newImg.src = srcUrl+item.file_name;
        const line = document.createElement("hr");
        line.classList.add("line-hr");
        box.appendChild(newText);
        box.appendChild(newImg);
        box.appendChild(line);
    })
})

const sentBtn = document.querySelector(".btn");

const imgInput = document.getElementById('uploadfile');
const textInput = document.getElementById('uploadtext');
const formData = new FormData();

imgInput.addEventListener("change", (e) => {
    const file = e.target.files[0];
    formData.append("image", file);
})
// const csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

sentBtn.addEventListener("click", (e) =>{
    e.preventDefault();
    const url = "api/uploadFile";
    const csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    // if (textInput.value===""){
    //     return
    // }
    formData.append("text", textInput.value);
    // formData.append("text", JSON.stringify({text:textInput.value}));

    fetch(url, {
        method:"POST",
        headers:{
            'X-CSRFToken': csrftoken  
        },
        body:formData
    })
    .then(res => {
        return res.json();
    }).then(data => {
        if ("ok" in data){
            location.href = "/";
        } 
    })
})
