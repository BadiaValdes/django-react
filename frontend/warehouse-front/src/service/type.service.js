import axios from "axios";
import {httpLink} from "../config/http";

export class TypeService {
    static get(){
        return axios.get(httpLink + 'type');
    }

    static retrive(id){
        return axios.get(httpLink + 'type/' + id);
    }

    static create(name) {
        return axios.post(httpLink + 'type', {
            name: name
        })
    }
    static update(data) {
        return axios.put(httpLink + 'type/' + data.id, {
            id: data.id,
            name: data.name
        })
    }
    static delete(id) {
        return axios.delete(httpLink + 'type/' + id)
    }
}