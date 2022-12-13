var arr = []
let elementClicked = false
var buttons = document.getElementsByClassName('button');

for (i = 0; i < buttons.length; i++) {
   
  $(buttons[i]).click(function(){
    elementClicked = true
    var button_id = $(this).attr('id');
    arr.push(button_id)
    
    if(elementClicked) {
      $(this).css('border-color', 'black');
      elementClicked = false
      return;
    }
  })
  }

$('.add_cart').click(function(){
  console.log(arr)
  $.ajax({
    type: 'GET',           
    url : 'add-to-cart/',
    datatype: "json",
    data:{
      'size': arr[arr.length-1]
    },
    success: function(){
      console.log('success')
    },
    error: function(){
      console.log('Not a Success')
    }
  })
})
    




