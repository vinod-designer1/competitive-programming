function send_cal_data (inp1, inp2) {
	var data = {
		'inp1': inp1,
		'inp2': inp2
	};

	$.ajax({
		type:"POST",
		url:"demo_test.txt",
		data: data,
		success:function(response){
			$('#feed').html(response);
		}
	});
}

$( document ).ready(function() {
	$('input[type=text]').blur(function() {
		var val = $(this).val();
		if (val != parseFloat(val)) {
			alert('only numbers allowed');
		}
		$(this).val(parseFloat(val));
	});

	$(document).keypress(function(e) {
		if(e.which == 13) {
			var inp1 = parseFloat($('#inp1').val());
			var inp2 = parseFloat($('#inp2').val());
			$('#solution').html(inp1+inp2);
		}
	});
});