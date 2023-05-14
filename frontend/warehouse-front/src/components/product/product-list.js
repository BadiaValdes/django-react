import React, {useEffect, useState} from 'react';
import {tableHeaderValues} from "../../config/table-values";
import {CustomTable} from "../table/custom-table";
import ProductForm from "./product-form";
import Button from "@mui/material/Button";
import {ProductService} from "../../service/product.service";
import Typography from "@mui/material/Typography";
import AlertDialog from "../confirm-dialog/confirm";
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Box from "@mui/material/Box";

function ProductList(props) {
    // useSate es un hook que nos permite cambiar los estados de variables en específico
    const [data, setData] = useState([])
    const [test, setTest] = useState({id: '',
        name: '', brand: '', quantity: '', position: '', photo: '', type: ''})
    const [showForm, setShowForm] = useState(false)
    const [showConfirm, setShowConfirm] = useState(false)
    const [deleteId, setDeleteId] = useState('')

    // useEffect es un hook que nos permite realizar una acción cuando el componente se inicio
    // es utilizado mayourmente para llamadas hacia APIS

    useEffect(() => {
        reloadData()
    }, [])

    const editFunction = (id) => {
        ProductService.retrive(id).then((data) => {
            setTest({
                id: data.data.id,
                name: data.data.name,
                brand: data.data.brand,
                quantity: data.data.quantity,
                position: data.data.position,
                photo: data.data.photo,
                type: data.data.type,
            })
            setShowForm(true);
        })
    }

    const cleanEdit = () => {
        setTest({
            id: '',
            name: '',
            brand: '',
            quantity: '',
            position: '',
            photo: '',
            type: '',
        })
    }

    const deleteFunction = (id) => {
        setDeleteId(id)
        setShowConfirm(true)
    }

    const del = () => {
        ProductService.delete(deleteId).then(() => reloadData())
    }

    const seeFunction = (id) => {
        console.log("ID " + id)
    }

    const reloadData = () => {
        ProductService.get().then((data) => {
                setData(data.data)
            }
        )
    }


    return (
        <>
            <Typography variant="h5" component={'h4'}>
                Productos
            </Typography>
            {showForm
                && <ProductForm dialogState={showForm}
                                setDialogState={setShowForm}
                                data={test}
                                clean={cleanEdit}
                                reloadData={reloadData}/>}
            {showConfirm &&
                <AlertDialog
                    deleteAction={del}
                    setConfirm={setShowConfirm}
                    confirm={showConfirm}
                />}
            <Button onClick={() => {
                cleanEdit();
                setShowForm(true);
            }}> Crear </Button>

            <Box sx={{'display': 'flex', 'flexDirection': 'row', 'gap': 5, 'flexWrap': 'wrap'}}>
            {data.map(dat => (
                <Card sx={{maxWidth: 345}}>
                    <CardMedia
                        sx={{height: 200}}
                        image={dat.photo}
                    />
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="div">
                            {dat.name}
                        </Typography>
                    </CardContent>
                    <CardActions>
                        <Button size="small">Detalles</Button>
                        <Button size="small" onClick={() => editFunction(dat.id)}>Modificar</Button>
                        <Button size="small" onClick={() => deleteFunction(dat.id)}>Eliminar</Button>
                    </CardActions>
                </Card>
            ))}
            </Box>

        </>
    );
}

export default ProductList;