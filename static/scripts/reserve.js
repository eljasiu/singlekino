const reserved = JSON.parse(document.getElementById('reserved').textContent);

const wrapper = document.querySelector('#wrapper')

const selected = []

const toggleSelect = id => {
    if(selected.includes(id)) {
        idx = selected.indexOf(id)
        selected.splice(idx, 1)
    }
    else {
        selected.push(id)
    }
}

const generateSchema = (rows, seatsInRow) => {
    const schema = document.createElement('div')
    schema.setAttribute('id', 'schema')

    for(let i=1; i<=rows; i++){
        const row = document.createElement('div')
        row.setAttribute('id', String.fromCharCode(96 + i))
        
        for(let j=1; j<=seatsInRow; j++){
            const seat = document.createElement('div')
            seat.setAttribute('id', String.fromCharCode(96 + i)+'-'+j)
            seat.setAttribute('class', 'seat')
            
            const isReserved = reserved.includes(seat.id)
            seat.innerText = isReserved ? seat.id+'*' : seat.id
            !isReserved && seat.addEventListener('click', () => toggleSelect(seat.id))
            
            row.appendChild(seat)
        }

        schema.appendChild(row)
    }

    return schema
}

wrapper.appendChild(generateSchema(8, 11))
