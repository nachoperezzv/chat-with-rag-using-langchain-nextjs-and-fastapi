import React from 'react';
import { useRef, useEffect } from 'react'

import styles from '@/app/ui/styles/chat.module.css';

interface Message {
  text: string;
  sender: string;
}

interface ChatBubblesProps {
  messages: Message[];
}

const ChatBubbles: React.FC<ChatBubblesProps> = ({ messages }) => {
  const messagesEndRef = useRef<null | HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]); 

  return (
    <section className={styles.chatBubbles}>
      {messages.map((msg, index) => (
        <div 
          key={index} 
          className={msg.sender === 'user' ? styles.userMessage : styles.botMessage}
        >
          {msg.text}
        </div>
      ))}
      <div ref={messagesEndRef} />
    </section>
  );
};

export default ChatBubbles;

