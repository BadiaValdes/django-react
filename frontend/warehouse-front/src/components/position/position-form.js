import React, {useEffect, useState} from 'react';
import {Dialog, DialogActions, DialogContent, DialogTitle, TextField} from "@mui/material";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import {PositionService} from "../../service/position.service";
import Box from "@mui/material/Box";

function PositionForm(props) {
    const [name, setName] = useState('')

    useEffect(() => {
        if (props.data.id != '') {
            setName(props.data.name)
        }
    }, [])

    const createBrand = () => {

        if (props.data.id == '') {
            PositionService.create(name).then(() => props.reloadData()
            )
        } else {
            const data = {
                id: props.data.id,
                name: name
            }
            PositionService.update(data).then(() => props.reloadData()
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

    return (
        <Dialog open={props.dialogState} breakpoints={{'960px': '75vw'}}
                style={{width: '50vw'}}
                onHide={() => hide()}>
            <DialogTitle>
                <Typography component={'h6'}> Crear Marca </Typography>
            </DialogTitle>
            <DialogContent>
                <TextField id="standard-basic" label="Standard" variant="standard" value={name}
                           onChange={(e) => setName(e.target.value.trim())}/>
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

export default PositionForm;