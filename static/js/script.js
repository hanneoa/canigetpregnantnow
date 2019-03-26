

// This is the slider JavaScript //
  $("#customRange1").change(function(){
    var newValue = $('#customRange1').val();
    console.log(newValue);
    $("#sliderValue").text(newValue);
  });
// This is the end of slider JavaScript //
