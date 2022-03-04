
function update() {
    var select = document.getElementById('ward');
    var option = select.options[select.selectedIndex];

    if (option.value == 'A') {
        document.getElementById('collapseOne').className = 'collapse show';
    }
    else {
        document.getElementById('collapseOne').className = 'collapse';
    }
    if (option.value == 'B') {
        document.getElementById('collapseTwo').className = 'collapse show';
    }
    else {
        document.getElementById('collapseTwo').className = 'collapse';
    }
    if (option.value == 'C') {
        document.getElementById('collapseThree').className = 'collapse show';
    }
    else {
        document.getElementById('collapseThree').className = 'collapse';
    }
}

update();