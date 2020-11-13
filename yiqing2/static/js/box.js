var area=document.getElementById("box");
area.innerHTML+=area.innerHTML;
var liHeight=20;
area.scrollTop=0;
var delay=2000;
var speed=50;
var time;
function starMove(){
  area.scrollTop++;
  time=setInterval("scrollUp()",speed);
}
function scrollUp(){
  if(area.scrollTop%liHeight==0){
  clearInterval(time);
  setTimeout("starMove()",delay);
  }else{
  area.scrollTop++;
  if(area.scrollTop>=area.offsetHeight/2){
  area.scrollTop=0;
  }
  }
}
setTimeout("starMove()",delay);