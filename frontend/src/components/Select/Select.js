
function Select({ gender, options, id, name }) {

    const createOption = (element) => {
        return (
            <option>{element}</option>
        )
    };

    return (
        <select id={id} name={id} className="form-select my-4 py-2" aria-label="">
            <option selected disabled>{ gender }</option>
            {options.map(createOption)}
        </select>
    )

}

export default Select;