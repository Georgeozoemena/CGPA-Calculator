import './App.css';
import Input from './Component/Input';
import Navbar from './Component/Navbar'


function App() {
  return(
    <div className='container'>
      <div className='content'>
        <Navbar />
        <section className='input-container'>
          <section className='input-content'>
            <section className='inputs'>
              <Input type="number" placeholder="Unit" id="1"/>
              <Input type="number" placeholder="Score" id="2"/>
              <Input type="number" placeholder="Grade" id="3"/>
            </section>
          <button type='submit'>calculate</button>
          </section>
        </section>
        <section className='listed courses'></section>
        <section className='total'></section>
      </div>
    </div>
  )
}

export default App;