import React from "react";

import "./App.css";
import axios from "axios";

export default class BookTable extends React.Component {
  state = {
    books: [],
  };

  componentDidMount() {

    axios.get(process.env.REACT_APP_API + '/dev/books').then((res) => {
      const books = res.data;
      this.setState({ books });
    });
  }

  render() {
    return (
      <>
        <h1>Liste de livres</h1>
        <table className="table">
          <thead>
            <tr>
        
              <th scope="col">Author</th>
              <th scope="col">Title</th>
            </tr>
          </thead>
          <tbody>
            {this.state.books.map((item) => (
              <tr>
                
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
