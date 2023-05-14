import axios from "axios";
import {httpLink} from "../config/http";

export class BrandService {
    static get(){
        return axios.get(httpLink + 'brand');
    }

    static retrive(id){
        return axios.get(httpLink + 'brand/' + id);
    }

    static create(name) {
        return axios.post(httpLink + 'brand', {
            name: name
        })
    }
    static update(data) {
       return axios.put(httpLink + 'brand/' + data.id, {
           id: data.id,
           name: data.name
       })
    }
    static delete(id) {
        return axios.delete(httpLink + 'brand/' + id)
    }
}