import React, {useEffect, useState} from 'react';
import {tableHeaderValues} from "../../config/table-values";
import {CustomTable} from "../table/custom-table";
import BrandForm from "./brand-form";
import Button from "@mui/material/Button";
import {BrandService} from "../../service/brand.service";
import Typography from "@mui/material/Typography";

function BrandList(props) {
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
        const value = BrandService.tableTestValues.filter(dat => dat.id == id)[0]
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
        BrandService.delete(id)
        reloadData()
    }

    const seeFunction = (id) => {
        console.log("ID " + id)
    }

    const reloadData = () => {
        setData(BrandService.get())
    }


    return (
        <>
            <Typography  variant="h5"  component={'h4'}>
                Marca
            </Typography>
            {showForm
                && <BrandForm dialogState={showForm}
                              setDialogState={setShowForm}
                              data={test}
                              clean={cleanEdit}
                              reloadData={reloadData}/>}
            <Button onClick={() => {
                cleanEdit();
                setShowForm(true);
            }}> Crear </Button>

            <CustomTable
                data={BrandService.get()}
                header={header}
                editFunction={editFunction}
                deleteFunction={deleteFunction}
                />
        </>
    );
}

export default BrandList;