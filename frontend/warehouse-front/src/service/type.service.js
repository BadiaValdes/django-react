
export class TypeService {
    static tableTestValues = [{
        id: '324',
        name: 'Test 1',
    }]

    static get(){
        return TypeService.tableTestValues;
    }

    static create(data) {
        TypeService.tableTestValues.push(data)
    }
    static update(data) {
        TypeService.tableTestValues = TypeService.tableTestValues.map(dat => {
            if(dat.id == data.id){
                dat.name = data.name
            }
            return dat
        })
    }
    static delete(id) {
        TypeService.tableTestValues = TypeService.tableTestValues.filter(dat => dat.id !== id)
    }
}