const reserved = JSON.parse(document.getElementById('reserved').textContent);

oldRaw = document.getElementById('old')
old = oldRaw ? JSON.parse(oldRaw.textContent) : []

const wrapper = document.querySelector('#wrapper')

const generateSchema = (rows, seatsInRow) => {
    const schema = document.createElement('div')
    schema.setAttribute('id', 'schema')

    for(let i=1; i<=rows; i++){
        const row = document.createElement('div')
        row.setAttribute('id', String.fromCharCode(96 + i))
        row.setAttribute('class', 'row')
        
        for(let j=1; j<=seatsInRow; j++){
            const seat = document.createElement('div')
            seat.setAttribute('class', 'seat')

            const seatInput = document.createElement('input')
            seatInput.setAttribute('type', 'checkbox')
            seatInput.setAttribute('name', 'selected')
            seatInput.setAttribute('id', String.fromCharCode(96 + i)+'-'+j)
            seatInput.setAttribute('value', String.fromCharCode(96 + i)+'-'+j)

            const seatLabel = document.createElement('label')
            seatLabel.setAttribute('for', String.fromCharCode(96 + i)+'-'+j)
            seatLabel.innerText = seatInput.id

            if(old.includes(seatInput.id))
                seatInput.setAttribute('checked', 'true');
            else if(reserved.includes(seatInput.id))
                seatInput.setAttribute('disabled', 'true');

            if(i !== rows && [3, 4, 13, 14].includes(j)) {
                seatInput.setAttribute('disabled', 'true')
                seat.classList.add('hidden')
            }
                

            seat.appendChild(seatInput)
            seat.appendChild(seatLabel)
            
            row.appendChild(seat)
        }

        schema.appendChild(row)
    }

    return schema
}

wrapper && wrapper.appendChild(generateSchema(10, 16))
