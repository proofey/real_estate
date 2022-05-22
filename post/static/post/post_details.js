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
    return setPicture();
}

function next(){
    if(currentPictureIndex >= allImages.length - 1) currentPictureIndex = -1;
    currentPictureIndex++;
    return setPicture();
}

function setPicture(){
    const src = allImages[currentPictureIndex].getAttribute('src');
    postDetailsMainPicture.removeAttribute('src');
    postDetailsMainPicture.setAttribute('src', src);
    return postDetailsMainPicture.setAttribute('src', src);
}