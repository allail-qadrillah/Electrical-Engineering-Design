from websites import create_app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True, port=5000)
  # app.run(debug=False, port='0.0.0.0')