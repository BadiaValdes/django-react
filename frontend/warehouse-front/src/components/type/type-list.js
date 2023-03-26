import React, {useEffect, useState} from 'react';
import {tableHeaderValues} from "../../config/table-values";
import {CustomTable} from "../table/custom-table";
import TypeForm from "./type-form";
import Button from "@mui/material/Button";
import {TypeService} from "../../service/type.service";
import Typography from "@mui/material/Typography";

function TypeList(props) {
    // useSate es un hook que nos permite cambiar los estados de variables en específico
    const [data, setData] = useState([])
    const [test, setTest] = useState({id: '', name: ''})
    const [showForm, setShowForm] = useState(false)

    const header = tableHeaderValues
    // useEffect es un hook que nos permite realizar una acción cuando el componente se inicio
    // es utilizado mayourmente para llamadas hacia APIS

    useEffect(() => {
        reloadData()
    }, [])

    const editFunction = (id) => {
        const value = TypeService.tableTestValues.filter(dat => dat.id == id)[0]
        setTest({
            id: value.id,
            name: value.name
        })
        setShowForm(true);
    }

    const cleanEdit = () => {
        setTest({id: '', name: ''})
    }

    const deleteFunction = (id) => {
        TypeService.delete(id)
        reloadData()
    }

    const seeFunction = (id) => {
        console.log("ID " + id)
    }

    const reloadData = () => {
        setData(TypeService.get())
    }


    return (
        <>
            <Typography variant="h5" component={'h4'}>
                Tipo de producto
            </Typography>
            {showForm
                && <TypeForm dialogState={showForm}
                             setDialogState={setShowForm}
                             data={test}
                             clean={cleanEdit}
                             reloadData={reloadData}/>}
            <Button onClick={() => {
                cleanEdit();
                setShowForm(true);
            }}> Crear </Button>

            <CustomTable
                data={TypeService.get()}
                header={header}
                editFunction={editFunction}
                deleteFunction={deleteFunction}
            />
        </>
    );
}

export default TypeList;