import React, { useRef, useState } from 'react';
import axios from 'axios';
import logo from './logo.jpeg';
import './App.css';

function App() {
    const input = useRef();
    const [message, setMessage] = useState('Open-source Music Recommendation Engine\n\nUpload a .wav file to generate recommendations');

    const importAudio = () => {
        setMessage('Processing... \n\n(This could take a few minutes)')

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
            .then(res => {
                let rows = [];
                rows.push('1. Artist : ' + res.data.artist[0] + '    Genre : ' + res.data.genre[0] + '    Track : ' + res.data.track[0])
                rows.push('2. Artist : ' + res.data.artist[1] + '    Genre : ' + res.data.genre[1] + '    Track : ' + res.data.track[1])
                rows.push('3. Artist : ' + res.data.artist[2] + '    Genre : ' + res.data.genre[2] + '    Track : ' + res.data.track[2])
                rows.push('4. Artist : ' + res.data.artist[3] + '    Genre : ' + res.data.genre[3] + '    Track : ' + res.data.track[3])
                rows.push('5. Artist : ' + res.data.artist[4] + '    Genre : ' + res.data.genre[4] + '    Track : ' + res.data.track[4])
                setMessage(rows.join("\n")); 
            });
    }  

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
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
