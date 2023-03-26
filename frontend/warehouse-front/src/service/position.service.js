
export class PositionService {
    static tableTestValues = [{
        id: '324',
        name: 'Test 1',
    }]

    static get(){
        return PositionService.tableTestValues;
    }

    static create(data) {
        PositionService.tableTestValues.push(data)
    }
    static update(data) {
        PositionService.tableTestValues = PositionService.tableTestValues.map(dat => {
            if(dat.id == data.id){
                dat.name = data.name
            }
            return dat
        })
    }
    static delete(id) {
        PositionService.tableTestValues = PositionService.tableTestValues.filter(dat => dat.id !== id)
    }
}