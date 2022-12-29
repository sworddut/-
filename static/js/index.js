window.addEventListener('DOMContentLoaded',()=>{
    const goBack = document.querySelector('.back-top');
    const contentBox = document.querySelector('.index-content');
    goBack.addEventListener('click',function () {
        goBackAnimate(contentBox,0);
    })
})
