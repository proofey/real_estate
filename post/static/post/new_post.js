// Preview main picture on attach
const newPostMainPicture = document.querySelector('.post-details-main-picture');
const attachMainPicture = document.getElementById('id_main_picture');
const src = newPostMainPicture.getAttribute('src');
attachMainPicture.addEventListener('change', ()=>{
    const file = attachMainPicture.files[0];
    if(file){
        const reader = new FileReader();

        reader.addEventListener('load', ()=>{
            newPostMainPicture.setAttribute('src', reader.result);
        });

        reader.readAsDataURL(file);
    }else{
        newPostMainPicture.setAttribute('src', src);
    };
});

// Toggle the dropdown for Attach More Pictures
const attachMorePicturesBtn = document.getElementById('attach-more-pictures-btn');
attachMorePicturesBtn.addEventListener('click', (e)=>{
    e.preventDefault();
    const attachMorePicturesBox = document.getElementById('attach-more-pictures');
    if(attachMorePicturesBox.classList.contains('d-none')){
        attachMorePicturesBox.classList.remove('d-none');
    }else{
        attachMorePicturesBox.classList.add('d-none');
    };
});