$(document).ready(function(){
    start(); 
});

// these three functions are so similar whoops
function start(){ 
    var startBubble = "<div class='row bot-response-wrapper'>"
    startBubble +="<div class='row left'>"; 
    startBubble += "<div class='chip'>"; 
    startBubble += "<img src='http://imagecdn.godvine.com/pics/GV-Article/dogsmiles-2.jpg'>"; 
    startBubble += "Hey there! I'm Impostor Bot! I do things, I guess"; 
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
    thinking += "Generating a tweet from user @" + user +"..."; 
    thinking += "<img src='http://imagecdn.godvine.com/pics/GV-Article/dogsmiles-2.jpg'>"; 
    thinking += "</div>"
    thinking += "</div>"
    
    $('.bot-chats').append($(thinking).hide().fadeIn(500));
    $('.bot-section').animate({scrollTop: $('.bot-section')[0].scrollHeight - $('.bot-section').height()}, 300); 
}