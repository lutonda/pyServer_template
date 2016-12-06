$(function(){
	$('#btnSignUp').click(function(){
		
		$.ajax({
			url: '/signUp',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				alert(response);
			},
			error: function(error){
				alert(error);
			}
		});
	});
});
