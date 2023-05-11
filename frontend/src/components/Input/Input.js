

function Input({id, placeholder, my}) {
    const style = 'form-floating' + ' ' + my;
    return (
        <div className="col-6">
            <div className={style} >
                <input type="text" className="form-control" id={id} placeholder={placeholder} required />
                <label htmlFor={id}>{placeholder}</label>
            </div>
        </div>
    );
}

export default Input;