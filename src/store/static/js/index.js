var arr = []
var buttons = document.getElementsByClassName('button');

$(document).ready(function(){

  for (i = 0; i < buttons.length; i++) {
   
    $(buttons[i]).click(function(){
      var button_id = $(this).attr('id');
      arr.push(button_id)
      for (i = 0; i < buttons.length; i++) {
        $(buttons[i]).css('border-color', 'grey')
      }
      $(this).css('border-color', 'black');
      })
  }

  $('.add_cart').click(function(){

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
})
