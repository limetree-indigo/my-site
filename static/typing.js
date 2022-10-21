content= "Jonathan's Home" // 사용할 문구
text = document.querySelector('#typing-text')
index = 0; // 문자열 인덱스

function typing() {
    text.textContent += content[index++];
    if(index > content.length){
        text.textContent = "";
        index = 0;
    }
}
setInterval(typing, 200);