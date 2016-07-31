$(document).ready(ready);

function ready(){
	$('.dt').dataTable({
		'pagelength':25,
		'scrollY':true,
		'ordering':true
	});
	$('.dt').css({'width':'100%'})
	$('#flashInfo').css({'visibility':hidden})
}