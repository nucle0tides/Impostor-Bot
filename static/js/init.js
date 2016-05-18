$(document).ready(function(){
    start(); 
});
// these three functions are so similar whoops
function start(){ 
    var startBubble = "<div class='row bot-response-wrapper'>"
    startBubble +="<div class='row left'>"; 
    startBubble += "<div class='chip'>"; 
    startBubble += "<img src='http://imagecdn.godvine.com/pics/GV-Article/dogsmiles-2.jpg'>"; 
    startBubble += "Hey there! I am Impostor Bot. To use me, please type a public Twitter handle and press 'Submit'!"; 
    startBubble += "</div>"
    startBubble += "</div>"
    
    $('.bot-chats').append($(startBubble).hide().fadeIn(500)); 
}

function add_tweet(response, picture)
{ 
    var tweet = "<div class='row bot-response-wrapper'>"
    tweet +="<div class='row right'>"; 
    tweet += "<div class='chip blue white-text'>"; 
    tweet += "<img src='"+picture+"' class='left'>"; 
    tweet += response; 
    tweet += "</div>"
    tweet += "</div>"
    
    $('.bot-chats').append($(tweet).hide().fadeIn(500));
}

function thinking(user)
{ 
    var thinking = "<div class='row bot-response-wrapper'>"
    thinking +="<div class='row left'>"; 
    thinking += "<div class='chip'>"; 
    thinking += "<img src='http://imagecdn.godvine.com/pics/GV-Article/dogsmiles-2.jpg'>"; 
    thinking += "Generating a tweet from user @" + user +"..."; 
    thinking += "</div>"
    thinking += "</div>"
    
    $('.bot-chats').append($(thinking).hide().fadeIn(500));
    $('.bot-section').animate({scrollTop: $('.bot-section')[0].scrollHeight - $('.bot-section').height()}, 300); 
}

function warning()
{ 
    var warn = "<div class='row bot-response-wrapper'>"
    warn +="<div class='row left'>"; 
    warn += "<div class='chip'>"; 
    warn += "<img src='http://imagecdn.godvine.com/pics/GV-Article/dogsmiles-2.jpg'>"; 
    warn += "Woah there! You did not enter a user!"; 
    warn += "</div>"
    warn += "</div>"
    
    $('.bot-chats').append($(warn).hide().fadeIn(500));
    $('.bot-section').animate({scrollTop: $('.bot-section')[0].scrollHeight - $('.bot-section').height()}, 300); 
}

function do_that_thing()
{
  var twitter_pic = null; 
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      add_tweet(xhttp.responseText, twitter_pic); 
      $('.bot-section').animate({scrollTop: $('.bot-section')[0].scrollHeight - $('.bot-section').height()}, 300); 
    }
  };
  
  var xhttp_pic = new XMLHttpRequest();
  xhttp_pic.onreadystatechange = function() {
    if (xhttp_pic.readyState == 4 && xhttp_pic.status == 200) { 
      twitter_pic = xhttp_pic.responseText; 
    }
  };
  var user = document.getElementById('twitter_input').value
  if(user){ 
    xhttp_pic.open("GET", "/getPic/" + user, true);
    xhttp_pic.send();
    xhttp.open("GET", "/getTweet/" + user, true);
    thinking(user); 
    xhttp.send();   
  }
  else{ 
    //   console.log("no user")
      warning(); 
  }
}