
function Select({ defalut, options }) {

    const createOption = (element) => {
        return (
            <option>{element}</option>
        )
    };

    return (
        <select className="form-select my-4 py-2" aria-label="">
            <option selected disabled>{defalut}</option>
            {options.map(createOption)}
        </select>
    )

}

export default Select;