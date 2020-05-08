import React, { useRef, useState } from 'react';
import axios from 'axios';
import Button from './modules/Button.js'
import logo from './logo.jpeg';
import './App.css';

function App() {
    const input = useRef();
    const [message, setMessage] = useState('Upload a .wav file to generate recommendations');

    const importAudio = () => {
        setMessage('Processing... (This could take a few minutes)')

        let files = input.current.files;
        let file  = files[files.length - 1];
        
        // Validation
        if(file === undefined) {
            setMessage('The file failed to upload. Please try again.');
            return;
        }

        const data = new FormData();
        data.append('file', file);
        axios.post('http://' + document.domain + ':5000/generate', data, { })
            .then(res => { setMessage(JSON.stringify(res.data)); });
    }  

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>Open-source Music Recommendation Engine</p>
                <label>{message}</label>
                <br/>
                <input ref={input} type="file" onChange={importAudio} name="upload" />
                <br/>
                <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
                    Learn React
                </a>
            </header>
        </div>
    );
}

export default App;
