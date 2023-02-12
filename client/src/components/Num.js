import React from 'react'
import { Button, Card ,Modal} from 'react-bootstrap';


const Num=({no})=>{
    return(
        <Card className="num">
            <Card.Body>
                <Card.No>{no}</Card.no>
            </Card.Body>
        </Card>
    )
}


export default Num;