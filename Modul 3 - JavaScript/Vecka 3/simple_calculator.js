function calculate(sign) {
    let num1 = parseFloat(document.getElementById('num1').value);
    let num2 = parseFloat(document.getElementById('num2').value);
    let result = 0;
    if (sign=='+'){
         result = num1 + num2;

    }
    else if (sign=='-'){
         result = num1 - num2;
    }
    else if (sign=='*'){
         result = num1 * num2;
    }
    else if (sign=='/'){
         result = num1 / num2;
    }
    else{
         result = 'Error';
    }
    document.getElementById('result').innerText = 'Result: ' + result;
}

