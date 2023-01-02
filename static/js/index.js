window.addEventListener('DOMContentLoaded',()=>{
    // 返回顶部
    const goBack = document.querySelector('.back-top');
    const contentBox = document.querySelector('.index-content');
    goBack.addEventListener('click',function () {
        goBackAnimate(contentBox,0);
    });

    // 添加帖子
    const appendPost = document.querySelector('.append-post');
    const appendTextarea = document.querySelector('.append-textarea');
    const appendTextareaHeight = 250;
    appendPost.addEventListener('touchend',e=>{
        console.log('append');
        // 要阻止事件冒泡,这样点击子盒子才不会触发父盒子是事件
        e.stopPropagation();
        // window.innerHeight-appendTextareaHeight为底部到盒子的距离
        myAnimateY(appendTextarea,window.innerHeight-appendTextareaHeight);
    });
    const appendParentNode = appendTextarea.parentElement;
    appendTextarea.addEventListener('touchend',e=>{
        e.stopPropagation();
        console.log('appendTextarea');
    })
    appendParentNode.addEventListener('touchend',e=>{
        console.log('appendParentNode');
        // 点击父盒子,弹窗收回
        myAnimateY(appendTextarea,window.innerHeight);
    })

    // 更改登录处的用户名
    const getCookie = (name) => document.cookie.match(`[;\s+]?${name}=([^;]*)`)?.pop();
    const username = getCookie('username') || '登录';
    const login = document.querySelector('.login');
    login.innerHTML = username;
    
})
