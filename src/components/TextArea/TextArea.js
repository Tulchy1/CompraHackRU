
function TextArea({ id }) {
    return (
        <div className="form-floating">
            <textarea style={{ height: "7rem" }} className="form-control" placeholder="Leave a comment here" id={id} required />
            <label htmlFor={id}>Problem</label>
        </div>
    )

}

export default TextArea;