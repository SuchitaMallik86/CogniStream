import { useEffect, useState } from "react";
import api from "./api";

function App() {
  const [analytics, setAnalytics] = useState(null);

  useEffect(() => {
    api.get("/analytics")
      .then((response) => {
        setAnalytics(response.data);
      })
      .catch((error) => {
  console.log(error);
  alert(error.message);

  if (error.response) {
    alert(JSON.stringify(error.response.data));
  }
});
}, []);

  const cardStyle = {
    background: "white",
    padding: "20px",
    borderRadius: "12px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    textAlign: "center",
  };

  if (!analytics) {
    return <h2 style={{ padding: "40px" }}>Loading Analytics...</h2>;
  }

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#f4f7fb",
        padding: "40px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1 style={{ color: "#4F46E5" }}>🚀 CogniStream Dashboard</h1>

      <p style={{ color: "#555", fontSize: "18px" }}>
        Developer Flow-State & Cognitive Load Analytics
      </p>

      <hr />

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        <div style={cardStyle}>
          <h2>{analytics.productivity_score}</h2>
          <p>Productivity Score</p>
        </div>

        <div style={cardStyle}>
          <h2>{analytics.flow_state}</h2>
          <p>Flow State</p>
        </div>

        <div style={cardStyle}>
          <h2>{analytics.context_switches}</h2>
          <p>Context Switches</p>
        </div>

        <div style={cardStyle}>
          <h2>{analytics.longest_flow_block}</h2>
          <p>Longest Focus</p>
        </div>
      </div>
    </div>
  );
}

export default App;