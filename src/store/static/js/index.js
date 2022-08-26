
// const xhr = new XMLHttpRequest()
// const size = document.querySelectorAll('div.size > p ');

// for (i =0; i < size.length;i++){
//     size[i].addEventListener("click", () => {
//         xhr.open("GET", 'product/<str:slug>/add-to-cart/')
//         xhr.responseType = "text"
//         xhr.send();
//         xhr.onload = function(){
//             //Si le statut HTTP n'est pas 200...
//             if (xhr.status != 200){ 
//                 //...On affiche le statut et le message correspondant
//                 alert("Erreur " + xhr.status + " : " + xhr.statusText);
//             //Si le statut HTTP est 200, on affiche le nombre d'octets téléchargés et la réponse
//             }else{ 
//                 alert(xhr.response.length + " octets  téléchargés\n" + JSON.stringify(xhr.response));
//             }
//         };
    
//     })
// };
// function getClickID(clickID) {
//     alert(clickID);
// }
// $('#buttonId').click(function() {    
//     $.ajax({
//         url: your_url,
//         method: 'POST', // or another (GET), whatever you need
//         data: {
//             name: value, // data you need to pass to your function
//             click: true
//         }
//         success: function (data) {        
//             // success callback
//             // you can process data returned by function from views.py
//         }
//     });
// });
