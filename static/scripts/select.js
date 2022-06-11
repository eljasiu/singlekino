const reserved = JSON.parse(document.getElementById('reserved').textContent);

const wrapper = document.querySelector('#wrapper')

const generateSchema = (rows, seatsInRow) => {
    const schema = document.createElement('div')
    schema.setAttribute('id', 'schema')

    for(let i=1; i<=rows; i++){
        const row = document.createElement('div')
        row.setAttribute('id', String.fromCharCode(96 + i))
        
        for(let j=1; j<=seatsInRow; j++){
            const seat = document.createElement('div')
            seat.setAttribute('id', String.fromCharCode(96 + i)+'-'+j)

            const seatInput = document.createElement('input')
            seatInput.setAttribute('type', 'checkbox')
            seatInput.setAttribute('name', 'selected')
            seatInput.setAttribute('id', String.fromCharCode(96 + i)+'-'+j)
            seatInput.setAttribute('value', String.fromCharCode(96 + i)+'-'+j)
            reserved.includes(seatInput.id) && seatInput.setAttribute('disabled', 'true')

            const seatLabel = document.createElement('label')
            seatLabel.setAttribute('for', String.fromCharCode(96 + i)+'-'+j)
            seatLabel.innerText = reserved.includes(seatInput.id) ? seatInput.id+'*' : seatInput.id

            seat.appendChild(seatInput)
            seat.appendChild(seatLabel)
            
            row.appendChild(seat)
        }

        schema.appendChild(row)
    }

    return schema
}

wrapper && wrapper.appendChild(generateSchema(8, 11))
