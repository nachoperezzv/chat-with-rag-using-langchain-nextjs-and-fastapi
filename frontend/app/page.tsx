'use client'

import React from 'react'
import { useState } from 'react';

import ChatTitle from '@/app/ui/components/chat-title';
import ChatBubbles from '@/app//ui/components/chat-bubbles';
import ChatBar from '@/app/ui/components/chat-bar';

import "@/app/globals.css";

export default function Home() {

  const [messages, setMessages] = useState<{ text: string; sender: string }[]>([]);

  const handleSendMessage = (message: string, response:string) => {
    if (!message.trim()) return;
    const newMessage = { text: message, sender: 'user' };
    setMessages([...messages, newMessage]);
    setTimeout(() => {
      setMessages(messages => [...messages, { text: response, sender: 'bot' }]);
    }, 500);
  };

  return (
    <main>
      <ChatTitle/>
      <ChatBubbles messages={messages}/>
      <ChatBar onSendMessage={handleSendMessage}/>
    </main>
  );
}
