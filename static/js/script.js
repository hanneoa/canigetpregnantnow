

// This is the slider JavaScript //
  $("#customRange1").change(function(){
    var newValue = $('#customRange1').val();
    console.log(newValue);
    $("#sliderValue").text(newValue);
  });
// This is the end of slider JavaScript //

// this is the calendar jscode (uses jquery)

$(function() {
  $( ".calendar" ).datepicker({
		dateFormat: 'dd/mm/yy',
		firstDay: 1
	});

	$(document).on('click', '.date-picker .input', function(e){
		var $me = $(this),
				$parent = $me.parents('.date-picker');
		$parent.toggleClass('open');
	});


	$(".calendar").on("change",function(){
		var $me = $(this),
				$selected = $me.val(),
				$parent = $me.parents('.date-picker');
		$parent.find('.result').children('span').html($selected);
	});
});
