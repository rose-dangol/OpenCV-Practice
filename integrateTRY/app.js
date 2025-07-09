import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleImageUpload = (e) => {
    setFile(e.target.files[0]);
  };

  const handleDetect = async () => {
    if (!file) return;
    const reader = new FileReader();
    reader.onloadend = async () => {
      const base64 = reader.result;
      const res = await axios.post('http://localhost:5000/detect-face', {
        image: base64,
      });
      setResult(res.data.faces_detected);
    };
    reader.readAsDataURL(file);
  };

  return (
    <div>
      <h1>Face Detection App</h1>
      <input type="file" onChange={handleImageUpload} />
      <button onClick={handleDetect}>Detect Face</button>
      {result !== null && <h2>Faces Detected: {result}</h2>}
    </div>
  );
}

export default App;
