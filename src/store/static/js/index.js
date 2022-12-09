function RequeteAjax(){

    $('.button').ready(function() {   
      var button_id = $('.button').attr('id');

      $.ajax({
        type: 'GET',           
        url : 'add-to-cart/',
        datatype: "json",
        data:{
          'size': button_id 
        },
        success: function(){
          console.log('Success')
        },
        error: function(){
          console.log('Not a Success')
        }
   });
  });
};    

