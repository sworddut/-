function myAnimate(obj, target,callback) {
    clearInterval(obj.timer);
    obj.timer = setInterval(() => {
        var step = (target - obj.offsetLeft) / 10;
        step = step > 0 ? Math.ceil(step) : Math.floor(step);
        if (target == obj.offsetLeft) {
            clearInterval(obj.timer);
            if(callback){
                callback();
            }
        }
        obj.style.left = obj.offsetLeft + step + 'px';
    }, 15);
}

function myAnimateY(obj, target,callback) {
    clearInterval(obj.timer);
    obj.timer = setInterval(() => {
        var step = (target - obj.offsetTop) / 10;
        step = step > 0 ? Math.ceil(step) : Math.floor(step);
        if (target == obj.offsetTop) {
            clearInterval(obj.timer);
            if(callback){
                callback();
            }
        }
        obj.style.top = obj.offsetTop + step + 'px';
        console.log(obj.offsetTop);
    }, 15);
}

function goBackAnimate(obj, target,callback) {
    clearInterval(obj.timer);
    obj.timer = setInterval(() => {
        var step = (target - obj.scrollTop) / 10;
        step = step > 0 ? Math.ceil(step) : Math.floor(step);
        if (target == obj.scrollTop) {
            clearInterval(obj.timer);
            if(callback){
                callback();
            }
        }
        obj.scroll(0,obj.scrollTop+step);
    }, 15);
}