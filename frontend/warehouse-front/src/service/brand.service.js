
export class BrandService {
    static tableTestValues = [{
        id: '324',
        name: 'Test 1',
    }]

    static get(){
        return BrandService.tableTestValues;
    }

    static create(data) {
        BrandService.tableTestValues.push(data)
    }
    static update(data) {
        BrandService.tableTestValues = BrandService.tableTestValues.map(dat => {
            if(dat.id == data.id){
                dat.name = data.name
            }
            return dat
        })
    }
    static delete(id) {
        BrandService.tableTestValues = BrandService.tableTestValues.filter(dat => dat.id !== id)
    }
}