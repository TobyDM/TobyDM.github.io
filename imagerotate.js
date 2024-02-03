imgind = 1;
function nextimage(page,imgtotal) {
    imgind ++;
    if (imgind>imgtotal){
        imgind = 1;
    }
    document.getElementById("myimage").src = `./content/${page}/images/img${imgind}.jpeg`;
}
function previmage(page,imgtotal) {
    imgind --;
    if (imgind<1){
        imgind = imgtotal;
    }
    document.getElementById("myimage").src = `./content/${page}/images/img${imgind}.jpeg`;
}