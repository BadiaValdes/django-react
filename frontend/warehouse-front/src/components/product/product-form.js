import React, {useEffect, useState} from 'react';
import {Dialog, DialogActions, DialogContent, DialogTitle, Select, TextField} from "@mui/material";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import {PositionService} from "../../service/position.service";
import {ProductService} from "../../service/product.service";
import Box from "@mui/material/Box";
import {BrandService} from "../../service/brand.service";
import {TypeService} from "../../service/type.service";
import MenuItem from "@mui/material/MenuItem";

function ProductForm(props) {
    const [name, setName] = useState('')
    const [photo, setPhoto] = useState('')
    const [quantity, setQuantity] = useState(0)
    const [brand, setBrand] = useState('')
    const [position, setPosition] = useState('')
    const [type, setType] = useState('')
    const [dbBrand, setdbBrand] = useState([])
    const [dbPosition, setdbPosition] = useState([])
    const [dbType, setdbType] = useState([])
    const [localImage, setLocalImage] = useState('')
    const [initialImage, setInitialImage] = useState('')
    const [error, setError] = useState({
        name: false,
        photo: false,
        quantity: false,
        brand: false,
        position: false,
        type: false,
    })

    useEffect(() => {
        if (props.data.id != '') {
            setName(props.data.name)
            setPhoto(props.data.photo)
            setQuantity(props.data.quantity)
            setBrand(props.data.brand)
            setPosition(props.data.position)
            setType(props.data.type)
            setLocalImage(props.data.photo)
            setInitialImage(props.data.photo)
        }

        BrandService.get().then((data) => setdbBrand(data.data))
        PositionService.get().then((data) => setdbPosition(data.data))
        TypeService.get().then((data) => setdbType(data.data))
    }, [])

    const createBrand = () => {

        if (props.data.id == '') {
            ProductService.create(
                {
                    name: name,
                    quantity: quantity,
                    brand: brand,
                    type: type,
                    position: position,
                    photo: photo

                }
            ).then(() => props.reloadData()
            )
        } else {
            const data = {
                id: props.data.id,
                name: name,
                quantity: quantity,
                brand: brand,
                type: type,
                position: position,
            }

            if (initialImage !== photo) {
                data['photo'] = photo
            }

            ProductService.update(data).then(() => props.reloadData()
            )
            props.clean()
        }
        hide()
    }

    const clear = () => {
        setName('')
    }

    const hide = () => {
        clear()
        props.setDialogState(false)
    }

    const stopDropPropagation = (e) => {
        e.stopPropagation();
        e.preventDefault();
    }

    const handleDrop = (e) => {
        stopDropPropagation(e)
        setPhoto(e.dataTransfer.files[0])
        setLocalImage(URL.createObjectURL(e.dataTransfer.files[0]))
    }

    return (
        <Dialog open={props.dialogState}
                style={{width: '100vw'}}
        >
            <DialogTitle>
                <Typography component={'h6'}> Crear Producto </Typography>
            </DialogTitle>
            <DialogContent sx={{'display': 'flex', 'flexDirection': 'column', 'gap': 5, 'width': '500px'}}>
                <TextField id="standard-basic" label="Nombre" variant="standard" value={name}
                           onChange={(e) => setName(e.target.value.trim())}/>
                <TextField
                    id="outlined-number"
                    variant="standard"
                    label="Cantidad"
                    type="number"
                    error={error.quantity}
                    InputLabelProps={{
                        shrink: true,
                    }}
                    value={quantity}

                    onInput={(e) => {
                        if (!(+e.target.value)) {
                            setError({...error, quantity: true})
                        } else {
                            setError({...error, quantity: false})
                        }
                    }}

                    onChange={(e) => {
                        setQuantity(e.target.value)
                        console.log(quantity)


                    }

                    }
                />


                <Select
                    labelId="demo-simple-select-label"
                    variant="standard"
                    id="demo-simple-select"
                    value={brand}
                    label="Marca"
                    onChange={(e) => setBrand(e.target.value)}
                >
                    {dbBrand.map((dat) => (<MenuItem key={dat.id} value={dat.id}>{dat.name}</MenuItem>))}
                </Select>


                <Select
                    labelId="demo-simple-select-label"
                    variant="standard"
                    id="demo-simple-select"
                    value={position}
                    label="Marca"
                    onChange={(e) => setPosition(e.target.value)}
                >
                    {dbPosition.map((dat) => (<MenuItem key={dat.id} value={dat.id}>{dat.name}</MenuItem>))}
                </Select>


                <Select
                    labelId="demo-simple-select-label"
                    variant="standard"
                    id="demo-simple-select"
                    value={type}
                    label="Marca"
                    onChange={(e) => setType(e.target.value)}
                >
                    {dbType.map((dat) => (<MenuItem key={dat.id} value={dat.id}>{dat.name}</MenuItem>))}
                </Select>

                <div style={{'width': '100%', 'height': '200px', 'border': 'solid blue 1px', 'overflow': 'auto'}}
                     onDrag={(e) => stopDropPropagation(e)}
                     onDrop={(e) => {
                         handleDrop(e)
                     }}
                     onDragOver={(e) => stopDropPropagation(e)}
                >
                    {localImage
                        ? <img src={localImage} width={200} height={200} draggable={false}/>
                        : <Typography component={"h4"}>Arrastre la imagen aquí</Typography>}
                </div>


            </DialogContent>
            <DialogActions>
                <Box>
                    <Button disabled={name == ''} onClick={() => createBrand()}>Aceptar</Button>
                    <Button onClick={() => hide()}>Cancelar</Button>
                </Box>
            </DialogActions>
        </Dialog>
    );
}

export default ProductForm;