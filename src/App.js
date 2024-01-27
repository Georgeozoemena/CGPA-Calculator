import './App.css';
import Input from './Component/Input';


function App() {
  return(
    <div className='container'>
      <div className='content'>
        <section className='input'>
          <Input type="number" placeholder="Current CGPA" id="1"/>
          <Input type="number" placeholder="Credit load" id="2"/>
        </section>
        <section className='listed courses'></section>
        <section className='total'></section>
      </div>
    </div>
  )
}

export default App;