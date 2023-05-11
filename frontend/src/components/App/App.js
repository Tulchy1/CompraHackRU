import './App.css';
import Input from '../Input/Input';
import Select from '../Select/Select';
import InputXL from '../Input/InputXL';
import logo from '../Images/logo.png'
import TextArea from '../TextArea/TextArea';

function App() {
  return (
    <div className="container mx-auto shadow p-3 my-4 rounded">
      <img src={logo} className="compraBetsLogo mx-auto img-fluid" />
      <form action="/process" method="post" className="registerForm mx-auto">
        <div className="row my-2">
          <Input id="Name" placeholder="Name" />
          <Input id="companyType" placeholder="Company Type" />
        </div>
        <Select defalut="Gender" options={['Female', 'Male']} />
        <InputXL id="charastitic" placeholder="Charastitic" />
        <TextArea id="Problem" />

        <input type="submit" className="btn btn-primary mx-auto my-3" id="registerButton" value="Start" />

      </form>
    </div>
  );
}

export default App;
