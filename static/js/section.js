window.addEventListener('DOMContentLoaded',()=>{
    const contentBox = document.querySelector('.index-content');
    const wordBox = document.querySelector('.index-word');
     
     // Event listener for scrolling
     window.addEventListener('touchend',() => {
        console.log('contentBox.scrollTop:',contentBox.scrollTop);
        console.log('contentBox.clientHeight:',contentBox.clientHeight);
        console.log('contentBox.scrollHeight:',contentBox.scrollHeight);
    
        // Check if we're at the bottom
        if ((contentBox.scrollTop + contentBox.clientHeight)/contentBox.scrollHeight >= 0.95) {
    
            // Change color to green
            console.log('到底了');
        } else {
    
            // Change color to white
            console.log('还没到底');
        }
    
    }) 
})

