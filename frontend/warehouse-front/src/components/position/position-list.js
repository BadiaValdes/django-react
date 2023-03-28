import React, {useEffect, useState} from 'react';
import {tableHeaderValues} from "../../config/table-values";
import {CustomTable} from "../table/custom-table";
import PositionForm from "./position-form";
import Button from "@mui/material/Button";
import {PositionService} from "../../service/position.service";
import Typography from "@mui/material/Typography";
import {BrandService} from "../../service/brand.service";
import AlertDialog from "../confirm-dialog/confirm";

function PositionList(props) {
    // useSate es un hook que nos permite cambiar los estados de variables en específico
    const [data, setData] = useState([])
    const [test, setTest] = useState({id: '', name: ''})
    const [showForm, setShowForm] = useState(false)
    const [showConfirm, setShowConfirm] = useState(false)
    const [deleteId, setDeleteId] = useState('')

    const header = tableHeaderValues
    // useEffect es un hook que nos permite realizar una acción cuando el componente se inicio
    // es utilizado mayourmente para llamadas hacia APIS

    useEffect(() => {
        reloadData()
    }, [])

    const editFunction = (id) => {
        PositionService.retrive(id).then((data) => {
            console.log(data)
            setTest({
                id: data.data.id,
                name: data.data.name
            })
            setShowForm(true);
        })
    }

    const cleanEdit = () => {
        setTest({id: '', name: ''})
    }

    const deleteFunction = (id) => {
        setDeleteId(id)
        setShowConfirm(true)
    }

    const del = () => {
        PositionService.delete(deleteId).then(() => reloadData())
    }

    const seeFunction = (id) => {
        console.log("ID " + id)
    }

    const reloadData = () => {
        PositionService.get().then((data) => setData(data.data
            )
        )
    }


    return (
        <>
            <Typography variant="h5" component={'h4'}>
                Posición
            </Typography>
            {showForm
                && <PositionForm dialogState={showForm}
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

            <CustomTable
                data={data}
                header={header}
                editFunction={editFunction}
                deleteFunction={deleteFunction}
            />
        </>
    );
}

export default PositionList;