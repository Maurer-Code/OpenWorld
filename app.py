from webapp import create_app


app = create_app(debug=True)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7000, debug=True, use_reloader=False)

