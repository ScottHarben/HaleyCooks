$(function(){

  //Recipes dropdown menu
  $('#top-nav-items-recipes').on('click', function() {
    if($('.dropdown-container').attr('id') === "dropdown-show"){
      $('.dropdown-container').attr('id','dropdown-hide');
    } else {
      $('.dropdown-container').attr('id','dropdown-show');
    }
  });

  //Hamburger menu
  $('#menu-btn').on('click', function() {
    if ($('.mid-nav').css('display') !== 'block'){
      $('.mid-nav').css('display','block');
    } else {
      $('.mid-nav').css('display','none');
    }
  });

  //click outside of dropdown menu
  $(document).on('click', function(e) {
    if (!$(e.target).closest('#recipe-nav').length){
      if($('.dropdown-container').attr('id') === "dropdown-show"){
        $('.dropdown-container').attr('id','dropdown-hide');
      }
    }
  });
  //click outside of hamburger menu
  $(document).on('click', function(e) {
    if (!$(e.target).closest('.top-nav-container').length){
      if ($('.mid-nav').css('display') === 'block'){
        $('.mid-nav').css('display','none');
      }
    }
  });

});
