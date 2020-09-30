import React from "react";

import "./App.css";
import axios from "axios";

export default class BookTable extends React.Component {
  state = {
    books: [],
  };

  componentDidMount() {
	
    axios.get(`http://localhost:4000/dev/books`).then((res) => {
      const books = res.data;
      this.setState({ books });
    });
  }

  render() {
    return (
	  <>
	  <h1> Liste de livres </h1>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Author</th>
            <th scope="col">Title</th>
          </tr>
        </thead>
        <tbody>
          {this.state.books.map((item, index) => (
            <tr>
              <th scope="row">{index}</th>
              <td>{item.author}</td>
              <td>{item.title}</td>
            </tr>
          ))}
        </tbody>
      </table>
	  </>
    );
  }
}
