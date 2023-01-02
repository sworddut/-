function getQueryVariable(variable)
{
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
        var pair = vars[i].split("=");
        if(pair[0] == variable){return pair[1];}
    }
    return(false);
}

document.addEventListener('DOMContentLoaded', () => {
    //get the index-content div
    const contentBox = document.querySelector('.index-content');

    // Start with first post
    let counter = 1;

    // Load posts 20 at a time
    const quantity = 20;

    // When DOM loads, render the first 20 posts
    load();

    // If scrolled to bottom, load the next 20 posts
    window.addEventListener('touchend', () => {
        if ((contentBox.scrollTop + contentBox.clientHeight) / contentBox.scrollHeight >= 0.9) {
            load();
        }
    })

    // Load next set of posts
    function load() {

        // Set start and end post numbers, and update counter
        const start = counter;
        const end = start + quantity - 1;
        counter = end + 1;
        const keywords = getQueryVariable('keywords');
        console.log(keywords);
        // Get new posts and add posts
        fetch(`/postSearch?keywords=${keywords}&start=${start}&end=${end}`)
            .then(response => response.json())
            .then(data => {
                if(data.posts.length !== 0 || keywords === ''){
                    data.posts.forEach(add_post);
                    console.log(data);
                }
                else{
                    add_when_null();
                    console.log('没有帖子');
                }
                
            })
    };

    // Add a new post with given contents to DOM
    function add_post(contents) {

        // Create new post
        const post = document.createElement('div');
        post.className = 'index-word';
        post.innerHTML =`<div class="index-content-name">
                        <span>${contents['name']}</span>
                        <em>${contents["time"]}</em>
                        </div>
                        <div class="index-content-text">
                        ${contents["appendwords"]}
                        </div>`;

        // Add post to DOM
        contentBox.append(post);
    };

    function add_when_null() {
        // Add post to DOM
        contentBox.innerHTML =  `<div class="not-found">
        <span>什么都没找到哦</span>
        </div>`;
    };
});
