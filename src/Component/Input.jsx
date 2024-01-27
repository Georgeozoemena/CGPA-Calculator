import React from 'react'

function Input(props){
    return(
        <div className="container">
            <input type={props.type} placeholder={props.placeholder} id={props.id} />
        </div>
    )
}

export default Input