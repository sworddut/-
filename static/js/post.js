document.addEventListener('DOMContentLoaded', ()=>{
    //get the index-content div
    const contentBox = document.querySelector('.index-content');
    
    // Start with first post
    let counter = 1;
    
    // Load posts 20 at a time
    const quantity = 20;
    
    // When DOM loads, render the first 20 posts
    load();
    
    // If scrolled to bottom, load the next 20 posts
    window.addEventListener('touchend',() => {
        if ((contentBox.scrollTop + contentBox.clientHeight)/contentBox.scrollHeight >= 0.9) {
            load();
        }
    }) 
    
    // Load next set of posts
    function load() {
    
        // Set start and end post numbers, and update counter
        const start = counter;
        const end = start + quantity - 1;
        counter = end + 1;
    
        // Get new posts and add posts
        fetch(`/posts?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            data.posts.forEach(add_post);
        })
    };
    
    // Add a new post with given contents to DOM
    function add_post(contents) {
    
        // Create new post
        const post = document.createElement('div');
        post.className = 'index-word';
        post.innerHTML = contents;
    
        // Add post to DOM
        contentBox.append(post);
    };
});
