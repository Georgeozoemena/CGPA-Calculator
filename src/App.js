import './App.css';
import Input from './Component/Input';
import Navbar from './Component/Navbar'


function App() {
  return(
    <div className='container'>
      <div className='content'>
        <Navbar />
        <section className='input'>
          <Input type="number" placeholder="Current CGPA" id="1"/>
        </section>
        <section className='listed courses'></section>
        <section className='total'></section>
      </div>
    </div>
  )
}

export default App;