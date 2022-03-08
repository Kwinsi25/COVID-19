
function update() {
    var select = document.getElementById('ward');
    var option = select.options[select.selectedIndex];

    if (option.value == 'General') {
        document.getElementById('collapseOne').className = 'collapse show';
    }
    else {
        document.getElementById('collapseOne').className = 'collapse';
    }
    if (option.value == 'Special') {
        document.getElementById('collapseTwo').className = 'collapse show';
    }
    else {
        document.getElementById('collapseTwo').className = 'collapse';
    }
    if (option.value == 'Emergency') {
        document.getElementById('collapseThree').className = 'collapse show';
    }
    else {
        document.getElementById('collapseThree').className = 'collapse';
    }
}

update();