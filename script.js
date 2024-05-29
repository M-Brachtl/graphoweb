let people = document.querySelectorAll('tbody tr');
let data = [];

function evaluatePoints(points) {
    people.forEach(person => {
        const points = Array.from(person.querySelectorAll('.points-input')).map(pnt => pnt.value);
        const total = points.reduce((acc,val) => acc + (isNaN(parseInt(val)) ? 0 : parseInt(val)),0);
        //const total = points.reduce((acc, val) => acc + val);
        person.querySelector('.result').textContent = total
    });
}

document.querySelectorAll('.points-input').forEach(input => {
    input.addEventListener('input', evaluatePoints);
});

function addRow() {
    const table = document.querySelector('tbody');
    const newRow = document.createElement('tr');
    table.appendChild(newRow);
    newRow.innerHTML = '<td><input type="text" placeholder="Jméno"></td>';
    const cols = document.querySelector('thead').querySelector('tr').children.length - 2;
    for (let i = 0; i < cols; i++) {
        newRow.innerHTML += '<td><input type="text" class="points-input" placeholder="0"></td>'; // add placeholder
    };
    newRow.innerHTML += '<td class="result">0</td>';
    people = document.querySelectorAll('tbody tr');
    newRow.querySelectorAll('.points-input').forEach(row => row.addEventListener('input', evaluatePoints));
    console.log(newRow.querySelectorAll('.points-input'));
}

function removeRow() {
    const table = document.querySelector('tbody');
    const rowCount = table.querySelectorAll('tr').length;
    while (table.querySelectorAll('tr').length === rowCount) table.removeChild(table.lastChild);
    people = document.querySelectorAll('tbody tr');
};

function closeGraph(){
    document.querySelector('.graph').style.top = "calc(100vh + 50%)";
    document.querySelectorAll('.blur').forEach(blur => blur.classList.remove('blur'));
}

async function openGraph(){
    // get graph png code
    let newData = [];
    people.forEach(person => {
        const points = Array.from(person.querySelectorAll('.points-input')).map(pnt => pnt.value || 0);
        const name = person.querySelector('input').value;
        newData.push({'name': name, 'points': points});
    });
    console.log(JSON.stringify(newData)!=JSON.stringify(data))
    if (JSON.stringify(newData)!=JSON.stringify(data)) {
        data = newData;
        console.log(JSON.stringify([data,Array.from(document.querySelectorAll('.headInput')).map(input => input.value)]));
        const response = await fetch('http://localhost:8000/get_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify([data,Array.from(document.querySelectorAll('.headInput')).map(input => input.value)])
        })
        const answer = await response.json();
        console.log(answer);
        document.querySelector('.graph img').src = "http://localhost:8000/graph?" + new Date().getTime(); // čas pro reload
    }
    ///
    // document.querySelector('.graph').style.display = 'flex';
    document.querySelector('.graph').style.top = '49vh';
    document.querySelector('.container').classList.add('blur');
    document.querySelector('.buttons').classList.add('blur');
}
document.querySelector('.graph button').addEventListener('click', closeGraph);