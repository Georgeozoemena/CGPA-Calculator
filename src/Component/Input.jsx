import React from 'react'

function Input(input){
    return(
        <div className="input">
            <input type={input.type} placeholder={input.placeholder} id={input.id} />
        </div>
    )
}

export default Input