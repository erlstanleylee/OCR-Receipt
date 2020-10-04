import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h3>
          Upload a photo of your grocery receipt! And we will keep track of your inventory
        </h3>
        <form method="post" encType="multipart/form-data">
			<input type="file" name="file" id="file"></input>
			<input type="submit" value="Upload"></input>
		</form>
      </header>
    </div>
  );
}

export default App;
