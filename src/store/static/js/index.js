function RequeteAjax(){

    $('.button').click(function() {
        
        var button_id = $(this).attr('id');
        console.log(button_id)
    $.ajax({
      type: 'GET',           
      url : 'add-to-cart', 
      datatype: "json",
      data:{
        'size': button_id 
      },
      success: function(response){
        let data = JSON.stringify(data);
        console.log(data)
      },
      error: function(){
        console.log('pas ok')
      }
   });
  });
};    
