import logo from './logo.svg';
import './App.css';
import {createBrowserRouter, Outlet, RouterProvider} from "react-router-dom";
import Layout from "./layout/layout";

const router = createBrowserRouter([
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
            element: <div>Inside Product</div>,

        },]
    },
])

function App() {
    return (

        <RouterProvider router={router}/>
    )
        ;
}

export default App;
