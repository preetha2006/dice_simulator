let dice=document.getElementById("dice")
let rollbtn=document.getElementById("roll")
let resetbtn=document.getElementById("reset")

let dicecontent=[
    'source/1.png',
    'source/2.png',
    'source/3.png',
    'source/4.png',
    'source/5.png',
    'source/6.png'
]

rollbtn.addEventListener("click",function(){
    let randInd=Math.floor(Math.random()*6);
    dice.src=dicecontent[randInd];
})


resetbtn.addEventListener("click",function(){
    dice.src='source/dice.webp';
})