import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../auth'
import Num from './Num'
import { Modal ,Form,Button} from 'react-bootstrap'
import { useForm } from 'react-hook-form'





const LoggedinHome = () => {
    const [nums, setNums] = useState([]);
    const [show, setShow] = useState(false)
    const {register,reset,handleSubmit,setValue,formState:{errors}}=useForm()
    const [numId,setNumId]=useState(0);

    useEffect(
        () => {
            fetch('/num/nums')
                .then(res => res.json())
                .then(data => {
                    setNums(data)
                })
                .catch(err => console.log(err))
        }, []
    );

    const getAllNums=()=>{
        fetch('/num/nums')
        .then(res => res.json())
        .then(data => {
            setNums(data)
        })
        .catch(err => console.log(err))
    }
    

    const closeModal = () => {
        setShow(false)
    }

    const showModal = (id) => {
        setShow(true)
        setNumId(id)
        nums.map(
            (num)=>{
                if(num.id==id){
                    setValue('no',num.no)
                }
            }
        )
    }


    let token=localStorage.getItem('REACT_TOKEN_AUTH_KEY')



    return (
        <div className="nums container">
            <Modal
                show={show}
                size="lg"
                onHide={closeModal}
            >
            </Modal>
            <h1>List of Nums</h1>
            {
                nums.map(
                    (num,index) => (
                        <Num
                             no={num.no}
                            key={index}
                            onClick={()=>{showModal(num.id)}}
                        />
                    )
                )
            }
        </div>
    )
}


const LoggedOutHome = () => {
    return (
        <div className="home container">
            <h1 className="heading">Welcome to the Nums</h1>
            <Link to='/signup' className="btn btn-primary btn-lg">Get Started</Link>
        </div>
    )
}

const HomePage = () => {

    const [logged] = useAuth()

    return (
        <div>
            {logged ? <LoggedinHome /> : <LoggedOutHome />}
        </div>
    )
}

export default HomePage