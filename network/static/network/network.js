document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#postInteract button').forEach(
        element => element.addEventListener('click', postUpdate));
})

function postUpdate() {
    //function that allows like, dislike, comment (comment will change page view)
    var methodInteract = this.name;
    //check for which method is being used
    if(methodInteract === 'like') {
        //do something
    }
    else if(methodInteract === 'dislike') {
        //do something
    }
    else if(methodInteract === 'comment') {
        //do something
    }
    else {
        console.log('Invalid method')
    }
}