import axios from "axios";
import {httpLink} from "../config/http";

export class PositionService {
    static get(){
        return axios.get(httpLink + 'position');
    }

    static retrive(id){
        return axios.get(httpLink + 'position/' + id);
    }

    static create(name) {
        return axios.post(httpLink + 'position', {
            name: name
        })
    }
    static update(data) {
        return axios.put(httpLink + 'position/' + data.id, {
            id: data.id,
            name: data.name
        })
    }
    static delete(id) {
        return axios.delete(httpLink + 'position/' + id)
    }
}