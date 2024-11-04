window.onscroll = function(){
    if(window.scrollY > document.getElementById('courses').offsetTop - 10){
        document.getElementById('navbar').classList.add('navbar-scroll');
    }
    else{
        document.getElementById('navbar').classList.remove('navbar-scroll');
    }
}