
function InputXL({id, placeholder}) {
    return (
        <div className="form-floating my-3">
        <input type="text" className="form-control" id={id} placeholder={placeholder} required />
        <label htmlFor={id}>{placeholder}</label>
      </div>
    );
}

export default InputXL;