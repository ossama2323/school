// var name = "hello world!";

// console.log(name);

// alert("hello world!");



// ------------------------- fake calculator with if & else ----------------------------

    // var x = 20;
    // var y = 20;

    // var o = "*";

    // if(o == "+"){
    //     alert(x + y);
    // }
    // else if(o == "-") {
    //  alert(x - y);   
    // }
    // else if(o == "*") {
    //     alert(x * y);   
    // }else{
    //     alert(x / y);
    // }




    // ------------------------------- get element by id------------------------------------------

    // var title = "session 12";

    // document.getElementById("x").innerHTML = title;




    // ------------------------- fake calculator with switch ----------------------------

//     var q = 33;  
//     var s = 78;
    
//     var e = "-";

//     switch(e){
//         case "+":
//             document.write(q + s);
//         break;
//         case "-":
//              document.write(q - s);
//         break;
//         case "*":
//              document.write(q * s);
//         break;
//         case "/":
//              document.write(q / s);
//         break;
//     }


     // ////////////////////////////////WHILE & DO WHILE & for

     //////////////while

     // var w = 2;

     // while(w <= 10){
     //      document.write(w + "<br>");
     //      w++;
     // }



     /////////////////////DO WHILE 

     // var d = 2;

     // do{
     //      document.write(d + "<br>");
     //      d++;
     // } while(d <= 10);




     ////////////////////// FOR

     // for(var f = 1; f < 10; f++){
     //      document.write(f + "<br>");
     // }





     //////////////// loop task 1

    //  for(var h= 1; h < 10; h++){
    //            if (h == 2) {
    //                 document.write("hamza gentiih" + "<br>");
    //            }else {
    //                 document.write(h + "<br>");
    //            }
    //  }



     ////////////// loop task 2
    //  var y = 2;
    //  for( var x=1; x <= 10; x++){
    //       document.write(y + "*" + x + "=" + x*y +"<br>");
    //  }





          // //////////////////////////////// FUNCTIONS

    // function number(num){
    //     document.write(num);
    // }

    // number(5);


    // function number(num){
    //     return num;
    // }
    // document.write(number(4) - 2);



    ////////// 3 methode to asigne function 
    

        //////////////////// methode 1 
    // function add(){
    //     alert("mohamed");
    // }

        //////////////////// methode 2
    // var add = function(){
    //     alert("mohamed");
    // }

        //////////////////// methode 3
    // (function add(){
    //     alert("mohamed");
    // })();


    // CALCULATOR WITH FUNCTION


    // function calculator(){
    //     var x = parseInt(document.getElementById('x').value);
    //     var y = parseInt(document.getElementById('y').value);
    //     var o = document.getElementById('o').value;

    //     if(isNaN(x) || isNaN(y)){
    //         document.getElementById("res").innerHTML="x and y must be a number";
    //     }
    //     else{
    //         switch(o){
    //             case "+":
    //                 document.getElementById("res").innerHTML = x + y;
    //             break;
    //             case "-":
    //                 document.getElementById("res").innerHTML = x - y;
    //             break;
    //             case "*":
    //                 document.getElementById("res").innerHTML = x * y;
    //             break;
    //             case "/":
    //                 document.getElementById("res").innerHTML = x / y;
    //             break;
    //         }
    //     }
    // }




    ///////////////////////////////////// error Task

    // function add(){
    //     var x = document.getElementById('x').value;
    //     var y = document.getElementById('y').value;

    //     if( x == ''){
    //         document.getElementById('x').classList.add('error');
    //     }else if( y == ''){
    //         document.getElementById('y').classList.add('error');
    //     }else{
    //         document.getElementById('x').classList.remove('error');
    //         document.getElementById('y').classList.remove('error');
    //     }
    // }



    ///////////////////////////////////////// scroll effects test


    window.onscroll = function(){
        alert('achiko AR');
    }



    window.onscroll = function(){
        if(window.scrollY > 39){
            document.getElementById('n').classList.add('navbg1');
        }else{
            document.getElementById('n').classList.remove('navbg1');
        }

        console.log(window.scrollY);
    }






    //------------------------- box-color TASK ---------------------------

    // function change(color){
    //     document.body.style.background = color;
    // }






        //------------------------- ARRAY TASK ---------------------------

        // var fruit = [ 'apple', 'orange', 'strawebery', 'banana'];

        // for(var r = 0; r < fruit.length; r++){
        //     if(r == 0){
        //         document.getElementById('f-1').innerHTML = ("the first fruit is : " + fruit[r] + '<br>');
        //     }else if(r == 1){
        //         document.getElementById('f-2').innerHTML = ("the second fruit is : " + fruit[r] + '<br>');
        //     }else if(r == 2){
        //         document.getElementById('f-3').innerHTML = ("the third fruit is : " + fruit[r] + '<br>');
        //     }else if(r == 3){
        //         document.getElementById('f-4').innerHTML = ("the fourth fruit is : " + fruit[r] + '<br>');
        //     }
        // }


        ////////////// ARRAY TASK another way

        // var fruit = [ 'apple', 'orange', 'strawebery', 'banana'];

        // for(var r = 0; r < fruit.length; r++){
        //     var res = '<li>' + fruit[r] + '</li>';

        //     document.getElementById('list').innerHTML += res;
        // }



                ////////////// ARRAY TASK with object 

                // var persones = [];

                // function add(){
                //     var name = document.getElementById('name').value;
                //     var age = document.getElementById('age').value;


                //     var persone = {'name': name , 'age': age};

                //     persones.push(persone);
                    
                //     console.log(persones);

                //     view();
                // }


                // function view(){
                //     var res = '';

                //     for(var x = 0; x < persones.length; x++){

                //         res += 'my name :' + persones[x].name + ' and my age :' + persones[x].age + "<button class='btn btn-danger ms-2' onclick='remove("+ x +")'>Remove</button><br>"; 
                //     }
                //     document.getElementById('resultat').innerHTML = res;

                // }


                // function remove(id){
                //     persones.splice(id, 1);
                //     view();
                // }





                ///////////////////////  ** $ for +
                // var name = "ossama";
                // var age = "19";
                // document.write(`my name is ${name} and my age ${age}`)

