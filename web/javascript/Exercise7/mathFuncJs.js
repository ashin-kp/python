function math() {
    let val1 = document.getElementById('n1').value;
    let val2 = document.getElementById('n2').value;

    document.getElementById('round').value = Math.round(val1);
    document.getElementById('ceil').value = Math.ceil(val1);
    document.getElementById('floor').value = Math.floor(val1);
    document.getElementById('trunc').value = Math.trunc(val1);
    document.getElementById('sign').value = Math.sign(val1);
    document.getElementById('power').value = Math.pow(val1,val2);
    document.getElementById('sqrt').value = Math.sqrt(val1);
    document.getElementById('sine').value = Math.sin(val1);
    document.getElementById('min').value = Math.min(val1,val2);
    document.getElementById('max').value = Math.max(val1,val2);
    document.getElementById('random').value = Math.random(1,10);
}