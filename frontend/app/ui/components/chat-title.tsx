import Image from 'next/image';
import styles from '@/app/ui/styles/chat.module.css'

const ChatTitle: React.FC = ({}) => {
  return (
    <section className={styles.chatTitle}>
      <strong>
        LangChain Chat
      </strong>
      <Image 
        src='/chat.svg'
        alt='Chat Icon'
        height={40}
        width={40}
      />
    </section>
  );
}

export default ChatTitle;
