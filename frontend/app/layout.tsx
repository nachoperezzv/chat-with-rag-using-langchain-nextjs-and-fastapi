import Head from "next/head";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <Head>
        <link rel="icon" href="/favicon.ico"/>
        <title>LangChain Chat</title>

        <meta charSet="utf-8"/>
        <meta lang="ES" />

        <meta name="viewport" content="width=device-width"/>
        <meta name="description" content="LangChain chat app using RAG" />
      </Head>
      <body className={inter.className}>
        {children}
      </body>
    </html>
  );
}
