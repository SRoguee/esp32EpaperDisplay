const fileTypes = [
        "image/apng",
        "image/bmp",
        "image/gif",
        "image/jpeg",
        "image/pjpeg",
        "image/png",
        "image/svg+xml",
        "image/tiff",
        "image/webp",
        "image/x-icon",
];
function checkValidFile(file) {
    return fileTypes.includes(file.type);
}
function returnByteSize(file) {
    if (file.size >= 1000000){
        return `${Math.round((file.size / 1000000) * 100) / 100} MB`;
    }
    else if (file.size > 1000) {
        return `${Math.round((file.size / 1000) * 100) / 100} KB`;
    }
    return `${file.size} Bytes`;
    
}
const upButt = document.querySelector("#submitButton");
const input = document.querySelector("input");
const preview = document.querySelector("#preview");
input.addEventListener("change", updateDisplayIMG);
console.log(preview);
console.log(preview.innerHTMl);
console.log(input);
preview.innerHTML = "";
preview.style.padding = "100vh 0% 0% 0%";

const form = document.querySelector("form");

/*upButt.addEventListener('click', function() {
  // Perform your action here
  
  // Grey out and disable the button
  upButt.disabled = true;
});*/

//form.addEventListener("submit", async (event) => {
//    event.preventDefault();
//})
function updateDisplayIMG(){
    if ((preview.childNodes).length >= 1){
        preview.innerHTML = ""
    }
    console.log(preview)
    let curFiles = input.files;
    if (curFiles.length === 0){
        let emptyFiles = document.createElement("p");
        emptyFiles.innerHTML = "No files have been selected";
        preview.appendChild(emptyFiles)
    }
    else {
        let x = 0;
	preview.style.padding = "20px 0 100vh";
        for (const file of curFiles){
            if (checkValidFile(file)){
                let fileList = document.createElement("div");
                const image = document.createElement("img");
                let name = document.createElement("p");
                let size = document.createElement("p");
                size.innerHTML = returnByteSize(file);
                name.innerHTML = file.name;
                image.src = URL.createObjectURL(file);
                image.width = 160;
                image.height = 90;
                fileList.appendChild(image);

                fileList.appendChild(name);
                fileList.appendChild(size);
                x = x + 1;
                preview.appendChild(fileList);
            }
            else {
                const inValid = document.createElement("p");
                inValid.innerHTML = "This image type is not supported message eoghan"
                preview.appendChild(inValid);
            }
        }
	if (preview.innerHTML == "") {
		preview.style.padding = "100vh, 0px , 0px, 0px";
	}
        
        
    }
}
function handleUpload(){
    const content = document.querySelector("#imageFile");
    console.log(content.value);
    const files = content.files;
    console.log(files);
    const filesArray = Array.from(files);
    filesArray.forEach(console.log);
}
