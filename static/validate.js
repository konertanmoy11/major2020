function validate(){
    var pass1=document.getElementById("pwd").value;
    var pass2=document.getElementById("cpwd").value;
    if(pass1!=pass2){
        alert("Passwords don't match!");
        return false;
    }
    return true;
}
