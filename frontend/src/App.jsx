import { useState } from "react";
import { askChat } from "./api";

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleAsk() {
    if (!question.trim()) return;

    const userQuestion = question;

    setMessages((prev) => [
      ...prev,
      { role: "user", content: userQuestion },
    ]);

    setQuestion("");
    setLoading(true);

    try {
      const data = await askChat(userQuestion);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.response,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Something went wrong while calling the backend.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ maxWidth: 800, margin: "40px auto", fontFamily: "Arial" }}>
      <h1>AI Notes Chat</h1>

      <div style={{ border: "1px solid #ddd", padding: 16, minHeight: 300 }}>
        {messages.map((message, index) => (
          <div key={index} style={{ marginBottom: 16 }}>
            <strong>{message.role === "user" ? "You" : "AI"}:</strong>
            <p>{message.content}</p>
          </div>
        ))}

        {loading && <p>AI is thinking...</p>}
      </div>

      <div style={{ marginTop: 16, display: "flex", gap: 8 }}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask about your notes..."
          style={{ flex: 1, padding: 10 }}
        />

        <button onClick={handleAsk} disabled={loading}>
          Ask
        </button>
      </div>
    </div>
  );
}

export default App;