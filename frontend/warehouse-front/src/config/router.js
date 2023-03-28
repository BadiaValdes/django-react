import {createBrowserRouter} from "react-router-dom";
import Layout from "../layout/layout";
import BrandList from "../components/brand/brand-list";
import PositionList from "../components/position/position-list";
import TypeList from "../components/type/type-list";
import ProductList from "../components/product/product-list";

export const route = createBrowserRouter([
    {
        path: "",
        element:
            <Layout/>
        ,
        children: [
            {
                path: "",
                element: <div>Inside Produc 2t</div>,

            },
            {
                path: "product/",
                element: <ProductList/>,

            },
            {
                path: "brand/",
                element: <BrandList/>,

            },
            {
                path: "position/",
                element: <PositionList/>,

            },
            {
                path: "type/",
                element: <TypeList/>,

            }]
    },
])