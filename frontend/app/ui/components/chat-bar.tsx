import React from 'react';
import { useState } from 'react';

import Image from 'next/image';

import styles from '@/app/ui/styles/chat.module.css'

interface ChatBarProps {
  onSendMessage: (message: string, response: string) => void;
}

const ChatBar: React.FC<ChatBarProps> = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');
  const [file, setFile] = useState<File | null>(null);

  const onFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
      await uploadFile(e.target.files[0]); 
    }
  };

  const sendMessage = async (e: React.FormEvent) => {
    e.preventDefault();

    if (message !== '') {
      try {
        const response = await fetch('http://localhost:8000/chat/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ "msg": message }),
        });
  
        if (response.ok) {
          const responseData = await response.json(); 
          const apiMessage = responseData.result.response;
          onSendMessage(message, apiMessage);
          setMessage(''); 
        } else {
          console.error('Error en la petición a la API');
        }
      } catch (error) {
        console.error('Error al enviar el mensaje:', error);
      }
    }
  };

  const uploadFile = async (selectedFile: File) => {
    if (!selectedFile) {
      alert('Por favor, selecciona un archivo primero.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('http://localhost:8000/document', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data);
        alert('Archivo subido con éxito');
      } else {
        alert('Error al subir el archivo');
      }
    } catch (error) {
      console.error('Error al subir el archivo:', error);
      alert('Error al subir el archivo');
    }
  };

  return (
    <section className={styles.chatBar}>
        <form 
            onSubmit={sendMessage} 
            style={{ 
                display: 'flex',
                justifyContent: 'start', 
                alignItems: 'center', 
                gap: '10px',
            }}
        >
            <label htmlFor="upload-button" style={{ cursor: 'pointer' }}>
              <Image
                src={'/paperclip.svg'}
                alt={'PaperClip Icon'}
                height={20}
                width={20}
              />
              <input
                id="upload-button"
                type="file"
                style={{ display: 'none' }}
                onChange={onFileChange}
              />
            </label>
            {/* <button onClick={uploadFile} disabled={!file}>
              Subir Documento
            </button> */}
          </form>
          <form
            onSubmit={sendMessage} 
            style={{ 
                display: 'flex',
                justifyContent: 'start', 
                alignItems: 'center', 
                gap: '10px',
                width: '100%',
            }}
          >
            <textarea
                rows={1}
                className='textArea'
                placeholder="Escriba un mensaje"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                style={{ 
                    border: 'none',
                    outline: 'none',
                    color: 'white',
                    backgroundColor: 'transparent',
                    resize: 'none', 
                    overflowY: 'auto',
                    display: 'flex',
                    flex: 10,
                }}
            ></textarea>
            <button 
                type="submit" 
                style = {{
                    border: 'none',
                    cursor: 'pointer',
                    backgroundColor: 'transparent'
                }}
            >
                <Image 
                    src={'/send.svg'} 
                    alt={'Send Icon'} 
                    height={20} 
                    width={20} 
                />
            </button>
        </form>
    </section>
  );
};

export default ChatBar;
