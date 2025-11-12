import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();
      if (res.ok) {
        setResponse(data.response);
      } else {
        setResponse(`Error: ${data.detail || "Something went wrong"}`);
      }
    } catch (err) {
      setResponse(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", textAlign: "center", fontFamily: "sans-serif" }}>
      <h1>💬 LLM Query App</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="4"
          placeholder="Ask me anything..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={{ width: "100%", padding: "10px", fontSize: "1rem" }}
          required
        />
        <button
          type="submit"
          disabled={loading}
          style={{
            marginTop: "1rem",
            padding: "10px 20px",
            fontSize: "1rem",
            cursor: "pointer",
          }}
        >
          {loading ? "Thinking..." : "Ask"}
        </button>
      </form>

      {response && (
        <div style={{ marginTop: "2rem", textAlign: "left", background: "#f9f9f9", padding: "15px", borderRadius: "8px" }}>
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
