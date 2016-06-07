$(document).ready(function(){
	$("input:checkbox.checkbox").change(function(){
		var val = $(this).val();
		var id = "#" + $(this).attr('id');
		if($(id).is(':checked')){
			res=1
		}else{
			res=0
		}
		$.ajax({
			type: 'POST',
			url :'/',
			data: {
				res : res,
				value: val,
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success: function(){
				console.log("it works")				
				window.location = window.location.href;
			}
		});
	});
});
