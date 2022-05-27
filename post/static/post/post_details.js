// Picture slider for Post Details

const postDetailsMainPicture = document.querySelector('.post-details-main-picture');
const postDetailsPictures = document.querySelectorAll('.post-details-picture');
const allImages = [];

postDetailsPictures.forEach(picture => {
    allImages.push(picture);
});
let currentPictureIndex = 0

function previous(){
    if(currentPictureIndex <= 0) currentPictureIndex = allImages.length;
    currentPictureIndex--;
    slideCounter();
    return setPicture();
}

function next(){
    if(currentPictureIndex >= allImages.length - 1) currentPictureIndex = -1;
    currentPictureIndex++;
    slideCounter();
    return setPicture();
}

function setPicture(){
    const src = allImages[currentPictureIndex].getAttribute('src');
    postDetailsMainPicture.removeAttribute('src');
    postDetailsMainPicture.setAttribute('src', src);
    return postDetailsMainPicture.setAttribute('src', src);
}
setPicture()

// Count the pictures '1 of 10' etc
function slideCounter(){
    let counter = document.getElementById('slide-counter');
    return counter.innerText = `${currentPictureIndex + 1} of ${allImages.length}`;
};
slideCounter();

// Confirm delete post
const deletePostBtn = document.getElementById('delete-post');
deletePostBtn.addEventListener('click', e =>{
    e.preventDefault();
    let confirmDeleteBox = document.querySelector('.confirm-delete');
    confirmDeleteBox.classList.remove('d-none');
    let deletePostNo = document.getElementById('delete-post-no');
    deletePostNo.addEventListener('click', e=>{
        e.preventDefault();
        confirmDeleteBox.classList.add('d-none');
    });
});