
import React, { useEffect, useState } from "react";

function App() {
  const [books, setBooks] = useState([]);
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    // Fetch books
    fetch("http://localhost:8000/book")
      .then((res) => res.json())
      .then((data) => setBooks(data.book))
      .catch((err) => console.error("Error fetching books:", err));

    // Fetch reviews
    fetch("http://localhost:8000/reviews")
      .then((res) => res.json())
      .then((data) => setReviews(data.reviews))
      .catch((err) => console.error("Error fetching reviews:", err));
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Book List</h1>
      <ul>
        {books.map((book) =>
          typeof book === "string" ? (
            <li key={book}>{book}</li>
          ) : (
            <li key={book[0]}>{book[1]}</li>
          )
        )}
      </ul>

      <h2>Reviews</h2>
      <ul>
        {reviews.map((review) => (
          <li key={review.id}>
            <strong>{review.reviewer}</strong>: {review.comment}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
