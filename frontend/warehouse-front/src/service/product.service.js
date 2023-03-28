import axios from "axios";
import {httpLink} from "../config/http";

export class ProductService {
    static get() {
        return axios.get(httpLink + 'productGLC');
    }

    static retrive(id) {
        return axios.get(httpLink + 'productGRUD/' + id);
    }

    static create(data) {
        const formData = new FormData();
        formData.append('name', data.name)
        formData.append('quantity', data.quantity)
        formData.append('brand', data.brand)
        formData.append('type', data.type)
        formData.append('position', data.position)
        formData.append('photo', data.photo)
        console.log(formData.get('type'))
        return axios.post(httpLink + 'productGLC', formData, {
            headers: {
                "Content-Type": 'multipart/form-data'
            }
        })
    }

    static update(data) {
        const formData = new FormData();
        formData.append('name', data.name)
        formData.append('quantity', data.quantity)
        formData.append('brand', data.brand)
        formData.append('type', data.type)
        formData.append('position', data.position)
        if (data.photo)
            formData.append('photo', data.photo)
        return axios.put(httpLink + 'productGRUD/' + data.id, formData, {
            headers: {
                "Content-Type": 'multipart/form-data'
            }
        })
    }

    static delete(id) {
        return axios.delete(httpLink + 'productGRUD/' + id)
    }
}