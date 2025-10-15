    function string()
    {
    let a1=document.getElementById("s").value;
    if(a1=="") {
        alert('enter something with letter a');
        return;
    }
    let a2=a1.length;
    document.getElementById("a").value=a2;
    let b2=a1.substring(2,4);
    document.getElementById("b").value=b2;
    let c2=a1.search("a");
    document.getElementById("c").value=c2;
    let d2=a1.indexOf("a");
    document.getElementById("d").value=d2;
    let e2=a1.replace("a","x");
    document.getElementById("e").value=e2;
    let f2 =a1.toUpperCase();
    document.getElementById("f").value=f2;
     let g2=a1.concat("hello");
    document.getElementById("g").value=g2;
     let h2=a1.substr(2,4);
    document.getElementById("h").value=h2;
     let i2=a1.slice(2,4);
    document.getElementById("i").value=i2;
     let j2=a1.lastIndexOf("a");
    document.getElementById("j").value=j2;
    }