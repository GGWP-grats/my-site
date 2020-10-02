let bg = document.getElementById("bg");
let star = document.getElementById("death_star");
let mountain = document.getElementById("mountain");
let hello = document.getElementById("hello");
let text = document.getElementById("text");
let road = document.getElementById("road");

window.addEventListener('scroll', function(){
	var value = window.scrollY;

	mountain.style.top = -value * 0.1 + 'px';
	hello.style.top = value * 0.7 + 'px';
})
